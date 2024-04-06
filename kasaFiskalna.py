product_List = input("Podaj listę produktów oddzielonych przecinkami: ")
product_List_Unique = product_List.split(",")
product_Dict = {}
for product in product_List_Unique:
    price = float(input("Podaj cenę produktu " + product + ": "))
    product_Dict[product] = price

print(product_Dict)

# products_list = input("Enter a list of products, they have to be separated by comma: ")

# products_list = [x.strip() for x in products_list.split(',')]

# products_dict = {}

# for product in products_list:
#     price = 0
#     while price<=0:
#         price = int(input(f"Enter a {product} price: "))
#     products_dict[product] = price
#     print(f"{product}:{products_dict[product]}")
