'''
Neil Mate | Chapter 6 Program 2
October 18, 2017
'''

def main():

	user = input('Enter the file name: ')
	file = open(user,'r')
	counter = 0
	for data in file:
		if counter < 5:
			print(data.rstrip('\n'))
			counter += 1
	file.close()
	
main()