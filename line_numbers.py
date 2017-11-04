'''
Neil Mate | Chapter 6 Program 3
October 18, 2017
'''

def main():

	user = input('Enter the file name: ')
	file = open(user,'r')
	counter = 1
	for data in file:
		#Casting data to string incase the file has numerical values
		print(counter,': ',str(data.rstrip('\n')))
		counter += 1
	file.close()
	
main()