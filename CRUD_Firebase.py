from firebase import firebase


class InsertionError(Exception):
    pass


class InvalidInput(Exception):
    pass


def InsertData(data):
    result = fireb.post('/mlh-day5-default-rtdb/Students/', data)
    if result:
        print("Data insertion sucessfull\n"
              f"ID:{result}\n")


def DeleteData(ID):
    fireb.delete('/mlh-day5-default-rtdb/Students/', ID)
    print("Data Deleted Sucessfully\n")


def UpdateData(data, ID):
    path = '/mlh-day5-default-rtdb/Students/' + ID
    for key, value in data.items():
        fireb.put(path, key, value)
    print("Data Updated sucessfully\n")


def DisplayData():
    data = fireb.get('/mlh-day5-default-rtdb/Students/', "")
    return data


fireb = firebase.FirebaseApplication("https://mlh-day5-default-rtdb.firebaseio.com/", None)

while True:
    try:
        choice = int(input("1. Insert Data\n"
                           "2. Display Data\n"
                           "3. Update Data\n"
                           "4. Delete Data\n"
                           "5. Exit\n"
                           "Enter your choice >>>"))
        print()
        if choice == 1:
            
            name = input("Student name: ")
            roll = input("Student Roll No.: ")
            marks = input("Student Marks: ")
            
            studentData = {"Name": name, "Roll No": roll, "Marks": marks}
            
            InsertData(studentData)
        
        elif choice == 2:
            database = DisplayData()
            for key,value in database.items():
                print(f"{key}:{value}")
            print()
        
        elif choice == 3:
            RowID = input("Enter RowID of the row you want to update with '-'\n"
                          "RowID: ")
            print()
            update_choice = int(input("What do you want to update\n"
                                      "1. Name\n"
                                      "2. Roll No.\n"
                                      "3 Marks\n"
                                      "4 Whole row \n"
                                      "5. Exit \n"
                                      "Enter your choice >>>"))
            if update_choice == 1:
                name = input("New name: ")
                update_data = {"Name": name}
                UpdateData(update_data, RowID)
            
            elif update_choice == 2:
                roll = input("New Roll No: ")
                update_data = {"Roll No": roll}
                UpdateData(update_data, RowID)
            
            elif update_choice == 3:
                marks = input("New Marks: ")
                update_data = {"Marks": marks}
                UpdateData(update_data, RowID)
            
            elif update_choice == 4:
                name = input("New name: ")
                roll = input("New Roll No.: ")
                marks = input("New Marks: ")
                update_data = {"Name": name, "Roll No": roll, "Marks": marks}
                UpdateData(update_data, RowID)
            
            elif choice == 5:
                print()
                continue
            
            else:
                raise InvalidInput
        
        elif choice == 4:
            RowId = input("Enter RowID of the row you want to delete\n"
                          "RowID: ")
            DeleteData(RowId)
        
        elif choice == 5:
            exit()
        
        else:
            raise InvalidInput
    
    except InvalidInput:
        print("Enter a Valid number")
