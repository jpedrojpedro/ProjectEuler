#
# Find the largest prime factor of any number
#
#

def findLargestPrime ( numero ) :
    div, num, primes = 1, numero, []
	while num <> 1 :
		if num % div == 0 :
			primes.append ( div )
			num = ( num / div )
			div = 1
		div += 1
	primes.sort()
	return primes[-1]

print findLargestPrime ( 600851475143 )
