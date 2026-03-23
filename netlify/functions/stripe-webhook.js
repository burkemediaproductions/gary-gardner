const Stripe = require("stripe");
const { Resend } = require("resend");
const { google } = require("googleapis");

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
const resend = new Resend(process.env.RESEND_API_KEY);

exports.handler = async (event) => {
  try {
    const signature =
      event.headers["stripe-signature"] || event.headers["Stripe-Signature"];

    if (!signature) {
      return {
        statusCode: 400,
        body: "Missing Stripe signature"
      };
    }

    const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
    if (!webhookSecret) {
      return {
        statusCode: 500,
        body: "Missing STRIPE_WEBHOOK_SECRET"
      };
    }

    const stripeEvent = stripe.webhooks.constructEvent(
      event.body,
      signature,
      webhookSecret
    );

    if (stripeEvent.type === "checkout.session.completed") {
      const session = stripeEvent.data.object;
      const metadata = session.metadata || {};

      const firstName = metadata.first_name || "";
      const lastName = metadata.last_name || "";
      const fullName =
        [firstName, lastName].filter(Boolean).join(" ").trim() || "Unknown donor";

      const donorEmail = session.customer_email || metadata.email || "";
      const amountNumber =
        typeof session.amount_total === "number" ? session.amount_total / 100 : null;

      const amountFormatted =
        amountNumber !== null
          ? new Intl.NumberFormat("en-US", {
              style: "currency",
              currency: (session.currency || "usd").toUpperCase()
            }).format(amountNumber)
          : "Unknown amount";

      const campaignEmails = (process.env.CAMPAIGN_NOTIFICATION_EMAILS || "")
        .split(",")
        .map((e) => e.trim())
        .filter(Boolean);

      const fromEmail = process.env.EMAIL_FROM;

      // 1) Email the campaign
      if (campaignEmails.length && fromEmail && process.env.RESEND_API_KEY) {
        const campaignHtml = `
          <div style="font-family: Arial, sans-serif; line-height:1.6; color:#222;">
            <h2 style="margin:0 0 16px;">New Donation Received</h2>
            <p style="margin:0 0 16px;">A new donation was completed through Stripe Checkout.</p>

            <table cellpadding="8" cellspacing="0" border="1" style="border-collapse:collapse; width:100%; max-width:700px;">
              <tr><td><strong>Name</strong></td><td>${escapeHtml(fullName)}</td></tr>
              <tr><td><strong>First Name</strong></td><td>${escapeHtml(firstName)}</td></tr>
              <tr><td><strong>Last Name</strong></td><td>${escapeHtml(lastName)}</td></tr>
              <tr><td><strong>Email</strong></td><td>${escapeHtml(donorEmail)}</td></tr>
              <tr><td><strong>Phone</strong></td><td>${escapeHtml(metadata.phone || "")}</td></tr>
              <tr><td><strong>Occupation</strong></td><td>${escapeHtml(metadata.occupation || "")}</td></tr>
              <tr><td><strong>Donation Amount</strong></td><td>${escapeHtml(amountFormatted)}</td></tr>
              <tr><td><strong>Street Address</strong></td><td>${escapeHtml(metadata.address_1 || "")}</td></tr>
              <tr><td><strong>Address Line 2</strong></td><td>${escapeHtml(metadata.address_2 || "")}</td></tr>
              <tr><td><strong>City</strong></td><td>${escapeHtml(metadata.city || "")}</td></tr>
              <tr><td><strong>State / Region</strong></td><td>${escapeHtml(metadata.state || "")}</td></tr>
              <tr><td><strong>ZIP / Postal</strong></td><td>${escapeHtml(metadata.zip || "")}</td></tr>
              <tr><td><strong>Country</strong></td><td>${escapeHtml(metadata.country || "")}</td></tr>
              <tr><td><strong>Stripe Session ID</strong></td><td>${escapeHtml(session.id || "")}</td></tr>
              <tr><td><strong>Payment Status</strong></td><td>${escapeHtml(session.payment_status || "")}</td></tr>
            </table>
          </div>
        `;

        await resend.emails.send({
          from: fromEmail,
          to: campaignEmails,
          subject: `New Donation${fullName ? `: ${fullName}` : ""} - ${amountFormatted}`,
          html: campaignHtml
        });
      }

      // 2) Email the donor
      if (donorEmail && fromEmail && process.env.RESEND_API_KEY) {
        const donorHtml = `
          <div style="font-family: Arial, sans-serif; line-height:1.6; color:#222;">
            <h2 style="margin:0 0 16px;">Thank You${fullName !== "Unknown donor" ? `, ${escapeHtml(fullName)}` : ""}!</h2>
            <p style="margin:0 0 16px;">
              We appreciate your contribution to Gary Gardner for Desert Hot Springs City Council District 1.
            </p>
            <p style="margin:0 0 16px;">
              <strong>Donation amount:</strong> ${escapeHtml(amountFormatted)}
            </p>
            <p style="margin:0 0 16px;">
              Your support helps move Desert Hot Springs forward.
            </p>
            <p style="margin:24px 0 0;">
              Gary Gardner for Desert Hot Springs City Council 2026<br>
              PO Box 333, Desert Hot Springs, CA 92240<br>
              FPPC#: 1405627<br>
              EIN: 82-5194248
            </p>
          </div>
        `;

        await resend.emails.send({
          from: fromEmail,
          to: [donorEmail],
          subject: `Thank you for your donation${firstName ? `, ${firstName}` : ""}!`,
          html: donorHtml
        });
      }

      // 3) Append to Google Sheets
      if (
        process.env.GOOGLE_SHEETS_CLIENT_EMAIL &&
        process.env.GOOGLE_SHEETS_PRIVATE_KEY &&
        process.env.GOOGLE_SHEETS_SPREADSHEET_ID
      ) {
        const auth = new google.auth.JWT({
          email: process.env.GOOGLE_SHEETS_CLIENT_EMAIL,
          key: process.env.GOOGLE_SHEETS_PRIVATE_KEY.replace(/\\n/g, "\n"),
          scopes: ["https://www.googleapis.com/auth/spreadsheets"]
        });

        const sheets = google.sheets({ version: "v4", auth });
        const range = `${process.env.GOOGLE_SHEETS_TAB_NAME || "Donations"}!A:Q`;

        await sheets.spreadsheets.values.append({
          spreadsheetId: process.env.GOOGLE_SHEETS_SPREADSHEET_ID,
          range,
          valueInputOption: "USER_ENTERED",
          insertDataOption: "INSERT_ROWS",
          resource: {
            values: [[
              new Date().toISOString(),
              firstName,
              lastName,
              fullName,
              donorEmail,
              metadata.phone || "",
              metadata.occupation || "",
              amountNumber !== null ? amountNumber : "",
              (session.currency || "usd").toUpperCase(),
              metadata.address_1 || "",
              metadata.address_2 || "",
              metadata.city || "",
              metadata.state || "",
              metadata.zip || "",
              metadata.country || "",
              session.id || "",
              session.payment_status || ""
            ]]
          }
        });
      } else {
        console.warn("Google Sheets env vars missing; skipping sheet append.");
      }
    }

    return {
      statusCode: 200,
      body: JSON.stringify({ received: true })
    };
  } catch (err) {
    console.error("Webhook error:", err.message);
    return {
      statusCode: 400,
      body: `Webhook Error: ${err.message}`
    };
  }
};

function escapeHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}