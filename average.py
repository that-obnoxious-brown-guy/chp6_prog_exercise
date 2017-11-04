'''
Neil Mate | Chapter 6 Program 5
October 18, 2017
'''

def main():

	file = open('numbers.txt','r')
	total = 0
	counter = 0
	for data in file:
		data = float(data.rstrip('\n'))
		total += data
		counter += 1
	print('Average of the numbers:',format(average,'.2f'))
	file.close()
	
main()