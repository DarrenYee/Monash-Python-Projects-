"""
Name: Darren Yee Jer Shien
Student ID: 31237223
FIT2004 Assignment 1
"""
def sort_counting_stable(new_list, column):
    '''
    Precondition: new_list must have at least one item

    This is an a full implementation of the counting sort algorithm which is used to be used in the radix sort
    for question 1 of assignment 1.

    :param new_list: list of transactions
    :param column: current column that we are checking
    :return: list sorted according to thr column

    Best Case Complexity: O(n+k)
    Worst Case Complexity: O(n+k)

    Code modified from FIT2004 Tutorial 2
    '''
    a = 0
    base = 10
    max_item = new_list[0] % base
    for item in new_list:
        if item > max_item:
            max_item = item

    # initialize count array
    count_array = [None] * 10
    # update count array
    for i in range(len(count_array)):
        count_array[i] = []
    for item in new_list:
        a = item % base
        count_array[item // (base ** column) % base].append(item)
    # update input list
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(len(frequency)):
            new_list[index] = count_array[i][j]
            index = index + 1
    return new_list


def radix_sort(list):
    """
    normal radix sort implementation for question 1 of assignment 1

    :param list: list of transactions
    :return: sorted list of transactions

    Best Case Complexity: O(nk) where n is the length of the list and k is the number of digits
    Worst Case Complexity: same as Best Case
    """
    maximum_value = max(list)
    base = 10
    col = 0
    while maximum_value > 0:
        sort_counting_stable(list, col)
        col += 1
        maximum_value = maximum_value // 10
    return list


def best_interval(transactions, t):
    """
    Used to find the interval with most transactions

    :param transactions: list of transactions
    :param t: the length of interval
    :return: the starting point of the interval with the most elements available

    The usage of each variables are as follows:
    lo and hi are used as pointers representing the minimum and maximum value of the interval,
    1) best_start and best_end to keep track ofthe current best interval,
    2) tracker and tracker1 to keep track of the current amount of element and the amount of elements
    in the current best interval respectively,
    3) swapped which is a boolean that returns true or false depending if the current transaction
    item is more than the hi
    4) swap which helps to keep track of which start point of interval we should check for next.
    should check for next

    Worst case complexity of this function would be O(nt) where n is the number of elements
    and t is the length of interval needed
    Best case complexity would be O(1) if the list is an empty list. It will loop through the list by using
    two pointers (lo and hi) in order to determine which interval has the most elements

    """
    #checks if transactions is an empty list and returns 0,0 immediately
    if len(transactions) == 0:
        return (0, 0)
    #performs radix_sort on transactions list to make sure similar items are grouped together
    radix_sort(transactions)
    lo = transactions[0]
    hi = lo + t
    best_start = 0
    best_end = 0
    tracker = 0
    tracker1 = 0
    swap = 0
    i = 0
    swapped = False
    #while loop that terminates only when it reaches the final element of the list
    while i <= len(transactions) - 1:
        swapped = False
        hi = lo + t
        #checks if it is within the range of the current interval that we are checking
        if transactions[i] >= lo and transactions[i] <= lo + t:
            tracker = tracker + 1
            i += 1
        else:
            #if not within the range, perform the check of best swap
            swap += 1
            swapped = True
            if swapped == True:
                if tracker > tracker1:
                    # if if the current tracker is higher than the current best tracker, update it
                    best_end = transactions[i - 1]
                    best_start = best_end - t
                    tracker1 = tracker
                    tracker = 0
                else:
                    #else, reset the tracker
                    tracker = 0
            if best_start < 0:
                best_start = 0
            #update lo with the new starting point of the interval
            lo = transactions[swap]
            i = swap
    #final checker for tracker in order to ensure it is correct
    if tracker > tracker1:
        best_end = transactions[i - 1]
        best_start = best_end - t
        tracker1 = tracker
    # if tracker one has not been updated, ie all elements are the same, set tracker1 as the current one
    if tracker1 == 0 and i > 0:
        tracker1 = tracker
        best_start = transactions[i - 1] - t
    #if everything is the same element, set tracker1 as length of the transactions list
    elif tracker1 == 0 and i == 0:
        tracker1 = len(transactions)
    return (best_start, tracker1)

"""
Name: Darren Yee Jer Shien
Student ID :31237223
Assignment 1 Question 2
"""
def sort_counting_alpha_radix(new_list, column):
    '''
    Precondition: new_list must have at least one item
    Counting sort for alphabets using ord and char

    :param new_list = list of words
    :param column = the current column that we are tracking

    Best Case Complexity: O(n+k) where n = number of elements in list and k = range between largest and smallest
    alphabet
    Worst Case Complexity: O(n+k) where n = number of elements in list and k = range between largest and smallest
    alphabet

    Code modified from FIT2004 Tutorial 2
    '''
    # finding max of list
    a = 0
    #sets the maximum item
    for i in range (len(new_list)):
        if len(new_list[i]) >= column+1:
            max_item = ord(new_list[i][column])-97
    for item in new_list:
        if len(item) >= column+1:
            item = ord(item[column])-97
            if item > max_item:
                max_item = item
    # initialize count array
    count_array = [None] * 26
    # update count array
    for i in range(len(count_array)):
        count_array[i] = []
    for item in new_list:
        tracker = 0
        if len(item) >= column+1:
            a = ord(item[column]) - 97
            count_array[a].append(item)
            tracker = 1
        if tracker == 0:
            count_array[0].append(item)
    # update input list
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(len(frequency)):
            if len(new_list[index]) < len(frequency[j]) and index+1 < len(new_list):
                new_list[index+1] = new_list[index]
            new_list[index] = count_array[i][j]
            index = index + 1
    return new_list

def sort_counting_alpha(new_list):
    '''
    Precondition: new_list must have at least one item

    :param new_list : current word in the radix sort

    Best Case Complexity: O(n+k) where n = number of elements in list and k = range between largest and smallest number
    Worst Case Complexity: O(n+k) where n = number of elements in list and k = range between largest and smallest number
    '''
    ans = []
    #finding max of list
    if len(new_list) <= 0:
        return ans.append(new_list)
    max_item = ord(new_list [0])-97
    for item in new_list:
        if len (item) > 0:
            item = ord(item)-97
            if item > max_item:
                max_item = item
    #prints max item
    #initialize count array
    count_array = [0] * (max_item+1)
    #update count array
    for item in new_list:
        count_array [ord(item)-97] = count_array [ord(item)-97] + 1
    #update input list
    index = 0
    for i in range (len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range (frequency):
            ans.append(chr((item)+97))
            index = index + 1
    return ans

def radix_sort_alpha(list):
    """
    used to sort strings using radix sort

    :param list: list of words that contain at least one anagram
    :return: sorted list of words

    Best case complexity = (L1M1 + L2M2) where L1 = number of elements in list 1 M1 = longest string in list 1,
    L2 = number of elements in list 2, M2 = longest string in list 2(bounded by radix sort)
    Best case complexity = (L1M1 + L2M2) where L1 = number of elements in list 1 M1 = longest string in list 1,
    L2 = number of elements in list 2, M2 = longest string in list 2(bounded by radix sort)
    """
    maximum_digits = 0
    for i in range (len(list)):
        if len(list[i]) > maximum_digits:
            maximum_digits = len(list[i])
    col = maximum_digits - 1
    while col >= 0:
        sort_counting_alpha_radix(list, col)
        col -= 1
    return list

def sort_counting(new_list):
    '''
    Precondition: new_list must have at least one item

    Basic counting sort algorithm used to sort the index list based on order.

    :param new_list : list of index
    Best Case Complexity: O(n+k) where n = number of elements in list and k = range between largest and smallest number
    Worst Case Complexity: O(n+k) where n = number of elements in list and k = range between largest and smallest number
    '''
    # checks if first element is empty string and skips if when setting maximum value
    if new_list[0] == "":
        max_item = new_list[1]
    else:
        max_item = new_list[0]
    for item in new_list:
        if item != "":
            if item > max_item:
                max_item = item
    #initializes count array
    count_array = [None] * (max_item+1)
    for i in range (len(count_array)):
        count_array[i] = []
    #checks if item is empty string and automatically appends it to index 0 of count array to ensure it appears first
    for item in new_list:
        if item == "":
            count_array[0].append(item)
        else:
            count_array[item].append(item)
    index = 0
    #update input list and return it
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(len(frequency)):
            new_list[index] = count_array[i][j]
            index = index + 1
    return new_list

def lensort(new_list):
    '''
    Precondition: new_list must have at least one item

    Used to sort the words based on their length, uses a modified version of counting sort

    :param new_list : list of words
    :return new_list: list of strings sorted according to length

    Best Case Complexity: O(n+k) where n = number of elements in list and k = range between largest and smallest number
    Worst Case Complexity: O(n+k) where n = number of elements in list and k = range between largest and smallest number
    '''
    #sets max item according to length of string
    max_item = len(new_list[0])
    for item in new_list:
        if len(item) > max_item:
            max_item = len(item)
    #initialize count array
    count_array = [None] * (max_item+1)
    for i in range (len(count_array)):
        count_array[i] = []
    #update count array
    for item in new_list:
        count_array [len(item)].append(item)
    index = 0
    #update input list
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(len(frequency)):
            new_list[index] = count_array[i][j]
            index = index + 1
    return new_list

def find_anagram (list1,list2):
    """
    Used to find the similar words in both list in order to extract the anagrams

    :param list1: list 1 from words_with_anagram
    :param list2: list2 from words_with_anagrams
    :return: the index of the common values in the list

    The usage of each variables are as follows:
    1) temp is a copy of the list1
    2) tester_a and tester_b sets the starting point of the iteration after checking
    whether it contains empty string.
    3) index is the list we return containing the index of words with anagrams
    4) a and b are current items that we are looking at from list1 and list2 respectively
    5) iterA and iterB are the two pointers that we use to transverse the lists, they are first
    initialized using tester_a and tester_b to start at the item after "" if it exists, if not,
    it will start at the first item.
    6)tracker will be our exit condition which tracks whether iterA or iterB has reached the end of the list

    Best Case Complexity: O(n) where n is the length of either list 1 or list 2 (depending on which is shorter)
    Worst Case Complexity: O(n) where n is the length of either list 1 or list 2 (depending on which is shorter)
    """
    temp = list1.copy()
    tester_a = 0
    tester_b = 0
    index = []
    #checks if list 1 and list 2 contains empty string
    for i in range(len(list1)):
        if len(list1[i]) <= 0:
            tester_a += 1
    for i in range(len(list2)):
        if len(list2[i]) <= 0:
            tester_b += 1
    if tester_a and tester_b > 0:
        index.append("")
    #initializes the first items from list 1 and list 2
    a = list1[tester_a]
    b = list2[tester_b]
    tester = []
    iterA = tester_a
    iterB = tester_b
    tracker = True
    # will only terminate if iterA or iterB reaches the maximum length of each list respectively
    while tracker == True:
        #calls radix sort on the items to check which one is larger
        tester= radix_sort_alpha([a,b])
        #if it is the same, we append the index of item into the list
        if a == b:
            index.append(temp.index(list1[iterA]))
            iterA += 1
            iterB += 1
            # if iterA or iterB reaches the end of the list, set tracker to False for loop termination
            if iterA == len(list1) or iterB == len(list2):
                tracker = False
            else:
                # if not then we increment both iterA and iterB
                a = list1[iterA]
                b = list2[iterB]

        # checks if the previous the item in list A is the same as the previous one since list1 can share an anagram from list2
        elif list1[iterA] == list2[iterB-1]:
            index.append(temp.index(list1[iterA])+1)
            iterA +=1
            if iterA == len(list1):
                tracker = False
            else:
                a = list1[iterA]

        #if b is longer than a, then we increment iterA
        elif len(a) < len(b):
            iterA += 1
            if iterA == len(list1):
                tracker = False
            else:
                a = list1[iterA]
        # if after we radix sort both values a is smaller than b and a's length is less than or equal to b's length, we increment iterA
        elif tester[0] == a and len(a) <= len(b):
            iterA += 1
            if iterA == len(list1):
                tracker = False
            else:
                a = list1[iterA]
        #if all the conditions are not met, then we increment iterB
        else:
            iterB += 1
            if iterB == len(list2):
                tracker = False
            else:
                b = list2[iterB]
    return index

def words_with_anagrams (list1,list2):
    """
    :param list1: list provided by tester
    :param list2: list provided by tester
    :return answer : all the words that are anagrams in between list1 and list2

    variables that are used as follows:
    1) temp is a copy of list1 after counting sort is performed
    2) temp1 is a copy of list1 before anything is performed
    3) answer is the list where we will store the anagrams
    4) index is where we will store the index of anagrams after calling
        find_anagrams

    Best Case Complexity: O(L1M1+L2M2) where L1 = number of elements in list 1 M1 = longest string in list 1,
    L2 = number of elements in list 2, M2 = longest string in list 2(bounded by radix sort)
    Worst Case Complexity: O(L1M1+L2M2) where L1 = number of elements in list 1 M1 = longest string in list 1,
    L2 = number of elements in list 2, M2 = longest string in list 2(bounded by radix sort)
    """

    temp = []
    temp1 = list1.copy()
    answer = []
    index = []
    #call counting sort for all items in list1 and 2 and join the outcome together back into the list
    #this is to ensure that they are sorted alphabetically
    for item in list1:
        if len (item) > 0:
            list1[list1.index(item)] =("".join(sort_counting_alpha(item)))
        else:
            list1[list1.index(item)] = list1[list1.index(item)]
        temp = list1.copy()
    for item in list2:
        if len(item) > 0:
            list2[list2.index(item)] =("".join(sort_counting_alpha(item)))
    #call radix sort for list1 and list2 after they are sorted alphabetically
    radix_sort_alpha(list1)
    radix_sort_alpha(list2)
    #sorts them based on length by using modified counting sort method
    lensort(list1)
    lensort(list2)
    #calls find_anagram method using list1 and list2
    index = find_anagram(list1,list2)
    #sort the index in order by calling original counting sort algorithm
    index = sort_counting(index)
    #append the answers by referencing the index of the items from the temp back into temp1
    for i in range(len(index)):
        # if it is empty string, then we just append it into the answers
        if index[i] == "":
            answer.append(index[i])
        else:
            #if not then we will append the item into the answer and set the current item to 0 in order to avoid words with the same anagrams to reference the wrong thing.
            answer.append(temp1[temp.index(list1[index[i]])])
            temp[temp.index(list1[index[i]])] = 0
    return answer