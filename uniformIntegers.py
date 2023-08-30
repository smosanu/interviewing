def isUniform(num):
  if num < 10: # if single digit -> is uniform
    return True
  numStr = str(num) # convert to string
  tmp = numStr[0] # tmp stores previous digit
  for c in numStr:
    if (c != tmp): # first cycle redundant
      return False
    tmp = c # update tmp
  return True # ran out with digits matching

def getDigitCount(num):
  return len(str(num)) # convert to string, then get length

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  if (A==B):
    if isUniform(A):
      return 1
    else:
      return 0

  if(A>B):
    return 0
  
  count = 0
  if isUniform(A):
    count+=1
  if isUniform(B):
    count+=1
  
  Adigits = getDigitCount(A)
  Bdigits = getDigitCount(B)
  digitDifference = Bdigits-Adigits
  if digitDifference > 1: # easy to get uniform numbers perfectly in between
    count+= (digitDifference-1)*9

  Adigit0 = int(str(A)[0])
  Bdigit0 = int(str(B)[0])
  if Bdigits > Adigits:
    count+= 9-Adigit0
    count+= Bdigit0-1
  else:
    count+= Bdigit0-Adigit0-1

  if A < int(str(Adigit0)*Adigits):
    count+=1
  if B > int(str(Bdigit0)*Bdigits):
    count+=1

  return count

if __name__ == "__main__":
    A = 1
    B = 9

    print(getUniformIntegerCountInInterval(A, B))