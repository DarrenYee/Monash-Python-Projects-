def bubble_sort(the_list):
    """sorts the list using bubble sort.
       time complexity: best (n^2), worst (n^2), average (n^2)
    """

    n = len(the_list)
    for a in range (n-1):                       #checks until n-1
        for i in range (n-1):                   #nested loop checks until n-1
            item = the_list [i]                 #current item will be the the item in the index that i is iterated to
            item_to_right = the_list [i+1]      #item to right is the next item after the current iteration
            if item > item_to_right:            #compares the current item with the item to the right and if it is more than the item to the right then swapping will occur.
                the_list[i] = item_to_right
                the_list[i+1] = item