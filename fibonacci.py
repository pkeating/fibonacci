from sys import exit

# gets first number from the user and ensures it is valid
while True:
	n1 = raw_input('First number >> ')
	if int(n1) == float(n1) and int(n1) >= 0:
		n1 = int(n1)		
		break
	print 'Please enter an integer greater than or equal to zero.'

# gets second number from the user and ensures it is valid
while True:
	n2 = raw_input('Second number >> ')
	if int(n2) == float(n2) and int(n2) > 0:
		n2 = int(n2)
		break
	print 'Please enter an integer greater than zero.'

# gets the stopping point from the user
while True:
	stp_pnt = raw_input('How many Fibonacci numbers? >> ')
	if int(stp_pnt) == float(stp_pnt) and int(stp_pnt) > 0:
		stp_pnt = int(stp_pnt)
		break
	print 'Please enter an integer greater than zero.'

# opens the output file
output_file = open('output.txt', 'w')

print 'Running...'
# writes headers
output_file.write('Row Number, Fibonacci Number, Golden Ratio\n')
# writes first row of data
output_file.write('1, %d, Undef\n' % n1)

# exits the program if the stopping point is 1
if stp_pnt == 1:
	output_file.close()
	exit(0)

# writes the second row of data and ensures there is no division by zero
if n1 == 0:
	output_file.write('2, %d, Undef\n' % n2)
else:
	output_file.write('2, %d, %s\n' % (n2, float(n2) / float(n1)))

# exits the program if the stopping point is two
if stp_pnt == 2:
	output_file.close()
	exit(0)

# calculates remaining fibonacci numbers and golden ratio estimates
# and writes them to the output file
for i in range(2, stp_pnt):
	n1, n2 = n2, n1 + n2
	output_file.write('%d, %d, %s\n' % (i+1, n2, float(n2) / float(n1)))

# closes the output file
output_file.close()
print 'Done!'
