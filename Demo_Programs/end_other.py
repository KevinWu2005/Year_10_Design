def end_other(a, b):
  a = a.lower() #formatting input
  b = b.lower() #formatting input
  #For example, (AbC, HiaBc) should evaluate to true, but when python compares 
  #these two strings, it will evalute to false because it it case sensitive
  #making both strings to lower case will eliminate this issue
  
  if a.endswith(b): #directly checks if string a ends with string b
    return True
  elif b.endswith(a): #directly checks if string b ends with string a
    return True
  else: # if both a does not end with b, and b does not end with a, return False
    return False