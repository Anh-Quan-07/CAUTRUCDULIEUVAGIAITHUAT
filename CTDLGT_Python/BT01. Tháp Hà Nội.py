# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 20:53:51 2021

@author: quann
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# BT01. Tháp Hà Nội
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)

n = int(input('Nhap so dia: '))
TowerOfHanoi(n, 'A', 'C', 'B')