import cProfile

class QuadraticPrimes:

    def __init__(self):
        self.prime_list = self.listPrimes(1000)

    def listPrimes(self,n):
        prime_list = []
        for i in range(2,n):
            for prime in prime_list:
                if i%prime == 0:
                    break
            else:
                prime_list.append(i)

        return prime_list

    def isPrime(self,x):
        if x<0:
            return False
        for prime in filter(lambda prime: prime<x,self.prime_list):
            if x%prime == 0:
                return False
        return True

    def checkQuadratic(self,a,b):
        x = 0
        while self.isPrime(x**2+a*x+b):
            x += 1
        return x

    def findPrimes(self):
        best_pair = (0,0,0)
        for a in range(-999,1000):
            for b in qp.prime_list:
                highest_prime = qp.checkQuadratic(a,b)
                if highest_prime > best_pair[2]:
                    best_pair = (a,b,highest_prime)
     
        print best_pair[0]*best_pair[1]


if __name__ == "__main__":

    qp = QuadraticPrimes()
    qp.findPrimes()
    
