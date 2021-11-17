# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:24:55 2021

@author: javia
"""

import numpy as np
import pandas as pd #the host editor doesn't support pandas, but didn't matter because the data frame is not necessary

#I will  create a dataframe containing item code, price, number of items, discount type and discount

#I intentionally create more data structures than needed because I want to play with dictionaries and dataframes
class ShoppingBag:

    def calculate_bag_total(self, items, discounts):
        # Your code goes here
        df=pd.DataFrame(
                   columns=['code', 'price', 'quantity','type','discount']) #this creates the data frame with only column names
        #I can keep adding colums with df['column_name']=list or I can create a numpy array with the lists, compute the transpose, and introduce that as the first argument of the data frame
        code_price=dict([(l[0:3],float(l[3:6])) for l in items])
        repeated_codes=[l[0:3] for l in items]
        
        codes=list(code_price.keys()) #column code
        prices=list(code_price.values()) #colum price
        
        #df[['code','price']]=np.array([codes,prices]).transpose() This should work 
        
        df['code']=codes
        df['price']=prices
        
        quantities=[repeated_codes.count(x) for x in codes] #column quantity
        
        df['quantity']=quantities
        
        code_quantity=dict(zip(codes,quantities)) #unused
        
        #to find the discounts that apply to a given item, I first look for the discounts with its code, then of those I take the ones that have a number of items less or equal to the quantity, and from those I take the one with greatest discount
        
        types=[]  #column type, to be updated
        discount_column=[] #column discount, to be updated
        pay=[] #column pay with price after discount to be added
        discounts_codes=[(l[0:3],l[3:7]) for l in discounts]
        
        for code in codes:
            quantity=code_quantity[code]
            price=code_price[code] 
            
            all_discounts=[a[1] for a in discounts_codes if a[0]==code]
            discounts_quantity=[d for d in all_discounts if int(d[0])<=code_quantity[code]]
            #to know what discount is bigger we will have to take into account the price, because P discounts depend on the amount
            p_discounts=[float(d[-2:]) for d in discounts_quantity if d[1]=='P']
            c_discounts=[float(d[-2:]) for d in discounts_quantity if d[1]=='C']
            if p_discounts and c_discounts:
                max_p_value=max(p_discounts)
                max_p_index = p_discounts.index(max_c_value)
                max_p_discount=p_disconts[max_p_index]
                
                max_c_value=max(c_discounts)
                max_c_index = c_discounts.index(max_c_value)
                max_c_discount=c_disconts[max_c_index]
                
                p_discount_amount=max_p_discount*0.01*price
                
                minus=max(max_c_discount,p_discount_amount)*quantity
                payment=max(0,price*quantity-minus)
                if max(max_c_discount,p_discount_amount)==max_c_discount:
                    types.append('C')
                    discount_column.append(f'{minus}£')
                    pay.append(payment)
                else:
                    types.append('P')
                    discount_column.append(f'{minus*0.01*price}%')
                    pay.append(payment)
            elif c_discounts:
                max_c_value=max(c_discounts)
                max_c_index = c_discounts.index(max_c_value)
                max_c_discount=c_discounts[max_c_index]
                
                minus=max_c_discount*quantity
                payment=max(0,price*quantity-minus)
                types.append('C')
                discount_column.append(f'{minus}£')
                pay.append(payment)
            elif p_discounts:
                max_p_value=max(p_discounts)
                max_p_index = p_discounts.index(max_p_value)
                max_p_discount=p_discounts[max_p_index]
                
                minus=max_p_discount*0.01*price*quantity
                payment=max(0,price*quantity-minus)
                types.append('P')
                discount_column.append(f"{ minus }%")
                pay.append(payment)
            else:
                types.append(None)
                discount_column.append(f'{0}£')
                pay.append(price)
                
    
        df[['type','discount']]=np.array([types,discount_column]).transpose()
        df['pay']=pay
        print(df)
        return df['pay'].sum()
            
            
        