import math
print("nhập n:")
n = input()
print("nhập N:")
N = input()
N = int(N)
n = int(n)
print("nhập r:")
r = input()
r = int(r)
print("nhập p:")
p = input()
p = float(p)
def prob(n, p, r):
  return math.factorial(n-1)/math.factorial(n-r)/math.factorial(r-1)*math.pow(p,r)*math.pow(1-p,n-r);
def sumProb(N,p,r):
  sum = 0.0
  for i in range(r,N):
    sum = sum + prob(i,p,r)
  return sum;
def infoMeasure(n,p,r):
  return -math.log2(prob(n,p,r))
def approxEntropy(N,p,r):
  H = 0.0
  for i in range(r,N):
    H = H + prob(i,p,r)*infoMeasure(i,p,r)
  return H
print("xác suất Pn:",prob(n,p,r))
print("lượng tin:", infoMeasure(n,p,r))
print("tổng xác suất:",sumProb(N,p,r))
print("H = ",approxEntropy(N,p,r))