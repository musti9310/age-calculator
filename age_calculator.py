from datetime import datetime

def check_birthdate(year, month, day):
	today = datetime.today()
	birthdate = datetime(int(year),int(month),int(day))
	if birthdate < today:
		return True
	else:
		return False	

def calculate_age(year, month, day):
	today = datetime.today()
	birthdate = datetime(int(year),int(month),int(day))
	age = ((today - birthdate).days) /365

	print("You are %d years old" %(age))
    

def main():
	year=input('Enter year of birth: ')
	month=input('Enter month of birth: ')
	day=input('Enter day of birth: ')

	if check_birthdate(year,month,day):
		calculate_age(year,month,day)
	else:
		print ("invalid birthdate")




if __name__ == '__main__':
	main()