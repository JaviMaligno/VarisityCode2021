import re
from operator import itemgetter

class Arti:

    def redact_card_details(self, message):
        # Your code goes here
        list_of_cards=[]
        amex=self.match_amex(message)
        amex_message=amex[0]
        amex_cards=amex[1]
        if amex[1]:#probably first output is a truth value and then there is the output with positions, but I could make it so that it returns just false if there are no matches
            message=amex_message
            list_of_cards+=amex_cards
            
        mastercard=self.match_mastercard(message)
        mastercard_message=mastercard[0]
        mastercard_cards=mastercard[1]
        if mastercard[1]:
            message=mastercard_message
            list_of_cards+=mastercard_cards
            
            
        visa=self.match_visa(message)
        visa_message=visa[0]
        visa_cards=visa[1]
        
        if visa[1]:
            message=visa_message
            list_of_cards+=visa_cards
            
        if list_of_cards:
            cards_in_order=sorted(list_of_cards,key=itemgetter(0))
            sorted_cards=[c[1] for c in cards_in_order]
            return sorted_cards+[message]
        else:
            return ['NONE',message]
        
    
    def match_amex(self,message):
        #match whether there is an AMEX card number and returns the position of the appearance
        #maybe I should try to match several appearances, so a while loop could be used, together with a list of positions to be passed to the last function
        amex_pattern='34\d{13}|37\d{13}'
        p=list(re.finditer(amex_pattern, message))
        starts=[match.span()[0] for match in p]
        ends=[match.span()[1] for match in p]
        amex_cards=[(start,'AMEX') for start in starts]
        for (start,end) in zip(starts,ends):
            message=self.replace_ast(message, start, end)
        return message,amex_cards
    
    def match_mastercard(self,message):
        mastercard_pattern='51\d{14}|52\d{14}|53\d{14}|54\d{14}|55\d{14}'
        p=list(re.finditer(mastercard_pattern, message))
        starts=[match.span()[0] for match in p]
        ends=[match.span()[1] for match in p]
        mastercard_cards=[(start,'MASTERCARD') for start in starts]
        for (start,end) in zip(starts,ends):
            message=self.replace_ast(message, start, end)
        return message,mastercard_cards
    
    def match_visa(self,message):
        visa_pattern='4\d{12}'
        p=list(re.finditer(visa_pattern, message))
        starts=[match.span()[0] for match in p]
        ends=[match.span()[1] for match in p]
        visa_cards=[(start,'VISA') for start in starts]
        for (start,end) in zip(starts,ends):
            message=self.replace_ast(message, start, end)
        return message,visa_cards
        
        
    
    #def match_visa(self,message):
     #   visa_pattern='4\d{12}'
      #  p=re.search(visa_pattern,message)
       # visa_cards=[]
        #while p:
         #   start=p.span()[0]
          #  end=p.span()[1]
           # message=self.replace_ast(message,start,end)
            #visa_cards+=(start,'VISA') #doing this I will not be able to put the cards in order, I need to compare the appearances to sort the apearances, maybe create a sorted dictionary of the form {'CARD':'start'} https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
            #p=re.search(visa_pattern,message)
        #return message,visa_cards
    
    #save all the starts together with the card (maybe a list of tuples to create a dictionary later), in the join all of them and sort it. After this, create a list with the card names in order and append it to the result if it is not empty, and append NONE otherwise
            
    
    def replace_ast(self,message, start,end):
        #given a message, it replaces the characters from position to position+length by asteriscs
        return message.replace(message[start:end],'*'*(end-start),1)