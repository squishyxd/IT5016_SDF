# requisitionsystem.py

requisition_counter = 10000  # Global counter for unique requisition IDs

class RequisitionSystem:
    requisitions = []  # sets requisitions to empty so that user input can be saved later.

    def __init__(self): #sets all data needed to be captured
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.items = {}
        self.total = 0.0
        self.requisition_id = 0
        self.status = ""
        self.approval_reference = ""

    def staff_info(self): #asks user to input staff information
        self.date = input("Enter date (dd/mm/yyyy): ")
        self.staff_id = input("Enter staff ID: ")
        self.staff_name = input("Enter staff name: ")

    def requisitions_details(self): #asks user to enter requistion items and price
        print("Enter requisition item and then the price:")
        while True:
            item_name = input("Enter item name (or 'done' to finish): ")
            if item_name.lower() == "done":
                break
            try:
                item_price = float(input(f"Enter price for {item_name}: "))
                self.items[item_name] = item_price
            except ValueError:
                print("Invalid price. Please enter a number.")

        self.total = sum(self.items.values())
        print(f"Total requisition value: ${self.total:.2f}")

    def requisition_approval(self): #automaticcly calculates if requistion is Approved/NotApproved/Pending
        global requisition_counter
        requisition_counter += 1
        self.requisition_id = requisition_counter

        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
        elif 500 <= self.total < 1000:
            self.status = "Pending"
            self.approval_reference = "Not available"
        else:
            self.status = "Not Approved"
            self.approval_reference = "Not available"

        RequisitionSystem.requisitions.append(self)

    def respond_requisition(self): #allows manager to approve or not approve pending requistions
        if self.status == "Pending":
            decision = input(f"Requisition {self.requisition_id} is pending. Manager decision (approved/not approved): ")
            if decision.lower() == "approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
            elif decision.lower() == "not approved":
                self.status = "Not Approved"
                self.approval_reference = "Not available"

    @classmethod
    def display_requisitions(cls): #prints requisition details
        print("\n All Requisitions:")
        for r in cls.requisitions:
            print(f"Date: {r.date}")
            print(f"Requisition ID: {r.requisition_id}")
            print(f"Staff ID: {r.staff_id}")
            print(f"Staff Name: {r.staff_name}")
            print("Items:")
            for item, price in r.items.items():
                print(f"{item}: ${price}")
            print(f"Total: ${r.total}")
            print(f"Status: {r.status}")
            print(f"Approval Reference: {r.approval_reference}")
            print("" * 10)

    @classmethod
    def requisition_statistic(cls): #prints requisition statistics
        total = len(cls.requisitions)
        approved = sum(1 for r in cls.requisitions if r.status == "Approved")
        pending = sum(1 for r in cls.requisitions if r.status == "Pending")
        not_approved = sum(1 for r in cls.requisitions if r.status == "Not Approved")

        print("\n Requisition Statistics:")
        print(f"Total submitted: {total}")
        print(f"Approved: {approved}")
        print(f"Pending: {pending}")
        print(f"Not Approved: {not_approved}")



def run_requisition_system(): #actual operation of program
    print("Requisition System:")
    try:
        num_reqs = int(input("How many requisitions would you like to submit? "))
    except ValueError:
        print("Invalid input. Exiting.")
        return

    for i in range(num_reqs):
        print(f"\n Requisition {i+1} :")
        req = RequisitionSystem()
        req.staff_info()
        req.requisitions_details()
        req.requisition_approval()
        req.respond_requisition()  # Manager response if needed

    RequisitionSystem.display_requisitions()
    RequisitionSystem.requisition_statistic()


# Runs the program when file tested
run_requisition_system()
