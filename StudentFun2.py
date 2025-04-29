#Program for student function 2
from Exceptionsschool import InvalidNumberError,ZeroNameLengthError,InvalidNameError,InvalidMarksError,SpaceError,ExistError,NoStudentError
from School.Exceptionsschool import NoStudentError

d={}  #creating an empty dict object to store sno of student as key

def new():
    global d
    s = {} #creating an empty dict object to store name,marks of student
    while(True):
        try:
            sno=int(input("Enter student sno:"))  #there is a chance of Value Error
            if sno in d:
                raise ExistError
            if sno<=0:
                raise InvalidNumberError
            else:
                d[sno]=sno
                break
        except ValueError:
            print("Dont Enter Symbols,Alphabets,and AlphaNumerics")
        except ExistError:
            print("Sno already Exist")
        except InvalidNumberError:
            print("Dont Enter negative digits as sno")
    while(True):
        try:
            name=input("Enter Student name:")
            if len(name)==0:
                raise ZeroNameLengthError
            elif name.isdigit():
                raise InvalidNameError
            elif name.isspace():
                raise SpaceError
            else:
                s["Name"]=name
                break
        except ValueError:
            print("Dont Leave name blankly")
        except ZeroNameLengthError:
            print("Enter something")
        except InvalidNameError:
            print("Dont Enter digits and special symbol")
        except SpaceError:
            print("Dont Enter Spaces")
    while(True):
        try:
            marks=int(input("Enter student marks:"))
            if marks not in range(0,101):
                raise InvalidMarksError
            else:
                s["Marks"]=marks
                d[sno]=s
                break
        except ValueError:
            print("Dont Enter Alphabets,Symbols,Alphanumerics in marks")
        except InvalidMarksError:
            print("Marks are invalid")
    print("Student Details:-\n\tsno:{}\n\tName:{}\n\tMarks:{}\nAdded successfully".format(sno,d[sno]["Name"],d[sno]["Marks"]))

def delete():
    global d
    if len(d)==0:
        print("No students added impossible to delete")
    else:
        while(True):
            try:
                del_details=int(input("Enter Sno of student to delete All details:"))
                if del_details not in d:
                    raise NoStudentError
                else:
                    d.pop(del_details)
                    print("Student Details Deleted Successfully")
                    break
            except ValueError:
                print("Dont Enter Alphabets Alphanumerics or Symbols")
            except NoStudentError:
                print("Student sno Dose not Exist--try again")
def up():
    global d
    if len(d) == 0:
        print("No students added. Impossible to update.")
    else:
        while True:
            try:
                n = int(input("Enter student sno to update: "))
                if n not in d:
                    raise NoStudentError

                # Update name
                while True:
                    try:
                        newname = input("Enter new student name: ")
                        if len(newname) == 0:
                            raise ZeroNameLengthError
                        elif newname.isdigit():
                            raise InvalidNameError
                        elif newname.isspace():
                            raise SpaceError
                        d[n]["Name"] = newname
                        break
                    except ZeroNameLengthError:
                        print("Enter something.")
                    except InvalidNameError:
                        print("Don't enter digits or special symbols.")
                    except SpaceError:
                        print("Don't enter only spaces.")

                # Update marks
                while True:
                    try:
                        newmarks = float(input("Enter new student marks: "))
                        if not (0 <= newmarks <= 100):
                            raise InvalidMarksError
                        d[n]["Marks"] = newmarks
                        break
                    except ValueError:
                        print("Don't enter alphabets, symbols, or alphanumerics in marks.")
                    except InvalidMarksError:
                        print("Marks must be between 0 and 100.")

                print(f"Student Updated Details:\n\tsno: {n}\n\tName: {d[n]['Name']}\n\tMarks: {d[n]['Marks']}")
                break

            except ValueError:
                print("Don't enter alphabets, symbols, or alphanumerics.")
            except NoStudentError:
                print("Student sno does not exist — try again.")

def viewsingle():
    global d,s,sno
    if len(d)==0:
        print("No students added impossible to view")
    else:
        while(True):
            try:
                n=int(input("Enter Student sno to view:"))
                if n not in range(0,101):
                    raise InvalidNumberError
                else:
                    print("Student Details:-\n\tsno:{}\n\tName:{}\n\tMarks:{}\nupdated successfully".format(sno, d[sno]["Name"],d[sno]["Marks"]))
                    break
            except ValueError:
                print("Dont Enter Alphabets,symbols,alphanumerics--try again")
            except InvalidNameError:
                print("sno is invalid--try again")
def viewall():
    global d
    if len(d) == 0:
        print("List is Empty")
    else:
        print("=" * 40)
        print("\tStudents List")
        print("=" * 40)
        print("S.No\t\tName\t\tMarks")
        print("-" * 40)
        for sno, details in d.items():
            print(f"{sno}\t\t\t{details['Name']}\t\t\t{details['Marks']}")


