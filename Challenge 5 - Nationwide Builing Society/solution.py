class Arti:

    def redact_card_details(self, message):
        # Your code goes here
        if self.match_amex(message):#probably first output is a truth value and then there is the output with positions, but I could make it so that it returns just false if there are no matches
            positions=self.match_amex(message)[1] 
            for p in positions:
                message=self.replace_ast(message,p,15) #will have to check that the positions returned by regex are what I want
            #depending on whether there can be several credit card numbers or not, I would just start another if or continue with elif
        if self.match_mastercard(message):
            positions=self.match_mastercard(message)[1]
            for p in positions:
                message=self.replace_ast(message,p,16)
        if self.match_visa(message):
            positions=self.match_visa(message)[1]
            for p in positions:
                message=self.replace_ast(message, p, 13)
                
        return message
    
    def match_amex(self,message):
        #match whether there is an AMEX card number and returns the position of the appearance
        #maybe I should try to match several appearances, so a while loop could be used, together with a list of positions to be passed to the last function
        pass
    
    def match_mastercard(self,message):
        pass
    
    def match_visa(self,message):
        pass
    
    def replace_ast(self,message, position,length):
        #given a message, it replaces the characters from position to position+length by asteriscs
        return message.replace(message[position:position+length+1],'*'*length)