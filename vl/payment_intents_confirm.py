import stripe
stripe.api_key = "sk_test_51OlWIPH7oiewvnTBVQDI6gsybpaqeFCLVYcIbQDroJhm11QHxqAgthPxApZJBFLojK6UwCBtQZgY1iWCVO5Y6F4K00kjNVHkNg"

stripe.PaymentIntent.confirm(
  "pi_3MtweELkdIwHu7ix0Dt0gF2H",
  payment_method="pm_card_visa",
  return_url="https://www.example.com",
)