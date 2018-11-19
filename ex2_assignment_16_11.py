#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:57:46 2018

@author: nataliecedeno
"""

#%% 
#Exercise 2
    
product_list = {
        "Guitar": 1000, 
        "Pick box": 5, 
        "Guitar string": 10, 
        "Insurance": 5, 
        "Priority mail": 10
        }   


shopping_cart = ["Guitar", "Insurance", "Insurance", "Priority mail", "Priority mail"]

def checkout_2(shopping_cart): 
    
    final_price = 0 
    
    indexes_insurance = [i for i, x in enumerate(shopping_cart) if x == "Insurance"]
    
    
    
    indexes_priority = [b for b, y in enumerate(shopping_cart) if y == "Priority mail"]
    
    if len(indexes_insurance) > 0: 
        final_price += (product_list["Insurance"])
        
    
       
    if len(indexes_priority) > 0: 
        final_price += (product_list["Priority mail"])     
        
        
    
    if shopping_cart == []:
        return None
    
    else:
        
        for item in shopping_cart: 
            if item == "Insurance":
                continue
            
            elif item == "Priority mail": 
                continue
            
            else: 
                final_price += (product_list[item])
            
        
    return final_price
#%%