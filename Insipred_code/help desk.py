class Ticket:
    ticket_id_counter = 1
    stats = {'submitted': 0, 'resolved': 0, 'in_progress': 0, 'closed': 0}
    tickets = []

    def __init__(self, employee_id, name, issue):
        self.id = Ticket.ticket_id_counter
        Ticket.ticket_id_counter += 1
        self.employee_id = employee_id
        self.name = name
        self.issue = issue
        self.priority = self.set_priority()
        self.status = "In Progress"
        self.resolution = ""

        if "password reset" in issue.lower():
            self.status = "Resolved"
            self.resolution = "Password reset. New pass: " + name[:2] + str(employee_id)[-2:]

        Ticket.stats['submitted'] += 1
        if self.status == "Resolved":
            Ticket.stats['resolved'] += 1
        else:
            Ticket.stats['in_progress'] += 1

        Ticket.tickets.append(self)

    def set_priority(self):
        if "system outage" in self.issue.lower():
            return "High"
        elif "password reset" in self.issue.lower():
            return "Low"
        else:
            return "Medium"

    def manager_approve(self):
        if self.priority == "High" and self.status == "In Progress":
            self.status = "Closed"
            self.resolution = "Manager approved resolution."
            Ticket.stats['in_progress'] -= 1
            Ticket.stats['closed'] += 1

    def display(self):
        print("--------Info--------")
        print("")
        print("---------------------")
        print("Ticket ID:", self.id)
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Issue:", self.issue)
        print("Priority:", self.priority)
        print("Status:", self.status)
        print("Resolution:", self.resolution)
        print("-------------------")
        print("")

def show_stats():
    print("--------statistics--------")
    print("")
    print("---------------------")
    print("Tickets Submitted:", Ticket.stats['submitted'])
    print("Resolved:", Ticket.stats['resolved'])
    print("In Progress:", Ticket.stats['in_progress'])
    print("Closed:", Ticket.stats['closed'])
    print("---------------------")
    print("")

t1 = Ticket(101, "Alice", "password reset")
t2 = Ticket(102, "Bob", "system outage")

t2.manager_approve()

for t in Ticket.tickets:
    t.display()

show_stats()
