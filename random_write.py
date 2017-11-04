'''
Neil Mate | Chapter 6 Program 7
October 18, 2017
'''
import random

def main():

	user = int(input('Enter the number of randoms required: '))
	file = open('randoms.txt','w')
	counter = 0
	for x in range(user):
		data = random.randint(1,500)
		file.write(str(data)+'\n')
	file.close()
	print(user,'random numbers successfully added to randoms.txt')
	
main()