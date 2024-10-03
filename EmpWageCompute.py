""" 

    @Author: Likhitha S
    @Date: 02-10-2024 18:00
    @Last Modified by: Likhitha S
    @Last Modified time: 02-10-2024 18:00
    @Title:Write a Python program to Add Part time Employee & Wage - Assume Part time Hour is 8

"""


import random

def employee_earnings(wage_earns_parttime,working_hours):
    """
        
        Description: 
           This function is used to calculate the part time on daily wage according to specified duration.
        Parameters:
         wage_earns_parttime, working_hours is an parameters from came from main method.
        Return:
            It prints the calculated amount earned according to the data given . 
        
    """
    
    
    total_earnings=wage_earns_parttime*working_hours
    print(f"employee earning per day will be: {total_earnings} rupees")
  
    

def main():
    wage_earns_parttime=15
    working_hours=8
    employee_earnings(wage_earns_parttime,working_hours)

if __name__=="__main__":
    main()