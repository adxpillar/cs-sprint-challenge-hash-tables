#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # trip will cover length-1 routes 
    # routes = [None] * (length - 1)
    routes = {}
    # iterate through entire trip
    for i in range(length):
        # set ticket for each trip
        ticket = tickets[i]
        # set source for each trip
        source = ticket.source
        # set destination for each trip
        destination = ticket.destination

        # no last flight - "FLG"
        # 
        if "NONE" not in routes:
            routes[i] = ticket.destination
            i += 1
    return list(routes)