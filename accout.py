import stripe
charge = stripe.Charge.retrieve(
  "ch_3Lmjoz2eZvKYlo2C1rBER4Dk",
  stripe_account="acct_1032D82eZvKYlo2C"
)
charge.capture() # Uses the same account.