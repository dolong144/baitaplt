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
def prob(n,p):
  result = pow(1-p,n-1) * p
  return result;
def infoMeasure(n,p):
  return -math.log2(prob(n,p))
def sumProb(N,p):
  #khi N càng lớn ta sẽ dần tính tổng được hết các trường hợp trong bài toán tung đồng xu đến khi có mặt ngửa. Công càng nhiều thì tổng càng dần tới 1
  sum = 0.0
  for i in range(1,N):
    sum = sum + p * pow(1-p,i-1)
  return sum
def approxEntropy(N,p):
  H = 0.0
  for i in range(1,N):
    H = H + prob(i,p) * infoMeasure(i,p)
  return H
print("xác suất Pn:",prob(n,p))
print("lượng tin:", infoMeasure(n,p))
print("tổng xác suất:",sumProb(N,p))
print("H = ",approxEntropy(N,p))
