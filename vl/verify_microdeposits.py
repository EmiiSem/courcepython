import stripe
stripe.api_key = "sk_test_51OlWIPH7oiewvnTBVQDI6gsybpaqeFCLVYcIbQDroJhm11QHxqAgthPxApZJBFLojK6UwCBtQZgY1iWCVO5Y6F4K00kjNVHkNg"

stripe.PaymentIntent.verify_microdeposits(
  "pi_1DtBRR2eZvKYlo2CmCVxxvd7",
  amounts=[32, 45],
)