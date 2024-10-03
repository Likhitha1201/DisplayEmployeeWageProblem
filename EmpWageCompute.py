""" 

    @Author: Likhitha S
    @Date: 02-10-2024 18:00
    @Last Modified by: Likhitha S
    @Last Modified time: 02-10-2024 18:00
    @Title:Write a Python program to Calculating Wages for a Month - Assume 20 Working Day per Month.

"""


def employee_Monthly_earnings(full_earn,no_of_days):
    """
        
        Description: 
           This function is used to calculate the employee monthly earnings.
        Parameters:
          full_earn,no_of_days is a parameter passed from method call.
        Return:
            It prints the output according to the calculation . 
        
    """
    
    
    monthly_earning=full_earn*no_of_days
    print(f"{monthly_earning} rupees")
    return monthly_earning