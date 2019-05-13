def main():
    x = 0
    class_name_list = []
    credits_total = 0
    working = True
    while working:
        class_name = input("Enter the class you want to add or hit 'Enter' to exit-> ")
        if class_name == "": #checking if the classname is an emty string"""
            
           break   #if it is empty exiting the while loop"""

        
        if class_name in class_name_list:
              print("You have entered this class already. Add another class. ")
              continue
        
        else:
              class_name_list.append(class_name)

        credit = float(input("Enter the class credits -> "))
        credits_total += credit

        score = float(input("Enter your score: -> "))
        if score >= 93:
             x += credit*4
        elif score >= 90:
             x += credit*3.7
        elif score >= 87:
             x += credit*3.3
        elif score >= 83:
             x += credit*3
        elif score >= 80:
             x += credit*2.7
        elif score >= 77:
             x += credit*2.3
        elif score >= 73:
             x += credit*2
        elif score >= 70:
             x += credit*1.7
        elif score >= 67:
             x += credit*1.3
        elif score >= 60:
             x += credit*1
        else:
             x += credit*0


        gpa=x/credits_total

        print ("Your GPA is " + str(gpa) + ".")


main()
      

     

