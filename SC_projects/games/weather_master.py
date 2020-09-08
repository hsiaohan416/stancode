"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100

def main():
	"""
	TODO:
	"""
	print('\"Welcome to HAN weather:)\" ')
	print('Please enter the temperature: ')
	temp = int(input('Next temperature: (or -100 to quit): '))
	if temp == EXIT:
		print('No Data Entered:( ')
		temp = int(input('Next temperature: (or -100 to quit): '))
	else:
		maximum = temp
		minimum = temp
		total = temp
		mean = total
		num = 1
		if temp < 16:
			cold = 1
		else:
			cold = 0
		while True:
			temp = int(input('Next temperature: (or -100 to quit): '))
			if temp == EXIT:
				break
			elif temp > maximum:
				maximum = temp
			elif temp < minimum:
				minimum = temp
			if temp < 16:
				cold = cold+1
			total = total + temp
			num = num + 1
			mean = total / num
	print('Highest temperature ='+ str(maximum))
	print('Lowest temperature =' + str(minimum))
	print('Average temperature ='+str(mean))
	print('cold days: '+str(cold))








###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
