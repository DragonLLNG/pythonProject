from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another  product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break
salesTaxRate = Invoice().inputNumber("Please enter sales tax for this invoice (%) : ")

total_amount = Invoice().totalPurePrice(products)

tax_amount = Invoice().calculateTax(products, salesTaxRate)

final_amount = Invoice().finalPrice(products,salesTaxRate)

print("Your total pure price is: ", total_amount)
print("You final price with tax is: ", final_amount)