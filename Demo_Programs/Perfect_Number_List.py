#List of perfect #
#Parameters? 2-1000? Problem tasks? Organization?
#find factors using % and remainder = 0
#sum of factors
#compare sum to original number at the start (check if perfect)
#perfect numbers are 6, 28, 496



def findFactors(num):
	factorList=[]
	for i in range(1,x+1):
		if x%i==0:
			factorList.append(i)

	return factorList

def sumFactors(list):
	sum = 0
	for i in range(0,factorList.length()):
		sum += factorList[i]

	return sum

def printPerfectNumber(num,sum):
	result = False
	if num==sum:
		result = True

	return result


list = findFactors(6)
sum = sumFactors(list)
printPerfectNumber(6,sum)
if isPerfectNumber(6,sum):
	print(6)





