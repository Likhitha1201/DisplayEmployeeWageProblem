""" 

    @Author: Likhitha S
    @Date: 02-10-2024 18:00
    @Last Modified by: Likhitha S
    @Last Modified time: 02-10-2024 18:00
    @Title:Write a Python program to check employee attendence using random.

"""


from EmpWageCompute import check_attendance
from EmpWageCompute import employee_earnings

def main():
    """
        
        Description: 
           This function is used to check employee attendence.
        Parameters:
          fun_name is used to an input from the user of type function.
        Return:
            It prints the output according to that fun_type . 
        
    """
    
    choice=int(input("Enter the choice between 1 to 7: "))
    
    if choice==1:
        check_attendance()
    
    elif choice==2:
       full_earn= employee_earnings()     
       print(f"{full_earn} rupees")
       
    elif choice==3:
        part_earn=employee_earnings()
        print(f"{part_earn} rupees")
        
    elif choice==4:
        main()
    
    elif choice==5:
        month_earning=employee_earnings(full_earn,part_earn)
        print(f"{month_earning} rupees")
if __name__=="__main__":
    main()
