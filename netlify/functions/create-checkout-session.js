const Stripe = require("stripe");

exports.handler = async (event) => {
  try {
    const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

    const body = JSON.parse(event.body || "{}");

    const amount = Math.round(parseFloat(body.donationAmount) * 100);

    if (!amount || amount < 100) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: "Invalid donation amount." })
      };
    }

    const proto =
      event.headers["x-forwarded-proto"] ||
      event.headers["X-Forwarded-Proto"] ||
      "https";

    const host =
      event.headers["x-forwarded-host"] ||
      event.headers["host"];

    const baseUrl = `${proto}://${host}`;

    const session = await stripe.checkout.sessions.create({
      mode: "payment",
      success_url: `${baseUrl}/donate/thank-you/?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${baseUrl}/donate/`,
      customer_email: body.email || undefined,
      billing_address_collection: "required",
      line_items: [
        {
          price_data: {
            currency: "usd",
            product_data: {
              name: "Campaign Donation",
              description: "Gary Gardner for Desert Hot Springs City Council District 1"
            },
            unit_amount: amount
          },
          quantity: 1
        }
      ],
      metadata: {
        first_name: body.firstName || "",
        last_name: body.lastName || "",
        occupation: body.occupation || "",
        phone: body.phone || "",
        email: body.email || "",
        address_1: body.address1 || "",
        address_2: body.address2 || "",
        city: body.city || "",
        state: body.state || "",
        zip: body.zip || "",
        country: body.country || "",
        donation_amount: String(body.donationAmount || "")
      }
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ url: session.url })
    };
  } catch (error) {
    console.error("create-checkout-session error:", error);

    return {
      statusCode: 500,
      body: JSON.stringify({
        error: error.message || "Server error"
      })
    };
  }
};
