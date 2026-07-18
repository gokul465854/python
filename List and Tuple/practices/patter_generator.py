# Build a Number Pattern Generator

def number_pattern(n):
  if not isinstance(n,int):
    return "Argument must be an integer value"
  if n < 1:
    return "Argument must be an integer greate than 0"
  
  pattern = ""
  for i in range(1,n+1):
    pattern += str(i) + " "

  return pattern

print(number_pattern(12))