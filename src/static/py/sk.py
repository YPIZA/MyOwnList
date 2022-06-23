import stripe
charge = stripe.Charge.retrieve(
  "ch_3L9Iun2eZvKYlo2C1zKiHHho",
  api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"
)
print(charge.save())