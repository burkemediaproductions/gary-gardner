const Stripe = require("stripe");

exports.handler = async (event) => {
  try {
    const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

    const sessionId =
      event.queryStringParameters &&
      event.queryStringParameters.session_id;

    if (!sessionId) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: "Missing session_id" })
      };
    }

    const session = await stripe.checkout.sessions.retrieve(sessionId);

    return {
      statusCode: 200,
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        id: session.id,
        payment_status: session.payment_status,
        customer_email: session.customer_email || "",
        amount_total: session.amount_total || 0,
        currency: session.currency || "usd",
        metadata: session.metadata || {}
      })
    };
  } catch (error) {
    console.error("get-checkout-session error:", error);

    return {
      statusCode: 500,
      body: JSON.stringify({
        error: error.message || "Unable to retrieve session"
      })
    };
  }
};
