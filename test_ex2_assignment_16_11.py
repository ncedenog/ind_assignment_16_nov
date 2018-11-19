#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:35:30 2018

@author: nataliecedeno
"""

#%%
from ex2_assignment_16_11 import checkout_2
def test_shoppingcart():
    values = []
    
    for item in values:
        assert checkout_2(item) == None

def test_shoppingcart1():
    values = [["Guitar", "Insurance"]]
    
    for item in values:
        assert checkout_2(item) == 1005

def test_shoppingcart2():
    values = [["Guitar", "Insurance", "Insurance", "Priority mail", "Priority mail"]]
    
    for item in values:
        assert checkout_2(item) == 1015
#%%
