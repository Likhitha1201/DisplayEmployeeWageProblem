""" 

    @Author: Likhitha S
    @Date: 03-10-2024 12:00
    @Last Modified by: Likhitha S
    @Last Modified time: 03-10-2024 12:00
    @Title:Write a Python program to Calculate Wages till a condition of total working hours or days is reached for a month - Assume 100 hours and 20 days

"""


def employee_hour_earnings(no_of_hours,per_hour_wage):
    """
        
        Description: 
           This function is used to calculate the wages according to hours and days.
        Parameters:
         no_of_hours,per_hour_wage is an parameters from came from main method.
        Return:
            It prints the calculated amount earned according to the data given . 
        
    """
    
    
    total_hour_earnings=no_of_hours*per_hour_wage
    print(f"employee earning for {no_of_hours} hours will be: {total_hour_earnings} rupees")
    
    
def employee_day_earnings(no_of_days,per_day_wage):
    """
        
        Description: 
           This function is used to calculate the wages according to hours and days.
        Parameters:
           no_of_days,per_day_wage is an parameters came from main method.
        Return:
            It prints the calculated amount earned according to the data given . 
        
    """
    
    
    total_earnings= no_of_days*per_day_wage
    print(f"employee earning for {no_of_days} days will be: {total_earnings} rupees")
    

def main():
    
    no_of_days=20
    no_of_hours=100
    per_hour_wage=20
    per_day_wage=160
    
    employee_hour_earnings(no_of_hours,per_hour_wage)
    employee_day_earnings(no_of_days,per_day_wage)
    
if __name__=="__main__":
    main()
