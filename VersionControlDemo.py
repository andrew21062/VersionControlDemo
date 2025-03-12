# Andrew Wong
# Version 2

def add_record():
    staff_code = input("Enter Staff code: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary amount:")
    with open("staff.txt", "a") as file:
        file.write(f"{staff_code},{name},{salary}\n")
    print("Record added successfully.")

def delete_record():
    staff_code = input("Enter Staff code to delete: ")
    records = []
    with open("staff.txt", "r") as file:
        records = file.readlines()
    with open("staff.txt", "w") as file:
        found = False
        for record in records:
            if not record.startswith(staff_code + ","):
                file.write(record)
            else:
                found = True
        if found:
            print("Record deleted successfully.")
        else:
            print("Record not found.")

def view_records():
    try:
        with open("staff.txt", "r") as file:
            records = file.readlines()
            if records:
                print("\nStafft Records:")
                for record in records:
                    staff_code, name, salary = record.strip().split(",")
                    print(f"Staff code: {staff_code}, Name: {name}, Salary: {salary}")
            else:
                print("No records found.")
    except FileNotFoundError:
        print("No records found.")

def main():
    while True:
        print("\nMenu")
        print("1. Add Record")
        print("2. Delete Record")
        print("3. View Records")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_record()
        elif choice == "2":
            delete_record()
        elif choice == "3":
            view_records()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
