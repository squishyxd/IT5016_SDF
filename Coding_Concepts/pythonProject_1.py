#this is a basic calc code:
from logging import basicConfig

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
solution=num1+num2
print(solution)

#this is a age calc:

name= input("Please enter your name: ")
age= int(input("please enter your age: "))
year= 2025
curage= year-age
print ("your name is,", (name), (curage))


#this is a grade calc:

m1=int(input("mark1:"))
m2=int(input("mark2:"))
m3=int(input("mark3:"))
m4=int(input("mark4:"))
grade=(m1+m2+m3+m4)/4

if(grade>50):
    print("You pass, final score:",grade,"%")
else:
    print("You Fail, final score:",grade,"%"# )

#this is a loop and includes boolein


while True:
     Get user input for marks
    m1 = int(input("Enter mark 1: "))
    m2 = int(input("Enter mark 2: "))
    m3 = int(input("Enter mark 3: "))
    m4 = int(input("Enter mark 4: "))

     Calculate the average grade
    grade = (m1 + m2 + m3 + m4) / 4

     Boolean variable to check if the student passes
    is_pass = grade > 50

     Conditional statement based on the boolean variable
    if is_pass:
        print("You pass! Final score:", grade, "%")
    else:
        print("You fail. Final score:", grade, "%")

    # Ask if the user wants to continue
    again = input("Do you want to enter another set of marks? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break

functions
def add (a,b):
    return a+b

def sub(a,b):
    return a-b

def main():
    a=10
    b=20
    print(add (a,b))

if __name__ =="__main__":
    main()

counter = 1

def gym_member_info():
    global counter
    name = input("Please enter your first and last name: ")
    date = input("Please enter the date (dd/mm/yyyy): ")
    member_id = counter
    counter += 1

    print("Date:", date)
    print("Name:", name)
    print("Member ID:", member_id)

    return name, date, member_id

def membership_fees_total(name):
    print("Hello", name)

    add_ons = int(input("How many add-ons? "))
    total = sum(float(input("Enter price for add-on: $")) for _ in range(add_ons))

    print("Thanks", name)
    print("Your total is: $", total)

    return total

def gym_member_approval(name, total, member_id):
    status, ref_number = ("Approved", name + str(member_id)) if total < 1000 else ("Pending", "Pending")

    print("\nApproval Status:", status)
    print("Reference Number:", ref_number)

    return status, ref_number

name, date, member_id = gym_member_info() # assigns name, date and member id in the called function.
total_fee = membership_fees_total(name)  #assigns total fee and passes name from previous function to stop the funtion running multplie times
gym_member_approval(name, total_fee, member_id) #calls final function and passes name, total fee and member id from the previous funtions.


