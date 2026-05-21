#Find Power using Recursion
def power(x,y):
  if y==0:
    return 1
  else:
    return x*power(x,y-1)
if __name__ == '__main__':
  x=3
  y=2
  res=power(x,y)
  print(res)