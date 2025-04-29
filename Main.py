from StudentFun2 import new,delete,up,viewall,viewsingle
from Exceptionsschool import NoStudentError,InvalidNameError,SpaceError
print("="*50)
print("\t\tStudent information System:")
print("="*50)
print("\t\t1.Add new student")
print("\t\t2.Delete Student")
print("\t\t3.Update Student Details")
print("\t\t4.View Single student Details")
print("\t\t5.View all Students")
print("\t\t6.EXIT")
print("="*50)
while(True):
    try:
        n=int(input("Enter Your Choice from above:"))
        if n not in range(1,7):
            print("INVALID SELECTION")
        else:
            match (n):
                case 1:
                    new()
                case 2:
                    delete()
                case 3:
                    up()
                case 4:
                    viewsingle()
                case 5:
                    viewall()
                case 6:
                    print("Thank for using-You have Been Exited")
                    break
    except ValueError:\
            print("Dont Enter Symbols,Alphabets and Alnums for selection")
    except NoStudentError:
            print("Student does not exist")
    except InvalidNameError:
        print("Invalid name")
    except SpaceError:
        print("Dont enter space")

