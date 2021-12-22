import re
import numpy as np
#import pandas as pd
from itertools import groupby
from operator import itemgetter


class Warehouse:
   
  

    def store_items(self, axis, storageInstructions, getItem):
        # Your code goes here
        if self.invalid_axis(axis):
            return ''
        axis_list=sorted(list(set(axis))) #I think sorting the axis will make it easier to give the position, but I will see
        #coordinates=len(axis_list)
        #origin=np.array((0,)*coordinates)
        items=[]
        positions=[]
        amounts=[]
        #movements=[]
        #item_dict=dict(zip(items,zip(amounts,positions)))
        item_position=dict(zip(items,positions))
        #position_dict=dict(zip(positions,items))
        item_amount=dict(zip(items,amounts))
        #|-\d{1,}[A-Za-z]{1,}
        for instruction in storageInstructions:
            if re.match('\d|-\d',instruction) and ':' in instruction: #This one eliminates
                manifest=instruction.split(':')
                multiple_items=re.findall('\d{1,}[A-Za-z]{1,}|-\d{1,}[A-Za-z]{1,}', manifest[0]) #we detect if an amount is negative to remove the item
                ordered_pairs=self.items_amounts(multiple_items) #list of [item,amount]
                new_pairs=self.remove_stored(ordered_pairs,items,item_amount) #remove items  that are already stored updating the amount
                multiple_movements=re.findall('[A-Za-z]{1,}\d{1,}|[A-Za-z]{1,}-\d{1,}', manifest[1])
                ordered_mov=self.items_movements(multiple_movements) #list of [axis,movement]
                new_mov=self.remove_axis(ordered_mov,axis_list) #remove axis that are not in the axis list
                for i in new_pairs:
                    items.append(i[0]) #update item list with new items
                    
                position=self.create_position(new_mov,axis_list)  #ATTENTION position should have 0 on the axis not involved in the instruction or I should also include  the axis label in position
                item_position.update(dict((i[0],position) for i in new_pairs)) #update the item_position with the position of the new items
                item_amount.update(dict(a for  a in new_pairs)) #update item_amount with new item:amount
                #return item_amount, item_position #I wrote this to test the dictionaries, they're working nicely
      
            elif re.match('[A-Za-z]',instruction) and ':' in instruction:
                manifest=instruction.split(':')
                access_instruction=re.findall('[A-Za-z]{1,}\d{1,}|[A-Za-z]{1,}-\d{1,}', manifest[0]) #coordinates to find items
                ordered_access=self.items_movements(access_instruction) #list of [axis,coordinate]
                existent_access=self.remove_axis(ordered_access,axis_list) #remove axis that are not in the axis list
                search_position=self.create_position(existent_access,axis_list)
                self.update_position(search_position, item_position, axis_list, manifest[1])
                #if any(np.array_equal(search_position,j) for j in item_position.values()):     #if there are no items in the position I won't look at  it #Arrays behave weirdly with booleans
                 #   move_instruction=re.findall('[A-Za-z]{1,}\d{1,}|[A-Za-z]{1,}-\d{1,}', manifest[1]) #movement instruction
                 #   ordered_instruction=self.items_movements(move_instruction)#list of [axis,movement]
                  #  new_move=self.remove_axis(ordered_instruction,axis_list) #remove axis that are not in the axis list
                   # movement=self.create_position(new_move,axis_list)
                    #find items on the given search_position
                    #items_to_move=self.find_keys(item_position,search_position) #items  on the given position
                    #for i in items_to_move:
                     #   item_position.update({i:item_position[i]+movement})
                        
            #recall that the output is ordered first by ascending amount and then by alphabetic order, so I have to reverse order by second element of the pairs [item,amount]
        coordinates=re.findall('[A-Za-z]{1,}\d{1,}|[A-Za-z]{1,}-\d{1,}', getItem)
        ordered_coordinates=self.items_movements(coordinates)
        existent_coordinates=self.remove_axis(ordered_coordinates,axis_list)
        get_position=self.create_position(existent_coordinates,axis_list)
        if any(np.array_equal(get_position,j) for j in item_position.values()):     #if there are no items in the position I won't look at  it #Arrays behave weirdly with booleans
                    #find items on the given get_position
            items_to_get=self.find_keys(item_position,get_position)
            itemamount=[]
            for i in items_to_get:
                itemamount.append([i,item_amount[i]])
            sorted_items=sorted(itemamount,key=(itemgetter(1,0)))
            answer=''
            for i  in sorted_items:
                answer+=str(i[1])+i[0]                
            
            return answer 
        else:
            return ''
                
    def invalid_axis(self,axis):
        return not all(x.isalpha() for x in axis)
    
    def items_amounts(self,multiple_items):
        pairs=[]
        ordered_pairs=[]
        for item in multiple_items:
            search=re.search('\d{1,}',item)
            start=search.span()[1]
            amount=int(item[:start])
            identifier=item[start:]
            pair_ia=(identifier,amount) #it is a list because I want to be able to modify the amount
            pairs.append(pair_ia)
        pairs.sort(key=itemgetter(0))
        for i,a in groupby(pairs, key=itemgetter(0)):
            ordered_pairs.append([i,sum(v[1] for v in a)])
        return ordered_pairs
            #still not sure what to do with this, I don't want to group everything at the  end, because it will depend on the instructions
            
            
            #do a version with pandas groupby(identifier).sum()
        #df=pd.DataFrame(columns=['Item','Amount'])
        #df['Item']=self.items
        #df['Amount']=self.amounts
        #df=df.groupby(by=['Item']).sum()
        
        # df1=pd.DataFrame([['B',3]], columns=['Item','Amount'])
        #df.append(df1,ignore_index=True)
            
    def items_movements(self,multiple_movements):
        pairs=[]
        ordered_pairs=[]
        for movement in multiple_movements:
            search=re.search('\d{1,}|-\d{1,}',movement)
            start=search.span()[0]
            axis=movement[:start]
            direction=int(movement[start:])
            pair_ia=(axis,direction) #it is a list because I want to be able to modify the amount
            pairs.append(pair_ia)
        pairs.sort(key=itemgetter(0))
        for i,a in groupby(pairs, key=itemgetter(0)):
            ordered_pairs.append([i,sum(v[1] for v in a)])
        return ordered_pairs
            
    def remove_stored(self,candidates,stored,item_amount):
        for a in candidates:
            if a[0] in stored:
                if a[1]>0:
                    item_amount.update({a[0]:item_amount[a[0]]+a[1]})
                candidates.remove(a)
            elif a[1]<=0: #if the amount is not positive
                candidates.remove(a) 
        return candidates
    
    def remove_axis(self,candidates,axis):
        for a in candidates:
            if a[0] not in axis:
                candidates.remove(a)
        return candidates
    
    
    def create_position(self,new_mov,axis_list):
        position=[]
        axis_dict=dict(new_mov)
        included_axis=[m[0] for m in new_mov]
        for x in axis_list:
            if x in included_axis:
                position.append(axis_dict[x])
            else:
                position.append(0)
        return np.array(position)
    
    
    
    def find_keys(self,item_position,search_position):
        values=list(item_position.values())
        searchval=search_position
        indices = [i for i, x in enumerate(values) if np.array_equal(x,searchval) ]
        keys=list(item_position.keys()) 
        wanted_keys=[keys[i] for i in indices]
        return wanted_keys
    
    def update_position(self,search_position,item_position,axis_list,manifest1):
        if any(np.array_equal(search_position,j) for j in item_position.values()):     #if there are no items in the position I won't look at  it #Arrays behave weirdly with booleans
                    move_instruction=re.findall('[A-Za-z]{1,}\d{1,}|[A-Za-z]{1,}-\d{1,}', manifest1) #movement instruction
                    ordered_instruction=self.items_movements(move_instruction)#list of [axis,movement]
                    new_move=self.remove_axis(ordered_instruction,axis_list) #remove axis that are not in the axis list
                    movement=self.create_position(new_move,axis_list)
                    #find items on the given search_position
                    items_to_move=self.find_keys(item_position,search_position) #items  on the given position
                    for i in items_to_move:
                        item_position.update({i:item_position[i]+movement})