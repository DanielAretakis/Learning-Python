houseprice = float(input('Type the price of the house: '))
salary = float(input('How much money do you make for month? '))
years = int(input('In how many years do you want to pay the loan? '))
loanprice = houseprice/(years*12)
if loanprice > salary*0.3:
    print("You can't buy this house at the moment in that amount of time, choose more time or try again when you've been promoted")
else:
    print(f"Your loan was accepted!! You have to pay {loanprice :.2f} every month in a total of {years} years")