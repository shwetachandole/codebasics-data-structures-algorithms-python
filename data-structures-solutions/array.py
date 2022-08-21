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
print("\nList of expenses from Jan to May this year is ", exp)

# compare February expenses to January
print("Q1.1: How many dollars did you spend extra in Feb compared to Jan? \nA1.1:", exp[1]-exp[0])

# total expense in first quarter
print("Q1.2: What is the total expense in the first quarter on the year? \nA1.2:", sum(exp[0:3]))

# find exact value in array
print("Q1.3: Did you spend exact $2000 in any months? \nA1.3:", end=" ")
findexp(exp, 2000)

# add June month exp to array
exp.append(1980)
print("Q1.4: Add expense of $1980 for June month to the expenses list. \nA1.4:", exp)

# make adjustment to array for $200 refund in April
print("Q1.5: If a refund of $200 was received in April, make an adjustment to the expenses accordingly. \nA1.5: Updated expenses are", adjustexp(exp, 4, 200))

'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''
heroes=['spider man','thor','hulk','iron man','captain america']

# print list of superheroes
print("\nList of favorite marvel superheroes is", heroes)

# 1. Length of the list
print("Q2.1: Print length of list. \nA2.1: Length of the list heros is", len(heroes))

# 2. Add 'black panther' at the end of this list
heroes.append('black panther')
print("Q2.2: Add black panther to the list. \nA2.2: Updated list", heroes)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
print("Q2.3: Remove black panther from the end and add after hulk. \nA2.3:", end=" ")
heroes.insert(3, heroes.pop())
print(heroes)

# 4. Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
heroes = [ele for ele in heroes if ele not in ('thor', 'hulk')] + ['doctor strange']
print("Q2.4: Remove thor and hulk and add doctor strange using one line of code. \nA2.4: Updated list", heroes)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heroes.sort()
print("Q2.5: Sort the list alphabetically. \nA2.5: Sorted list", heroes,"\n")

'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''
# define function to list odd numbers
def listoddnums():
    ls = []
    n = int(input("Enter max number to print all odd numbers from 1 to given max number:"))
    for i in range(1,n+1):
        if i%2 == 1:
            ls.append(i)
    print(ls)
    print("\n")

listoddnums()
