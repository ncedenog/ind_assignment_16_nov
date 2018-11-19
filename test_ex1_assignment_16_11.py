#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:25:57 2018

@author: nataliecedeno
"""

#%%
from ex1_assignment_16_11 import checkout
def test_shoppingcart():
    values = []
    
    for item in values:
        assert checkout(item) == None

def test_shoppingcart1():
    values = [["Guitar"]]
    
    for item in values:
        assert checkout(item) == 1000

def test_shoppingcart2():
    values = [["Guitar", "Guitar_string"]]
    
    for item in values:
        assert checkout(item) == 1010
#%%