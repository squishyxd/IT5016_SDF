# requisitionsystem.py

requisition_counter = 10000  # Global counter for unique requisition IDs

class RequisitionSystem:
    requisitions = []

    def __init__(self):
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.items = {}
        self.total = 0.0
        self.requisition_id = 0
        self.status = ""
        self.approval_reference = ""

    def staff_info(self):
        self.date = input("Enter date (dd/mm/yyyy): ")
        self.staff_id = input("Enter staff ID: ")
        self.staff_name = input("Enter staff name: ")

    def requisitions_details(self):
        print("Enter requisition items and their prices:")
        while True:
            item_name = input("Enter item name (or 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            try:
                item_price = float(input(f"Enter price for {item_name}: "))
                self.items[item_name] = item_price
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
        self.total = sum(self.items.values())
        return self.total

    def requisition_approval(self):
        global requisition_counter
        requisition_counter += 1
        self.requisition_id = requisition_counter

        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
        elif 500< self.total<999: #confused never actually pending. unless manager approval after outputs.
            self.status = "Pending"
            self.approval_reference = "Not available"
        else:#partA didnt have not approved have created based on guess.
            self.status = "Not Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]

        RequisitionSystem.requisitions.append(self)

    def respond_requisition(self, decision):
        if self.status == "Pending":
            if decision.lower() == "approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
            elif decision.lower() == "not approved":
                self.status = "Not approved"
                self.approval_reference = "Not available"

    @classmethod
    def display_requisitions(cls):
        print("\nRequisitions Info:\n")
        for r in cls.requisitions:
            print("Date:", r.date)
            print("Requisition ID:", r.requisition_id)
            print("Staff ID:", r.staff_id)
            print("Staff Name:", r.staff_name)
            print("Total: $" + str(r.total))
            print("Status:", r.status)
            print("Approval Reference Number:", r.approval_reference, "\n")

    @classmethod
    def requisition_statistic(cls):
        total = len(cls.requisitions)
        approved = sum(1 for r in cls.requisitions if r.status == "Approved")
        pending = sum(1 for r in cls.requisitions if r.status == "Pending")
        #not_approved = sum(1 for r in cls.requisitions if r.status == "Not approved")
        not_approved = sum(1 for r in cls.requisitions if r.status.lower() == "not approved")

        print("\nStatistics:")
        print("Total requisitions submitted:", total)
        print("Approved:", approved)
        print("Pending:", pending)
        print("Not approved:", not_approved)


# Example run
if __name__ == "__main__":
    num_reqs = int(input("How many requisitions would you like to enter? "))
    for _ in range(num_reqs):
        req = RequisitionSystem()
        req.staff_info()
        req.requisitions_details()
        req.requisition_approval()

        if req.status == "Pending":
            decision = input("Manager decision for pending requisition (approved/not approved): ")
            req.respond_requisition(decision)

    RequisitionSystem.display_requisitions()
    RequisitionSystem.requisition_statistic()
