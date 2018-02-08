#!/usr/bin/env python
#-*- coding:utf8 -*-

"""
Create: 2018/2/8
@author: Jianhao
"""

def computerCost(x, y, theta)
	m = len(y)
	J = 0

	J = (np.transpose((x*theta-y)*(x*theta-y)))/2m
	return J
