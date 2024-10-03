""" 

    @Author: Likhitha S
    @Date: 02-10-2024 18:00
    @Last Modified by: Likhitha S
    @Last Modified time: 02-10-2024 18:00
    @Title:Write a Python program to check employee attendence using random.

"""


import random

def check_attendance(attend):
    """
        
        Description: 
           This function is used to check employee attendence.
        Parameters:
          fun_name is used to an input from the user of type function.
        Return:
            It prints the output according to that fun_type . 
        
    """
    
    attend = random.random(0,1)
    
    if attend==1:
        print(attend," ->Employee is Present!!")
    else:
        print(attend," ->Employee is Absent!!") 
    
