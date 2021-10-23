#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator.")
total_bill=input("What was the total Bill?")
tip=input("What percentage of tip would you like to give? 10, 12 or 15?")
people=input("How many people to split the bill in ?")
tip=(float(total_bill)*float(tip)/100)
print(tip)
total=float(total_bill)+tip
print(round(total,2))
each_person_pay=round(float(total)/float(people),2)
print(f"The number is {each_person_pay:.2f}")

