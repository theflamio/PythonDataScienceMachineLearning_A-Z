import math
import numpy as np

'''
You have been supplied with tow list of data:

1: monthly revenue 
2: monthly expenses

for the financial year in question.

Your task is to calculate the following financial metrics:

- profit of each month.
- profit after tax for each month (tax = 30%).
- profit margin for each month . equals to profit after tax devided be revenue.
- good months - where profit after tax was greaten than the mean of the year.
- bad months - where profit after tax was lees than the mean for the year.
- the best month - where the profit after tax was max for the year.
- the worst month - where the profit after tax was min for the year.

'''

'''

All results need to be presented as lists.

Results for dollar values need to be calculated with 0.01 precision, but need to be presented in Units of 1,000 dollars = 1K with no decimal points.

Results for the profit margin ration need to be presented in units of % with no decimal points.

Note: Your colleague has warned you that it is okay for tax for any given month to be negative (in accounting terms, negative tax translates into defeered tax asset).

'''

'''
Hint 1

round()
max()
min()

Hint 2

# Operations with two lists

ab = []

for i in range(0, len(list)):
    ab,append(a[i] * b[i])

ab

# List comprehensions
List comprehensions provide a concise way to create lists.
Common applications are to make new lists where each element is the result of some operations applied
to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy 
a certain condition.

doubled_a = [i * 2 for i in a]
doubled_a

'''
#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

# PrintResults in 1 k dollars with no decimal
def PrintResults(inputResult):
    months = ["January", "February","March","April","May","June","july","August", "September", "Oktober", "November", "December"]
    for i in range(0, len(inputResult)):
        print(months[i],round(inputResult[i] / 1000), "k dollars")

# Calculate Renenue after tax on 30 %
def RenenueAfterTax(renevue):
    profit = []
    for i in range (0, len(renevue)):
        profit.append(renevue[i] * 0.70)
    return profit

#Calculate Profit As The Differences Between Revenue And Expenses
def CalculateRevenue(renevue, expenses):
    profit = []
    for i in range (0, len(renevue)):
        profit.append(round(renevue[i] - expenses [i],2))
    return profit

# Calculate profit margin for each month . equals to profit after tax devided be revenue.
def CalculateProfitMargin(renevueAfterTax, renevue):
    margin = []
    for i in range (0, len(renevueAfterTax)):
        margin.append(renevueAfterTax[i] / renevue [i])
    return margin

# Calculate the best month - where the profit after tax was max for the year.
def BestMonth(profitAfterTax):
    bestmonth = max(profitAfterTax)
    return bestmonth

# Calculate  the worst month - where the profit after tax was min for the year.
def WorstMonth(profitAfterTax):
    worstMonth = min(profitAfterTax)
    return worstMonth

# Calculate good months - where profit after tax was greaten than the mean of the year.
def GoodMonths(profitAfterTax):
    goodMonths = []
    meanOfYear = np.mean(profitAfterTax)
    for i in range (0, len(profitAfterTax)):
        if(profitAfterTax[i] > meanOfYear):
            goodMonths.append(profitAfterTax[i])
    return goodMonths


# Calculate bad months - where profit after tax was lees than the mean for the year.
def BadMonths(profitAfterTax):
    badMonths = []
    meanOfYear = np.mean(profitAfterTax)
    for i in range (0, len(profitAfterTax)):
        if(profitAfterTax[i] < meanOfYear):
            badMonths.append(profitAfterTax[i])
    return badMonths

#Print Results
print ("Revenue :") 
PrintResults(CalculateRevenue(revenue, expenses))

# Revenue after taxes
print ("Profit after tax :")
PrintResults (RenenueAfterTax(CalculateRevenue(revenue, expenses)))

print ("Profit margin :")
PrintResults (CalculateProfitMargin(RenenueAfterTax(CalculateRevenue(revenue, expenses)), CalculateRevenue(revenue, expenses)))

print ("Good months :")
print (GoodMonths(RenenueAfterTax(CalculateRevenue(revenue, expenses))))

print ("Bad months :")
print (BadMonths(RenenueAfterTax(CalculateRevenue(revenue, expenses))))

print ("Best month :")
print (BestMonth(RenenueAfterTax(CalculateRevenue(revenue, expenses))))

print ("Worst month :")
print (WorstMonth(RenenueAfterTax(CalculateRevenue(revenue, expenses))))