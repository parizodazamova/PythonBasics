cars_sale = ['dugati vayron', 'tesla Model Y', 'bmw m5', 'ferrari F80']
cars_sold = []



for i in range(4): #0,1,2,3,4
    print(f'We got a great offer for {cars_sale[0].title()}')
    print(f"{cars_sale[0].upper()} is sold!!!")
    #remove car from the list
    cars_sold.append(cars_sale.pop(0))
    print(f"We still have these cars for you: {cars_sale}")
print(f"Here is the list of sold cars today: {cars_sold}")
print("***** All cars are sold out!!! *****")