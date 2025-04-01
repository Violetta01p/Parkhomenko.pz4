products = []
num_products = int(input("Enter the number of products: "))


for i in range(num_products):
   name = input("Enter product name: ")
   price = float(input("Enter product price: "))
   quantity = int(input("Enter product quantity: "))
   products.append((name, price, quantity))


print("\n{:<20} {:>10} {:^8}".format("Product Name", "Price", "Qty"))
print("-" * 40)


for name, price, quantity in products:
   print("{:<20} {:>10.2f} {:^8}".format(name, price, quantity))
