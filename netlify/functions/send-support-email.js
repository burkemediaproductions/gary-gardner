const { Resend } = require("resend");

const resend = new Resend(process.env.RESEND_API_KEY);

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method Not Allowed" };
  }

  try {
    const data = JSON.parse(event.body || "{}");

    const subject = `New Campaign Support Form: ${data.firstName || ""} ${data.lastName || ""}`.trim();

    const html = `
      <h2>New Campaign Support Form Submission</h2>
      <p><strong>Name:</strong> ${data.firstName || ""} ${data.lastName || ""}</p>
      <p><strong>Email:</strong> ${data.email || ""}</p>
      <p><strong>Phone:</strong> ${data.phone || ""}</p>
      <p><strong>Support Options:</strong> ${data.supportOptions || ""}</p>
      <p><strong>Donation Amount:</strong> ${data.donationAmount || ""}</p>
      <p><strong>Occupation:</strong> ${data.occupation || ""}</p>
      <p><strong>Address:</strong><br>
        ${data.address1 || ""}<br>
        ${data.address2 || ""}<br>
        ${data.city || ""}, ${data.state || ""} ${data.zip || ""}<br>
        ${data.country || ""}
      </p>
      <p><strong>Message:</strong><br>${data.message || ""}</p>
      <hr>
      <pre>${JSON.stringify(data, null, 2)}</pre>
    `;

    const toEmails = (process.env.CAMPAIGN_NOTIFICATION_EMAILS || "")
    .split(",")
    .map(e => e.trim())
    .filter(Boolean);

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