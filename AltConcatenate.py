"""
    Function takes 2 lists, and adds them into each other alternating the merger
    If the two input lists are uneven in length, the function adds None elements to "result"
    Function then calls itself till both lists are even, and then altenates them
    Creates list "result", adds list a into it, with an inteval of 2
    Result takes list b, starting on 2nd element and inteval of 2
    Lastly, checks if there are any "None"'s inside result, and deletes them before printing

    :param list1: 
    :param list2:
    :return: Merges both lists together alternating the elements between each
"""

#### Function ####

def altconcatenate(list1, list2):
    if len(list1) == len(list2):
        result = [None] * (len(list1) + len(list2))
        result[::2] = list1
        result[1::2] = list2
        for i in range(len(result) -1, -1, -1):
            if result[i] == None:
                result.remove(None)
        else:
            print(result)
            return
    else:
        if len(list1) < len(list2):
            list1.append(None)
            return altconcatenate(list1, list2)
        else:
            if len(list2) < len(list1):
                list2.append(None)
                return altconcatenate(list1, list2)
        
      
