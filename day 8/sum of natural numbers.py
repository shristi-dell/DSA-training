#Find sum of N using recursion
def sum(n):
  if n==1:
    return 1
  else:
    return n+sum(n-1)
if __name__ == '__main__':
  n=6
  res=sum(n)
  print(res)