#!/usr/bin/python3
"""
Main file for testing
"""


import sys


makeChange = __import__('0-making_change').makeChange

print(makeChange([3, 6, 9], 1278652))