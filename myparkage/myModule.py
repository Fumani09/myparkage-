def top_n(items, n):
    """ Return the top n in an arrary, in desc order.

    args:
        items(array): list or arrary-like object
        n(int): num of items to return

    Return:
        array: top n items, in desc order
    
    Egs:
        >>>top_n([7,2,4,8,1], 3)
        [8,7,4]
    """
    for i in range(n): # Keep sorting until we have top n numbers
        for j in range(len(items)-1-1):
        
            if items[j] > items[j+1]:  # if this item is bigger than next item...
             items[j], items[j+1] = items[j+1], items[j] # Swap the two!
        # Get last two items
        top_n = items[-n:]

    return top_n[::-1]