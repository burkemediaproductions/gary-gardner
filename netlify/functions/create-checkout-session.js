const Stripe = require('stripe');

exports.handler = async (event) => {
  try {
    const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

    const body = JSON.parse(event.body || '{}');

    const amount = Math.round(parseFloat(body.donationAmount) * 100);

    if (!amount || amount < 100) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Invalid donation amount.' })
      };
    }

    const session = await stripe.checkout.sessions.create({
      mode: 'payment',
      success_url: 'https://gardnerfordhs.com/donate/thank-you/?session_id={CHECKOUT_SESSION_ID}',
      cancel_url: 'https://gardnerfordhs.com/donate/',
      customer_email: body.email,
      billing_address_collection: 'required',
      line_items: [
        {
          price_data: {
            currency: 'usd',
            product_data: {
              name: 'Campaign Donation',
              description: 'Gary Gardner for Desert Hot Springs City Council District 1'
            },
            unit_amount: amount
          },
          quantity: 1
        }
      ],
      metadata: {
        first_name: body.firstName || '',
        last_name: body.lastName || '',
        occupation: body.occupation || '',
        phone: body.phone || '',
        address_1: body.address1 || '',
        address_2: body.address2 || '',
        city: body.city || '',
        state: body.state || '',
        zip: body.zip || '',
        country: body.country || ''
      }
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ url: session.url })
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({
        error: error.message || 'Server error'
      })
    };
  }
};