#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:23:46 2018

@author: nataliecedeno
"""

#%%
#Exercise 1
shopping_list = {"Guitar":1000,
               "Pick_box":5,
               "Guitar_string":10
               
               }
shopping_cart = ["Guitar", "Guitar_string" ]

def checkout(shopping_cart):
    
    final_price=0
    
    if shopping_cart == []:
        return None
    else:
        for item in shopping_cart:
            final_price = final_price +(shopping_list [item])
    return final_price
    
checkout (shopping_cart)
#%%