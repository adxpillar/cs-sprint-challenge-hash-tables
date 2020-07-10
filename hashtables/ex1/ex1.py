def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create hash table
    index = {}
    # enumerate weights 
    for key,value in enumerate(weights):
        # conditional
        wb = limit - value
        if wb not in index:
            # swap value for list index
            index[value] = key
        else:
            return key,index[wb]
    return None
