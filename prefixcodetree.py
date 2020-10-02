class PrefixCodeTree:
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.value = str(data)   
    def insert(self, codeword, symbol):
        for i in range (0, len(codeword)-1):
            if codeword[i] == '0':
                if self.left == None:
                    self.left = PrefixCodeTree()
                self = self.left
            else:
                if self.right == None:
                    self.right = PrefixCodeTree()
                self = self.right
        if codeword[len(codeword)-1] == '0':
            self.left = PrefixCodeTree(symbol)
        else:
            self.right = PrefixCodeTree(symbol)
    def decode(self, encodedData, datalen):
      n = 0
      root = self
      res = ''
      for i in encodedData:
            if i == '0':
                root = root.left
            else:
                root = root.right
            if root.left == None and root.right == None:
                res += root.value
                root = self
                datalen -= 1
            if datalen == 0:
              return res
      return "encodedData thiếu"
'''
test = PrefixCodeTree()
test.insert("00",'a')
test.insert("01",'b')
test.insert("10",'c')
test.insert("111111",'d')
print(test.decode("000110111111",4))
print(test.left.left.value)
print(test.left.right.value)
print(test.right.left.value)'''
