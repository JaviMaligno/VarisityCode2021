from decimal import Decimal
from math import gcd

class Solution:

    KEEP_PREVIOUS = 'KEEP_PREVIOUS'
    NUMBER_OF_POINTS = int(4)
    COLINEAR = 'colinear'

    def fix_fuel_config(self, config):
        # Your code goes here
        
        points=self.list_of_points(config)
        #slopes = [points[i][1]/points[i][0] for i in range(self.NUMBER_OF_POINTS)]
        
        

        if self.check_x_coordinate(points):
            return self.KEEP_PREVIOUS
        else:
             return self.check_colinearity(points,config)
        
    
    def list_of_points(self,config:str)->list: #transform the configuration in a list of tuples, each tuple representing a point
        first_split=config.split(';')
        points=[(float(i.split(':')[0]),float(i.split(':')[1])) for i in first_split]
        return points

    def check_x_coordinate(self,points):
        return len(set([points[i][0] for i in range(self.NUMBER_OF_POINTS)]))<self.NUMBER_OF_POINTS

    def check_colinearity(self,points,config):
        #three points are collinar if and only if the determinant of the 3 (in two rows) points and (1 1 1) (in the third row) is 0
        triplets_of_points=[[points[0],points[1],points[2]], 
                            [points[0],points[1],points[3]],
                            [points[0],points[2],points[3]],
                            [points[1],points[2],points[3]]]
                          

        if self.determinant(triplets_of_points[0])==0:
            if self.determinant(triplets_of_points[1])==0: #in this case all four are collinear
                return config
            else:
                return self.fix_config(triplets_of_points[0],points[3],points,3)
        elif self.determinant(triplets_of_points[1])==0:
             return self.fix_config(triplets_of_points[1],points[2],points,2)
        elif self.determinant(triplets_of_points[2])==0:
             return self.fix_config(triplets_of_points[2],points[1],points,1)
        elif self.determinant(triplets_of_points[3])==0:
             return self.fix_config(triplets_of_points[3],points[0],points,0)
        else:
            return self.KEEP_PREVIOUS



    def fix_config(self,three_points,fourth_point,points,position):
        #we computee the line y=mx+b
        p=three_points[0]
        q=three_points[1]
        vector= (q[0]-p[0],q[1]-p[1])
        slope=vector[1]/vector[0] #m
        independent=p[1]-slope*p[0] #b
        if self.finite_decimal(vector): #checking if the decimal representation of slope is finite
            new_point=(fourth_point[0],slope*fourth_point[0]+independent)
            points[position]=new_point
            return self.list_to_config(points)
        else:
            return self.KEEP_PREVIOUS

    def determinant(self,three_points):
        determinant = three_points[0][0] * (three_points[1][1] - three_points[2][1]) + three_points[1][0] * (three_points[2][1] - three_points[0][1]) + three_points[2][0] * (three_points[0][1] - three_points[1][1])
        return determinant


   
        

    def list_to_config(self,points)->str:
        colon_points=list(map(lambda x: ':'.join(map(lambda y: "{:g}".format(y),x)),points))
        config= ';'.join(colon_points) 
        return config      


        

    def finite_decimal(self,vector)->bool:
        #checkes if the slope of a vector has a finite decimal representation
        a="{:g}".format(vector[0]) #the format eliminates trailing zeroes
        b="{:g}".format(vector[1])
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