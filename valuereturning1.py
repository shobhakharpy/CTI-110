def main ():

    price = get_price()

    sales_price = price - discount(price)

    print ("The sales price is:", sales_price)


def get_price():
    price = int(input("Please enter price:"))

    return price

def discount (price):
    discount = price*0.10

    return discount

main()
