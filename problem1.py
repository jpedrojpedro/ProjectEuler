#
# Function that sum multiples numbers in [0,999] which
# are multiples from 3 and 5
# The code is a little extense because I tried to do it
# gereric. It works for any multiple you want.
#

def isMultiple ( num, base ) :
  if num%base == 0 :
		return True
	else :
		return False

def sumElemList ( list ) :
	sum = 0
	for num in list :
		sum += num
	return sum

def getMultiples ( listNumber, listBase ) :
	multiples = []
	count = 0
	for n in listNumber :
		for b in listBase :
			if isMultiple ( n, b ) :
				multiples.append ( n )
				count += 1
		if count >= 1 : multiples.append ( n )
		count = 0
	return multiples

numbers = []
# attencion in range function!!! It works like [0,1000)
for i in range(0,1000) :
	numbers.append ( i )
bases = []
bases.append ( 3 )
bases.append ( 5 )
print sumElemList ( list( set( getMultiples ( numbers, bases ) ) ) )
