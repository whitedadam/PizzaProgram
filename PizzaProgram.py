# This is a simple project made with requirements and a prompt from Codecademy. If is a program for a pizza shop to organize their sales data.
# Created by John Adam Gordon Whited

# Creating 2 lists. One for the types of slices, called 'toppings'. The other for the price of each slice, 'prices'.
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

# Creating a variable that will make it easier to print how many types of slices the store can offer.
num_pizzas = len(toppings)

# Defining a function that will give a string to greet/sell the diversity of the store's products.
def sales_pitch(x):
  return "Welcome to Len's Slice. We sell " + str(num_pizzas) + " different kinda of pizza!"

# Printing the sales_pitch() function.
print(sales_pitch(num_pizzas))
print(" ")

# Zipping the prices & toppings list into one master list 'pizzas'. This is followed by a few print functions to address the customer and a formatting line.
pizzas = list(zip(prices, toppings))
pizzas.sort()
print("Here are all of our pizza options: ")
print(pizzas)
print(" ")

# To add depth to the sales options we create a few new lists for the cheapest pizza, the priciest pizza, and a combo of the 3 cheapest options sans cheese. These are all individually followed by a few print functions to address the customer and a formatting line.
print("Our cheapest pizza option is: ")
cheapest_pizza = pizzas[0]
print(cheapest_pizza)
print(" ")

print("Our priciest pizza option is: ")
priciest_pizza = pizzas[-1]
print(priciest_pizza)
print(" ")

print("Here's the Cheapest 3 Options, Larry, Curly, and Moe: ")
three_cheapest = pizzas[:3]
print(three_cheapest)
print(" ")

print("If you're short on cash, here's how many $2 options we have: ")
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
print(" ")

# End of project. 4/1/2020
      
