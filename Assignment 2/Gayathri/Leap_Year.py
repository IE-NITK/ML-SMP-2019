#To check if the entered date falls under a leap year
def is_leap_baby(day,month,year):
	if day == 29:
		if month == "Feb" or month == "feb": 
			print("Checking with year of birth")
			if year%4 == 0 & year%100 == 0:
				print("It's a leap year")
			else:
				print("It's not a leap year")		
		else:
			print("It's not a leap year")
	else:
		print("It's not a leap year")			
day = int(input("Enter the day : "))
month = str(input("Enter the month : "))
year = int(input("Enter the year : "))
is_leap_baby(day,month,year)
