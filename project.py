import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='')as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "age", "contact no", "emailid"])
        
        writer.writerow(info_list)
        
if __name__== '__main__':
    condition = True
    student_num =1
    while(condition):
        student_info = input("Enter student information for student #{} in  following format(name, age, contact number, email id):".format(student_num))
        print("Entered information: "+student_info)
    
        student_info_list =student_info.split(' ')
        print("entered split up information is:" + str(student_info_list))
        
        print("\nthe entered information is -\nName: {}\nAge: {}\nContact number: {}\nEmail id: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3] ))
    
        choice_check = input("is the entered info correct? yes or no:")
        if choice_check == "yes":
            
        
            write_into_csv(student_info_list)
    
            condition_check = input("Enter yes / no if you want to enter information for another student: ")
            if condition_check == "yes":
                condition = True
                student_num =student_num + 1
            elif condition_check == "no":
                condition = False
            
        elif choice_check =="no":
            print("\nplease re enter the values")