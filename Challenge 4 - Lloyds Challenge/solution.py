class Solution:

    def number_of_days_to_save(self, moneySaved):
        # Your code goes here
        if moneySaved<0 or moneySaved>74926:
            return -1
        elif moneySaved==0:
            return 0
        else:
            return self.number_of_days(moneySaved)
            
    
    def number_of_days(self,moneySaved):
        amount=0 #saved amount so far
        day=0 #current day, each day of the week is a residue modulo 7, starting from Monday
        pounds=1 #number of pounds she puts in the account
        monday_pounds=1 #number of pounds corresponding to monday
        while amount<moneySaved:
            amount+=pounds 
            day+=1
            pounds+=1 
            if day % 7 == 0:
                monday_pounds+=1
                pounds=monday_pounds
            else:
                pass
        return day 