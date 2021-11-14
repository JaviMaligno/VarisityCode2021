from decimal import Decimal
from math import gcd
#this solution is only valid if we only consider lines going through the origin
class Solution:

    KEEP_PREVIOUS = 'KEEP_PREVIOUS'
    NUMBER_OF_POINTS = int(4)
    COLINEAR = 'colinear'

    def fix_fuel_config(self, config):
        # Your code goes here
        
        points=self.list_of_points(config)
        slopes = [points[i][1]/points[i][0] for i in range(self.NUMBER_OF_POINTS)]

        if self.check_x_coordinate(points):
            return self.KEEP_PREVIOUS
        else:
             return self.check_colinearity(points,slopes,config)
        
    
    def list_of_points(self,config:str)->list: #transform the configuration in a list of tuples, each tuple representing a point
        first_split=config.split(';')
        points=[(float(i.split(':')[0]),float(i.split(':')[1])) for i in first_split]
        return points

    def check_x_coordinate(self,points):
        return len(set([points[i][0] for i in range(self.NUMBER_OF_POINTS)]))<self.NUMBER_OF_POINTS

    def check_colinearity(self, points, slopes,config):
        number_of_slopes=len(set(slopes))
        if number_of_slopes>2:
            return self.KEEP_PREVIOUS
        elif number_of_slopes == 1:
            return config
        else:
            return self.three_colinear(points,slopes)

#we decide if the points are colinear by comparing the slopes, three points are colinear if the slopes of any 2 pairs of points are equal
    def three_colinear(self,points,slopes): 
        correct_point=points[0]
        correct_slope=slopes[0]
        if slopes[0]==slopes[1]:
            if slopes[0]==slopes[2]:
                incorrect_point=points[3]
                if self.finite_decimal(correct_point):
                    d=incorrect_point[0]*correct_slope
                    points[3]=(incorrect_point[0],d) #fixes the configuration 
                    return self.list_to_config(points)
                else:
                    return self.KEEP_PREVIOUS
            else: 
                incorrect_point=points[2]
                if self.finite_decimal(correct_point):
                    d=incorrect_point[0]*correct_slope
                    points[2]=(incorrect_point[0],d)
                    return self.list_to_config(points)
                else:
                    return self.KEEP_PREVIOUS
        elif slopes[0]==slopes[2]:
            incorrect_point=points[1]
            if self.finite_decimal(correct_point):
                    d=incorrect_point[0]*correct_slope
                    points[1]=(incorrect_point[0],d)
                    return self.list_to_config(points)
            else:
                    return self.KEEP_PREVIOUS
        else:
            incorrect_point=points[0]
            correct_point=points[1]
            correct_slope=slopes[1]
            if self.finite_decimal(correct_point):
                    d=incorrect_point[0]*correct_slope
                    points[1]=(incorrect_point[0],d)
                    return self.list_to_config(points)
            else:
                    return self.KEEP_PREVIOUS
        

    def list_to_config(self,points)->str:
        colon_points=list(map(lambda x: ':'.join(map(lambda y: "{:g}".format(y),x)),points))
        config= ';'.join(colon_points) 
        return config      


        

    def finite_decimal(self,correct_point)->bool:
        a="{:g}".format(correct_point[0]) #the format eliminates trailing zeroes
        b="{:g}".format(correct_point[1])
        d1=Decimal(a) #need to string it because otherwise Decimal does weird things
        power1=-d1.as_tuple().exponent #this equals the number of decimal points. The formatting was crucial here
        d2=Decimal(b)
        power2=-d2.as_tuple().exponent
        power=max(power1,power2)
        denominator=int(float(b)*10**power)
        numerator=int(float(a)*10**power)
        g=gcd(numerator,denominator)
        quotient=denominator//g
        bad_primes=self.prime_factors(quotient)-set((2,5))
        return not bad_primes
             #If the correct slope is given by b/a, I need to check whether b/a is terminating.
             #This is because if (c,d) is a wrong configuration, I need to replace d by b/a*c, so that d/c=b/a
             #To do that, take into account that the coorrect slope comes from a tuple (a,b) (not necessary the same a and b, but doesn't matter)
             #First, I would count the number of decimals of both a and b multiply to the greates power of 10 above and below. https://stackoverflow.com/questions/6189956/easy-way-of-finding-decimal-places
             #Then I would have to compute the reduced fraction, but it  is enough compute the reduced denominator, which can be computed by deving the denominator by the gcd(numerator,denominator)
             #Finally, the fraction is terminating if and only if the primer decomposition of the denominator has a number distinct of 2 or 5
             #I only need to use this function when fixing a configuration, because the given points will always be terminating

    def prime_factors(self,n): #returns the set of prime factors of n
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors