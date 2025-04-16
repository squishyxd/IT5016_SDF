
class RequisitionSystem:  #actual function of lass
    requisition_counter = 10000
    requisitions = []

    def __init__(self, date, staff_id, staff_name, items): #sets names inside class and tests values for boundary's
        if not date:
            date = input("Date is missing. Please enter date: ")
        if not staff_id:
            staff_id = input("Staff ID is missing. Please enter staff ID: ")
        if not staff_name:
            staff_name = input("Staff Name is missing. Please enter staff name: ")
        if not items:
            items = {}
            print("Items are missing. Please enter items and their prices.")
            while True:
                item_name = input("Enter item name (or 'done' to finish): ")
                if item_name.lower() == 'done':
                    break
                item_price = float(input(f"Enter price for {item_name}: "))
                items[item_name] = item_price

        RequisitionSystem.requisition_counter += 1
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = RequisitionSystem.requisition_counter
        self.total = 0
        for item in items:
            self.total += items[item]

        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

        RequisitionSystem.requisitions.append(self)

    def respond(self, decision): #responds to value of said boundary
        if self.status == "Pending":
            if decision.lower() == "approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
            elif decision.lower() == "not approved":
                self.status = "Not approved"
                self.approval_reference = "Not available"

    @classmethod
    def display_requisitions(cls): #prints stored values
        print("\nPrinting Requisitions:\n")
        for r in cls.requisitions:
            print("Date:", r.date)
            print("Requisition ID:", r.requisition_id)
            print("Staff ID:", r.staff_id)
            print("Staff Name:", r.staff_name)
            print("Total: $" + str(r.total))
            print("Status:", r.status)
            print("Approval Reference Number:", r.approval_reference, "\n")

    @classmethod  #statistics part of program does same as about but all in one class/function
    def requisition_statistics(cls):
        total = len(cls.requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for r in cls.requisitions:
            if r.status == "Approved":
                approved += 1
            elif r.status == "Pending":
                pending += 1
            elif r.status == "Not approved":
                not_approved += 1

        print("\nStatistics:")
        print("Total requisitions submitted:", total)
        print("Approved:", approved)
        print("Pending:", pending)
        print("Not approved:", not_approved)

# Testing the class, remove value for error that says you have empty value:
req1 = RequisitionSystem("03/04/2024", "FN19", "John Paul", {"Coffee": 200, "Paper": 100, "Pen": 50})
req2 = RequisitionSystem("05/04/2024", "FN20", "Tracy Brown", {"Laptop": 1000})
req3 = RequisitionSystem("07/05/2024", "FN15", "Emma Wellington", {"Printer": 3500})
req3.respond("not approved")
req4 = RequisitionSystem("03/05/2024", "FN02", "Catlin White", {"Chair": 490})
req5 = RequisitionSystem("09/05/2024", "FN22", "Alex Green", {"Table": 800})
req5.respond("approved")

#calling class to run program.
RequisitionSystem.display_requisitions()
RequisitionSystem.requisition_statistics()


