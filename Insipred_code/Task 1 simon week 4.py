import uuid #used for creating unique ids

def create_donation_request():
    requester_name = input("Enter your name: ")
    project_name = input("Enter the project name: ")
    request_id = str(uuid.uuid4())[:8]  # this is a simple way to create a unique id.
    return requester_name, project_name, request_id

def collect_donation_items():
    total_amount = 0
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ")
        if item_name.lower() == 'done': #allows you to add items until you type done to continue.
            break
        item_price = float(input("Enter item price: "))
        total_amount += item_price #calcs total price of items added.
    return total_amount

def approve_request(requester_name, project_name, request_id, total_amount):
    priority = "Low" #basic priority is set to low
    status = "Pending"
    approval_id = "None"
    if "family" in project_name:
        priority = "High" #if family is in project name set priority to high.
        status = "Approved"
        approval_id = request_id + requester_name[-2:]
    elif total_amount < 500:
        priority = "Medium" #else if total is < 500 the set the priority to medium.
        status = "Approved"
        approval_id = request_id + requester_name[:2]
    return priority, status, approval_id

def display_request_details(requester_name, project_name, request_id, total_amount, status, priority, approval_id):
    print("\n--- Donation Request Details ---")
    print("Request ID:", request_id)
    print("Requester Name:", requester_name)
    print("Project Name:", project_name)
    print("Total Amount Requested:", total_amount)
    print("Approval Status:", status)
    print("Priority Level:", priority)
    if approval_id != "None":
        print("Approval ID:", approval_id)

requester_name, project_name, request_id = create_donation_request() #assigns RN PN and RI to input in function.
total_amount = collect_donation_items() #sets total to calc in function.
priority, status, approval_id = approve_request(requester_name, project_name, request_id, total_amount) # assigns priority status and AP to approve request function and passes previous function names through to current function.
display_request_details(requester_name, project_name, request_id, total_amount, status, priority, approval_id) #runs function passing previous values to current function.
