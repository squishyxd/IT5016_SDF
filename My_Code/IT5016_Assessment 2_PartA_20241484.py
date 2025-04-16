counter = 1  # creates a counter


def staff_info():
    global counter  # calls counter

    while True: # Validate date input otherwise program breaks if blank.
        date = input("Enter Date (DD/MM/YYYY): ").strip()
        if date:
            break
        else:
            print("Date cannot be blank. Please enter a valid date.")

    while True:  # Validate staff ID input otherwise program breaks if blank.
        staff_id = input("Enter Staff ID (XX00): ").strip()
        if staff_id:
            break
        else:
            print("Staff ID cannot be blank. Please enter a valid Staff ID.")

    while True: # Validate staff name input otherwise program breaks if blank.
        staff_name = input("Enter Staff Name: ").strip()
        if staff_name:
            break
        else:
            print("Staff Name cannot be blank. Please enter a valid name.")

    requisition_id = 10000 + counter  # unique requisition id for each entry
    counter += 1  # increment counter for next entry

    return date, staff_id, staff_name, requisition_id

def requisitions_total():
    total = 0
    items = []  # list to store items

    while True:
        item = input("Enter item name (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        if not item:
            print("Item name cannot be blank. Please enter a valid item name.")
            continue

        while True: # Validate price input otherwise program breaks if blank and not number.
            price_input = input("Enter item price: ").strip()
            if not price_input:
                print("Price cannot be blank. Please enter a valid price.")
                continue
            try:
                price = float(price_input)
                break
            except ValueError:
                print("Invalid price. Please enter a numeric value.")

        total += price  # add price to total
        items.append(item)  # add item to list

    return total

def requisition_approval(total, staff_id, requisition_id):
    status = "Pending"
    approval_reference = "N/A"

    if total < 500:
        status = "Approved"
        approval_reference = staff_id + str(requisition_id)[-3:]  # staff ID plus last 3 digits of requisition ID

    return status, approval_reference

def display_requisitions(): # Collect staff info and requisition details
    date, staff_id, staff_name, requisition_id = staff_info()
    total = requisitions_total()
    status, approval_reference = requisition_approval(total, staff_id, requisition_id)

    # Display summary
    print("\nRequisition Summary:")
    print("Date:", date)
    print("Requisition ID:", requisition_id)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Total: $" + str(total))
    print("Status:", status)
    if status == "Approved":
        print("Approval Reference Number:", approval_reference)


# Call the display_requisitions function to execute the full workflow
display_requisitions()
