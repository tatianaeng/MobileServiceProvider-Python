# A mobile phone service provider has 3 different subscription packages for its customers:
# Package A: For $39.99 per month, 450 minutes are provided. Additional minutes are $0.45 per minute.
# Package B: For $59.99 per month, 900 minutes are provided. Additional minutes are $0.40 per minute.
# Package C: For $69.99 per month, unlimited minutes are provided.
# Write a program that calculates a customer's monthly bill.
# It should ask the user to enter the package they purchased and number of minutes used.
# The program should display the following:
#       - total charges
#       - how much money Package A customers would save if they purchased Package B or C
#       - how much money Package B customers would save if they purchased Package C
# If there would be no savings, no message should be printed.

# variables
total_cost_c = 69.99

# ask the user which service package they have
package = input("Which cell phone plan do you have? (A, B, or C)\n")

# ask the user how many minutes they used last month
# cast the input to an int so we can use for calculations later on
minutes = int(input("How many minutes did you use last month?\n"))

# total charges using Package A pricing
if (minutes > 450):
    total_cost_a = 39.99 + ((minutes - 450) * 0.45)
else:
    total_cost_a = 39.99
    
# total charges using Package B pricing
if (minutes > 900):
    total_cost_b = 59.99 + ((minutes - 900) * 0.40)
else:
    total_cost_b = 59.99

# based on which phone plan the user says they have, calculate how much they would save under other phone plans
# display the results
if (package == "a" or package == "A"):
    print(f"\nThanks, Tatiana! Your phone bill for last month's usage is ${total_cost_a:.2f}")
    savings_if_b = total_cost_a - total_cost_b
    if (savings_if_b > 0):
        print(f"If you had Package B, you would've saved ${savings_if_b:.2f} on your phone bill!")
    savings_if_c = total_cost_a - total_cost_c
    if (savings_if_c > 0):
        print(f"If you had Package C, you would've saved ${savings_if_c:.2f} on your phone bill!")
elif (package == "b" or package == "B"):
    print(f"\nThanks, Tatiana! Your phone bill for last month's usage is ${total_cost_b:.2f}")
    savings_if_c = total_cost_b - total_cost_c
    if (savings_if_c > 0):
        print(f"If you had Package C, you would've saved ${savings_if_c:.2f} on your phone bill!")
elif (package == "c" or package == "C"):
    print(f"\nThanks, Tatiana! Your phone bill for last month's usage is ${total_cost_c:.2f}")