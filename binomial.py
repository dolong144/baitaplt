import math
print("nhập n:")
n = input()
print("nhập N:")
N = input()
N = int(N)
n = int(n)
print("nhập p:")
p = input()
p = float(p)
def prob(n, p, N):
  return math.factorial(N)/math.factorial(n)/math.factorial(N-n)*math.pow(p,n)*math.pow(1-p,N-n);
def sumProb(N,p):
  sum = 0.0
  for i in range(0,N):
    sum = sum + prob(i,p,N)
  return sum;
def infoMeasure(n,p,N):
  return -math.log2(prob(n,p,N))
def approxEntropy(N,p):
  H = 0.0
  for i in range(0,N):
    H = H + prob(i,p,N)*infoMeasure(i,p,N)
  return H
print("xác suất Pn:",prob(n,p,N))
print("lượng tin:", infoMeasure(n,p,N))
print("tổng xác suất:",sumProb(N,p))
print("H = ",approxEntropy(N,p))