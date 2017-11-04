'''
Neil Mate | Chapter 6 Program 11
October 18, 2017
'''

def main():

	name = input('Enter Name: ')
	desc = input('Describe yourself: ')
	htmlfile = open('file.html','w')
	code = '<html>'+'\n'+'<head>'+'\n'+'</head>'+'\n'+'<body>'+'\n'+'\t'+'<center>'+'\t\t'+'<h1>'+name+'<h1>'+'\n\t</center>\n\t<hr />\n\t'+desc+'\n\t<hr />\n</body>\n</html>'
	htmlfile.write(code)
	htmlfile.close()

main()