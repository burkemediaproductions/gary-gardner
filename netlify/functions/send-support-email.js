const { Resend } = require("resend");

const resend = new Resend(process.env.RESEND_API_KEY);

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method Not Allowed" };
  }

  try {
    const data = JSON.parse(event.body || "{}");

    const fullName = [data.firstName, data.lastName].filter(Boolean).join(" ").trim() || "Unknown Supporter";

    const selected = String(data.supportOptions || "")
      .split(",")
      .map((item) => item.trim())
      .filter(Boolean);

    const wantsDonation = selected.includes("Donate to Gary");
    const wantsEndorsement = selected.includes("Endorse Gary");
    const wantsVolunteer = selected.includes("Volunteer to help Gary's campaign");

    const requestTypes = [];
    if (wantsEndorsement) requestTypes.push("Endorsement");
    if (wantsDonation) requestTypes.push("Donation");
    if (wantsVolunteer) requestTypes.push("Volunteer Request");

    const subject = `${requestTypes.join("/")} from ${fullName}`;

    const sections = [];

    sections.push(`
      <h2>${escapeHtml(subject)}</h2>
      <p><strong>Name:</strong> ${escapeHtml(fullName)}</p>
      <p><strong>Email:</strong> ${escapeHtml(data.email || "")}</p>
      <p><strong>Phone:</strong> ${escapeHtml(data.phone || "")}</p>
      ${data["title-occupation"] ? `<p><strong>Title:</strong> ${escapeHtml(data["title-occupation"])}</p>` : ""}
    `);

    if (wantsEndorsement) {
      sections.push(`
        <hr>
        <h3>Endorsement Details</h3>
        <p><strong>Endorser Type:</strong> ${escapeHtml(data["endorser-type"] || "")}</p>
        ${data["endorsement-individual-name"] ? `<p><strong>Individual Name:</strong> ${escapeHtml(data["endorsement-individual-name"])}</p>` : ""}
        ${data["endorsement-group-name"] ? `<p><strong>Group Name:</strong> ${escapeHtml(data["endorsement-group-name"])}</p>` : ""}
        ${data["endorsement-business-organization-name"] ? `<p><strong>Business / Organization:</strong> ${escapeHtml(data["endorsement-business-organization-name"])}</p>` : ""}
        ${data["endorsement-message"] ? `<p><strong>Endorsement Message:</strong><br>${escapeHtml(data["endorsement-message"])}</p>` : ""}
        <p><strong>Public Consent:</strong> ${escapeHtml(data["endorsement-public-consent"] || "")}</p>
      `);
    }

    if (wantsDonation) {
      sections.push(`
        <hr>
        <h3>Donation Details</h3>
        <p><strong>Donation Amount:</strong> ${escapeHtml(formatMoney(data.donationAmount))}</p>
        <p><strong>Occupation:</strong> ${escapeHtml(data.occupation || data["donation-occupation"] || "")}</p>
        <p><strong>Address:</strong><br>
          ${escapeHtml(data.address1 || data["donation-address-line-1"] || "")}<br>
          ${escapeHtml(data.address2 || data["donation-address-line-2"] || "")}<br>
          ${escapeHtml(data.city || data["donation-city"] || "")}, ${escapeHtml(data.state || data["donation-state-region"] || "")} ${escapeHtml(data.zip || data["donation-zip-postal"] || "")}<br>
          ${escapeHtml(data.country || data["donation-country"] || "")}
        </p>
        <p><em>Note: this email means the support form was submitted. The Stripe webhook still confirms completed payment separately.</em></p>
      `);
    }

    if (wantsVolunteer) {
      sections.push(`
        <hr>
        <h3>Volunteer Details</h3>
        <p><strong>Help Areas:</strong> ${escapeHtml(data["volunteer-help-areas"] || "")}</p>
        ${data["volunteer-help-other"] ? `<p><strong>Other Help:</strong> ${escapeHtml(data["volunteer-help-other"])}</p>` : ""}
        <p><strong>Availability:</strong> ${escapeHtml(data["volunteer-availability"] || "")}</p>
      `);
    }

    if (data.message) {
      sections.push(`
        <hr>
        <h3>Additional Message</h3>
        <p>${escapeHtml(data.message)}</p>
      `);
    }

    const html = `
      <div style="font-family: Arial, sans-serif; line-height:1.6; color:#222;">
        ${sections.join("")}
      </div>
    `;

    const toEmails = (process.env.CAMPAIGN_NOTIFICATION_EMAILS || "")
      .split(",")
      .map((e) => e.trim())
      .filter(Boolean);

    if (!toEmails.length) {
      throw new Error("No campaign notification emails configured.");
    }

    const result = await resend.emails.send({
      from: process.env.EMAIL_FROM,
      to: toEmails,
      replyTo: data.email || undefined,
      subject,
      html
    });

    if (result.error) {
      throw new Error(result.error.message || "Resend failed.");
    }

    return {
      statusCode: 200,
      body: JSON.stringify({ success: true, id: result.data?.id })
    };
  } catch (error) {
    console.error("Support email error:", error);
    return {
      statusCode: 500,
      body: JSON.stringify({ success: false, error: error.message })
    };
  }
};

function formatMoney(value) {
  if (!value) return "";
  const cleaned = String(value).replace("$", "").trim();
  return cleaned ? `$${cleaned}` : "";
}

function escapeHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}