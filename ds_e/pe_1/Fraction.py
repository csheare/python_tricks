
class Fraction:

    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __eq__(self,other):
        firstnum = self.numerator * other.denominator
        secondnum = self.denominator * other.numerator
        return firstnum == secondnum

    def __lt__(self,other):
        return self.numerator*other.denominator < self.denominator*other.numerator

    def __le__(self,other):
        return self.numerator*other.denominator <= self.denominator*other.numerator

    def __gt__(self,other):
        return self.numerator*other.denominator > self.denominator*other.numerator

    def __ge__(self,other):
        return self.numerator*other.denominator >= self.denominator*other.numerator

    def __ne__(self,other):
        return self.numerator*other.denominator != self.denominator*other.numerator

    def __add__(self, other):
        new_num = self.numerator*other.denominator + other.numerator*self.denominator
        new_denom = self.denominator * other.denominator
        common = gcd(new_num,new_denom)
        return Fraction(new_num//common,new_denom//common)

    def __sub__(self,other):
        new_num = self.numerator*other.denominator - other.numerator*self.denominator
        new_denom = self.denominator * other.denominator
        common = gcd(new_num,new_denom)
        return Fraction(new_num//common,new_denom//common)
    
    def __mul__(self,other):
        new_num = self.numerator*other.denominator 
        new_denom = self.denominator * other.denominator
        common = gcd(new_num,new_denom)
        return Fraction(new_num//common,new_denom//common)

    def __truediv__(self,other):
        new_num = self.numerator*other.denominator
        new_denom = self.denominator * other.numerator
        common = gcd(new_num,new_denom)
        return Fraction(new_num//common,new_denom//common)


    # Euclid's Algorithm
    def gcd(m,n):
        while n % m != 0:
            # you want to keep setting n to be the remainder of m % n
            oldn = n
            oldm = m

            m = oldn
            n = oldn % oldm
        return n


    def getNum(self):
        return self.numerator

    def getDen(self):
        return self.denominator

