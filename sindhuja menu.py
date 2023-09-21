import os
def menu():
    print("Main Menu")
    print("1.create a file")
    print("2.Reaname file ")
    print("3.Print the info in file ")
    print("4. add info to the file")
    print("5.Exit ")



print("Choose a option ")
menu()
choice = int(input("Enter your option : "))
f_name = "hello.txt"
file = open("hello.txt", "w")
file.close()
while (choice != 5):
    if (choice ==1):
        f_name = input("Enter the file name")
        f_name = f_name+".txt"
        file = open(f_name, "w")



    elif (choice == 2):
        user_file_name = input("Enter the file name")
        user_file_name = user_file_name+".txt"
        os.rename(f_name, user_file_name)
        f_name = user_file_name
    elif (choice == 3):
        out = open(f_name,"r")
        print(out.read())
    elif (choice == 4):
        file = open(f_name, "a")
        info_toadd = input("enter the info you want to add")
        file.write(info_toadd)
        file.close()
    elif (choice == 5):
        print("Thank you exiting application")
        break
    choice = int(input("Enter your option : "))
