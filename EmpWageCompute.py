""" 

    @Author: Likhitha S
    @Date: 02-10-2024 18:00
    @Last Modified by: Likhitha S
    @Last Modified time: 02-10-2024 18:00
    @Title:Write a Python program to Add Part time Employee & Wage - Assume Part time Hour is 8

"""


import random

def employee_parttime_earnings():
    """
        
        Description: 
           This function is used to calculate the part time on daily wage according to specified duration.
        Parameters:
         wage_earns_parttime, working_hours is an parameters from came from main method.
        Return:
            It prints the calculated amount earned according to the data given . 
        
    """
    
    wage_earns_parttime=16
    working_hours=4 
     
    total_earnings=wage_earns_parttime*working_hours
    print(f"employee earning per day will be: {total_earnings} rupees")
    return total_earnings

