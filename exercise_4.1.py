#The algorithmic building blocks

#1a) Write a Python program that prompts for two inputs: 
# the before tax price of an item, and the discount offered on it (as a percentage). 
# The program should then calculate and display the new price, given that the sales tax rate is 17.5%.

def exercise_1a():
    def get_inputs():
        price= float(input("give the before tax price as a float: "))
        discount = int(input ("give the discount percentage as a float (1-100): "))
        return price, discount
    
    def get_new_price(price, discount):
        return print(f"post tax price with discount: £{round(price*(1-discount/100)*1.175, 2)}")

    price, discount = get_inputs()
    get_new_price(price, discount)

exercise_1a()


