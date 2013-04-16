#
# Function that sum the even-valued terms in fibonacci
# whose value does not exceed 4 million
#

def recursiveFibo ( elem ) :
	if elem == 0 :
		return 0
	elif elem == 1 :
		return 1
	elif elem == 2 :
		return 2
	else :
		return ( recursiveFibo ( elem - 1 ) + recursiveFibo ( elem - 2 ) )

num, sum = 0, 0

while True :
	ret = recursiveFibo ( num )
	if ret < 4000000 :
		if ret % 2 == 0 : sum += ret
	else :
		break
	num += 1
print sum
