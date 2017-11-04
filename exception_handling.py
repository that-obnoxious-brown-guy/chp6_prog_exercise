'''
Neil Mate | Chapter 6 Program 9
October 24, 2017
'''

def main():
	try:
		
		file = open('numbers.txt','r')
		total = 0
		count = 0
		
		for data in file:
			data = float(data.rstrip('\n'))
			total += data
			count += 1
		
		print('Average of the numbers:',format(total/count,'.2f'))
		file.close()

	except ValueError:
		print('Non-Numeric data found in the file.')
	
	except IOError:
		print('Error occured while trying to read the file.') 

main()