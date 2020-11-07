#List of perfect #
#Parameters? 2-1000? Problem tasks? Organization?
#find factors using % and remainder = 0
#sum of factors
#compare sum to original number at the start (check if perfect)
#perfect numbers are 6, 28, 496

X = input()
X = int(X)
i = 1
count = 0

while i<X:
	if (X % i==0):
		count += i
	i +=1

if (count==X):
	print("perfect")
else:
	print("not perfect")