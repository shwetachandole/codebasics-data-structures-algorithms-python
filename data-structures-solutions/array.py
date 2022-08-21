'''
1. Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

exp = [2200, 2350, 2600, 2130, 2190]

def findexp(exp, n):
    if n in exp:
        for index, value in enumerate(exp):
            if value == n:
                print(f"Yes, expense of {value} found in month {index+1}.")
    else:
        print(f"${n} value not found in expenses.")


def adjustexp(exp, month, value):
    exp[month-1] = exp[month-1]-value
    return exp
# print array exp
print("List of expenses from Jan to May this year is ", exp)

# compare February expenses to January
print("Q1: How many dollars did you spend extra in Feb compared to Jan? \nA1:", exp[1]-exp[0])

# total expense in first quarter
print("Q2: What is the total expense in the first quarter on the year? \nA2:", sum(exp[0:3]))

# find exact value in array
print("Q3: Did you spend exact $2000 in any months? \nA3:", end=" ")
findexp(exp, 2000)

# add June month exp to array
exp.append(1980)
print("Q4: Add expense of $1980 for June month to the expenses list. \nA4:", exp)

# make adjustment to array for $200 refund in April
print("Q5: If a refund of $200 was received in April, make an adjustment to the expenses accordingly. \nA5: Updated expenses are", adjustexp(exp, 4, 200))
