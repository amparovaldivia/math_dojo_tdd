import unittest
class MathDojo:
    def __init__(self):
        self.result = 0

    def adicion(self, num, *nums):
        self.result+=num
        for numero in nums:
            self.result+=numero
        return self
        
    
    def sustraccion(self, num, *nums):
        self.result-=num
        for numero in nums:
            self.result-=numero
        return self
md = MathDojo()

x = md.adicion(2).adicion(2,5,1).sustraccion(3,2).result
print(x)	

class Test(unittest.TestCase):
    def test(self):
        md=MathDojo()
        self.assertEqual(md.adicion(8,3,3).result,14)
    def test2(self):
        md=MathDojo()
        self.assertEqual(md.sustraccion(9,3,2).result,-14)

if __name__=='__main__':
    unittest.main()

