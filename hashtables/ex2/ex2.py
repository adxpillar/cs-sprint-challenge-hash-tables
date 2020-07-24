#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here


    # index destination to depature 
    # each destination is precursor for next depature 
    # starting_point = source and ending_point = destination

    # path of flight route 
    route = [None] * length
    # hold tickets here 
    tix_cache = {}

    for ticket in tickets:
        # connect each ticket with it's destination
        tix_cache[ticket.source] = ticket.destination
    # move through source-destination using 
    # since both start at none 
    next = tix_cache["NONE"]
    # use 
    for departure in range(0, length):
        route[departure] = next
        next = tix_cache[next]
    return route