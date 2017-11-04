def main():

	file = open('steps.txt','r')

	jan=31
	feb=28
	mar=31
	apr=30
	may=31
	jun=30
	jul=31
	aug=31
	sep=30
	ocb=31
	nov=30
	dec=31

	counter = 0
	total = 0
	data = file.readline()

	while data != '':

		data = int(data.rstrip('\n'))
		counter += 1
		total = total + data

		if counter == jan:
			print('January Steps:',total/jan)
			total = 0

		elif counter == (jan+feb):
			print('February Steps:',total/feb)
			total = 0

		elif counter == (jan+feb+mar):
			print('February Steps:',total/mar)
			total = 0

		elif counter == (jan+feb+mar+apr):
			print('April Steps:',total/apr)
			total = 0

		elif counter == (jan+feb+mar+apr+may):
			print('May Steps:',total/may)
			total = 0

		elif counter == (jan+feb+mar+apr+may+jun):
			print('June Steps:',total/jun)
			total = 0

		elif counter == (jan+feb+mar+apr+may+jun+jul):
			print('July Steps:',total/jul)
			total = 0

		elif counter == (jan+feb+mar+apr+may+jun+jul+aug):
			print('August Steps:',total/aug)
			total = 0

		elif counter == (jan+feb+mar+apr+may+jun+jul+aug+sep):
			print('September Steps:',total/sep)
			total = 0

		elif counter == (jan+feb+mar+apr+may+jun+jul+aug+sep+ocb):
			print('October Steps:',total/ocb)
			total = 0

		elif counter == (jan+feb+mar+apr+may+jun+jul+aug+sep+ocb+nov):
			print('November Steps:',total/nov)
			total = 0

		elif counter == (jan+feb+mar+apr+may+jun+jul+aug+sep+ocb+nov+dec):
			print('December Steps:',total/dec)
			total = 0

		data = file.readline()

	file.close()

main()