""" 

    @Author: Likhitha S
    @Date: 02-10-2024 18:00
    @Last Modified by: Likhitha S
    @Last Modified time: 02-10-2024 18:00
    @Title:Write a Python program to check employee attendence using random.

"""


from EmpWageCompute import check_attendance
from EmpWageCompute import employee_Daily_earnings
from EmpWageCompute import employee_parttime_earnings
from EmpWageCompute import employee_Monthly_earnings
from EmpWageCompute import employee_totaldays_earnings

def main():
    """
        
        Description: 
           This function is used to call all the methods based on the senarios.
        Parameters:
           choice is used to take an input from the user of type function.
        Return:
            It prints the output according to choice given from user . 
        
    """
    
    choice=int(input("Enter the choice between 1 to 7: /n 1. Check Attendance  /n 2. Daily Earnings /n 3. Part Time Earnings /n 4. Monthly Earnings 5. based on hour and days earnings /n 6. solving above senarious using class and variables /n 7. Exit"))
    
    if choice==1:
        check_attendance()
    
    elif choice==2:
       full_earn= employee_Daily_earnings()     
       print(f"{full_earn} rupees")
       
    elif choice==3:
        part_earn=employee_parttime_earnings()
        print(f"{part_earn} rupees")
        
    elif choice==4:
        month_earning=employee_Monthly_earnings(full_earn,20)
        print(f"{month_earning} rupees")
       
    elif choice==5:
        daily_earn,hour_earn=employee_totaldays_earnings(full_earn,15)
        print(f"daily earnings will be of {daily_earn} rupees")
        print(f"hourly earnings will be {hour_earn} rupees")
    
    elif choice==6:
        print("Thank you for your updates....")
        exit()
        
        
if __name__=="__main__":
    main()
