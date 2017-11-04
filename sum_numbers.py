'''
Neil Mate | Chapter 6 Program 5
October 18, 2017
'''

def main():

	file = open('numbers.txt','r')
	total = 0
	for data in file:
		data = int(data.rstrip('\n'))
		total += data
	print('Total sum of the integers in numbers.txt : ',total)
	file.close()
	
main()