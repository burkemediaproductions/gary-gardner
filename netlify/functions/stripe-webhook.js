const Stripe = require("stripe");
const { Resend } = require("resend");

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
      const fullName = [firstName, lastName].filter(Boolean).join(" ").trim() || "Unknown donor";

      const amount =
        typeof session.amount_total === "number"
          ? new Intl.NumberFormat("en-US", {
              style: "currency",
              currency: (session.currency || "usd").toUpperCase()
            }).format(session.amount_total / 100)
          : "Unknown amount";

      const campaignEmails = (process.env.CAMPAIGN_NOTIFICATION_EMAILS || "")
		  .split(",")
		  .map(e => e.trim())
		  .filter(Boolean);
      const fromEmail = process.env.EMAIL_FROM;

      if (!campaignEmail || !fromEmail || !process.env.RESEND_API_KEY) {
        console.warn("Email env vars missing; skipping campaign email.");
      } else {
        const html = `
          <div style="font-family: Arial, sans-serif; line-height:1.6; color:#222;">
            <h2 style="margin:0 0 16px;">New Donation Received</h2>
            <p style="margin:0 0 16px;">
              A new donation was completed through Stripe Checkout.
            </p>

            <table cellpadding="8" cellspacing="0" border="1" style="border-collapse:collapse; width:100%; max-width:700px;">
              <tr><td><strong>Name</strong></td><td>${escapeHtml(fullName)}</td></tr>
              <tr><td><strong>First Name</strong></td><td>${escapeHtml(firstName)}</td></tr>
              <tr><td><strong>Last Name</strong></td><td>${escapeHtml(lastName)}</td></tr>
              <tr><td><strong>Email</strong></td><td>${escapeHtml(session.customer_email || metadata.email || "")}</td></tr>
              <tr><td><strong>Phone</strong></td><td>${escapeHtml(metadata.phone || "")}</td></tr>
              <tr><td><strong>Occupation</strong></td><td>${escapeHtml(metadata.occupation || "")}</td></tr>
              <tr><td><strong>Donation Amount</strong></td><td>${escapeHtml(amount)}</td></tr>
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
          subject: `New Donation: ${fullName} - ${amount}`,
          html
        });
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