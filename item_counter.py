'''
Neil Mate | Chapter 6 Program 4
October 18, 2017
'''

def main():

	user = input('Enter the file name: ')
	file = open(user,'r')
	counter = 0
	for data in file:
		counter += 1
	print(counter,'names stored in',user)
	file.close()
	
main()