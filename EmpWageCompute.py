""" 

    @Author: Likhitha S
    @Date: 02-10-2024 18:00
    @Last Modified by: Likhitha S
    @Last Modified time: 02-10-2024 18:00
    @Title:Write a Python program to Calculate Daily Employee Wage - Assume Wage per Hour is 20 - Assume Full Day Hour is 8

"""


import random

def employee_earnings():
    """
        
        Description: 
           This function is used to calculate the daily wage according to an hour.
        Parameters:
         wage_earnsper_hour, working_hours is an parameters from came from main method.
        Return:
            It prints the calculated amount earned according to the data given . 
        
    """
    
    wage_earnsper_hour=20
    working_hours=8
    
    total_earnings=wage_earnsper_hour*working_hours
    print(f"employee earning per day will be: {total_earnings} rupees")
  
    

