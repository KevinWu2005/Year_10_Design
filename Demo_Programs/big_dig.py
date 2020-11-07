def big_diff(nums):
  minVal = 1000000 #min value, will be changed to the lowest number in loop
  maxVal = -1000000 #max value, will be changed to largerst number in loop
  #I learned coding with Java, so normally I would use Integer.MAX_VALUE 
  #and Integer.MIN_VALUE, but I could not find the python counterpart
  
  for i in range(0,len(nums),1): #standard loop, goes through all terms in big_diff
    minVal = min(nums[i],minVal) #compares if nums[i] or minVal is smaller
    maxVal = max(nums[i],maxVal) #compares if nums[i] or maxVal is larger
  
  return maxVal-minVal #final output
