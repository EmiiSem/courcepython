import stripe

charge = stripe.Charge.retrieve(
  "ch_3Ln3e92eZvKYlo2C0eUfv7bi",
  api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"
)
charge.capture() # Uses the same API Key.