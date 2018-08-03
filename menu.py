import cx_Oracle
conn = cx_Oracle.connect('SYSTEM/SYSTEM')
cur = conn.cursor()
#import class_doctor
        
def print_menu():       ## Your menu design here
    
    print ('''-----------------------------Menu-----------------------------
    	1. Patient registration
    	2. Patient Payment
    	3. Medical reports
    	4. Bill Receipts
    	5. Doctor Details
    	6. Patient Details
    	7. Staff Details
    	8. Exit''')


print("Welcome to Hospital Management System!") 
loop=True      
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = int(input("Enter your choice [1-8]: "))
     
    if choice==1:     
        print ("----------------------Menu 1 has been selected---------------------")
        
        choice_2 = int(input('''Enter choice:
        	1. Schedule Appointment
        	2. New Entry'''))
        if choice_2==2:
            import check

            k=int(input("enter the patientid: "))
            l=input("name: ")
            m=input("gender: ")
            n=input("address: ")
            o=int(input("telephone number: "))
            p=int(input("doctor code: "))
            obj1=check.entry(k,l,m,n,o,p)

            obj1.enter()
        ## Hospital sub-menu
    elif choice==2:
        print ("----------------------Menu 2 has been selected---------------------")
        import option2
        k=int(input("Enter the patient id of patient to check payment details: "))
        obj2=option2.payment(k)
        obj2.pay_detail()
        ## You can add your code or functions here
    elif choice==3:
        print ("----------------------Menu 3 has been selected---------------------")
        choice_2=int(input('''Enter choice:
                      1. Discharge
                      2. Hospital Admission '''))
        ## Medical report sub-menu
    elif choice==4:
        print ("----------------------Menu 4 has been selected---------------------")
        import option4
        l=int(input("Enter the patient id to generate bill receipt"))
        obj4=option4.receipt(l)
        obj4.display()

        ## You can add your code or functions here
    elif choice==5:
        print ("----------------------Menu 5 has been selected---------------------")
        #choice =
        import option5
        dr_code=int(input("Enter the doctor code or id"))
        ob5=option5.doctor(dr_code)
        ob5.view_details()
        
    elif choice==6:
        print ("----------------------Menu 6 has been selected---------------------")
       
        pat_id = int(input("Please Enter Patient ID: "))
        obj6 = Pat_View(pat_id)
        obj6.view_details()

        
    elif choice==7:
        print ("----------------------Menu 7 has been selected---------------------")
        choice = int(input("""Select an option:
        1. View details
        2. Add staff member
        """))
        if choice == 1:
            import option7
            staff_id = int(input("Enter staff ID: "))
            obj7 = option7.Staff_View(staff_id)
            obj7.view_details()
            
        elif choice ==2:
                     pass
                     #add code here
        else:
                     print("Invalid Option")
    else:
        loop=False # This will make the while loop to end as not value of loop is set to False