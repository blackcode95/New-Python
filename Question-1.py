# Question 1: You are at the grocery store and have a list of items and their prices.

# Write a Python function to calculate the total bill amount for a shopping cart containing these items.
# The function should take two lists as input: one containing the item names and another containing their corresponding prices.
# Make sure to handle scenarios where the item prices are not given or the lists are of different lengths.

from unittest import result


def cal_total_bill(items,prices):
    if len(items) != len(prices):
        return "Error"
    
    total_bill = 0
    for i in prices:
        total_bill += i
    return total_bill
    
    
items_lists = ["apple","banana","milk","bread"]
prices_lists = [100,60,33,48]
ammount = cal_total_bill(items_lists,prices_lists)
print("Total bill = ", ammount)


# Question 2: Some items in the grocery store have discounts.

# Write a Python function that calculates the discounted bill amount by reducing the price of items with a discount of 10%.
# The function should take the original price list and a list of items eligible for the discount, and then return the discounted total bill amount.

def cal_dis_bill(org_price,dis_items):
    dis_bill = 0
    for i in range(len(org_price)):
        if dis_items[i]:
            dis_bill += org_price[i] * 0.9
        else:
            dis_bill += org_price[i]
    return dis_bill


org_price_lt = [100,60,33,48]
dis_items_lt = [True,False,False,True]
dis_bill_ammount = cal_dis_bill(org_price_lt,dis_items_lt)
print("Discounted Bill Amount = ", dis_bill_ammount)

# Question: Write a Python function that takes a list of numbers as input and returns the count of even numbers in the list.

def count_even_numbers(num):
    even_num = [n for n in num if n % 2 == 0]
    return even_num

num = [1,5,8,6,5,7,15,25,14,546,52,69,78]
result = count_even_numbers(num)
print("Even Numbers are: ", result)
print(len(result))
