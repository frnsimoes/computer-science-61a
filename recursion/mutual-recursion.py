# The Luhn ALgorithm

"""
from the rightmost digit, which is the check digit, moving left,
double the value of every second digit; if product of this doubling
operation is greater than 9 (e.g., 7*2=14), then sum the digits of the 
products (e.g., 10: 1+0=1; 14:1+4=5)
"""