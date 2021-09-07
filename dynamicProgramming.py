"""
Name: Darren Yee Jer Shien
Student ID: 31237223
FIT2004 Assignment 2
"""

# Assignment 2 Q1 (Jobs)
def convert_to_tuple (weekly_income):
    """
    Complexity of O(n) where n is the number of elements in the weekly_income list
    Space Complexity of O(n) where n is the number of elements in the weekly_income list
    :param weekly_income:
    :return: weekly_income list in tuples to match competitions
    """
    for i in range (len(weekly_income)):
        weekly_income[i] = i+1,i+1,weekly_income[i]
    return weekly_income

def convert_week_start_1 (competitions):
    """
    Complexity of O(n) where n is the number of elements in the competitions list
    Space Complexity of O(n) where n is the number of elements in the competitions list
    :param competitions:
    :return: competitions list converted so that it starts at week 1
    """
    for i in range (len(competitions)):
        competitions[i] = competitions[i][0]+1,competitions[i][1]+1,competitions[i][2]
    return competitions


def best_schedule (weekly_income, competitions):
    """
    First, convert the weekly income to tuple and join it with competitions
    Then, sort it according to the end date
    After that, use memoization and compare the amount of money that we get with the take the amount of money that can
    be earned before the current start date from the memor list and compare it with the current amount of money that we
    have with the same end date in the memo list. Replace it if it is more and ignore if it is less
    The time complexity of this is O(nlogn) which is bounded by the built in sort
    The space complexity of this is O(N) where N is total number of weekly income and competition items combined
    :param weekly_income: list of weekly income
    :param competitions: list of competitions
    :return: memor[-1][2] which will be the amount of money the best_schedule yields.
    """
    if len(weekly_income) == 0: #returns zero if both are empty lists
        return 0
    #initializes the memo lists
    memor = []
    weekly_income = convert_to_tuple(weekly_income) #converts weekly income into tuple of (start,end,profit)
    weekly_income.extend(convert_week_start_1(competitions)) # joins the two list together for comparison
    weekly_income.sort(key=lambda x: x[1]) #sorts the whole list according to its end day
    # initializes the memo lists
    for i in range (weekly_income[-1][1] + 1):
        memor.append((0,0,0))
    #keeps compare to memo list to see whether
    for i in range (len(weekly_income)):
        a = len(memor)
        index = weekly_income[i][1]
        #checks if value in memor is more than the current one plus what comes before it
        if memor[a-1][2] < (memor[index][2] + weekly_income[i][2]):
            if weekly_income[i][2] + memor[weekly_income[i][0]-1][2] > memor[index][2]:
                memor[index] = ([weekly_income[i][0],weekly_income[i][1],weekly_income[i][2]+memor[weekly_income[i][0]-1][2]])
    return memor[-1][2]


def best_itinerary (profit,quarantine_time,home):
    """
    Creates 4 different memo matrix (nd) where memo takes down the values normally
    memo2 takes down the values if staying
    memo3 takes down the values if we are only allowed to skip to the right
    memo4 takes down the values if we are only allowed to be skipping to the left.
    time and space complexity of this would be o(Nd) where N is the number of cities and d is the number of days
    The main concept is to utilize the four different memo to slot in different values
    in order to avoid checking every single city one by one (which would mean that the complexity will become
    N*2D therefore exceeding the complexity). In this case the usage of our memo will only cost ND each will means that
    it will end up as O(ND) at the end of the day.
    :param profit: profit nd matrix given to extract the result
    :param quarantine_time: time needed to quarantine if staying in each cities
    :param home: where we are supposed to start at
    :return: returns the highest number of profit we are able to make
    """
    list = profit
    memo = [[0 for x in range(len(list[0]))] for y in range(len(list))]
    #add base case
    memo.append([0 for x in range(len(list[0]))])
    memo2 = [[0 for x in range(len(list[0]))] for y in range(len(list))]
    memo3 = [[0 for x in range(len(list[0]))] for y in range(len(list))]
    memo4 = [[0 for x in range(len(list[0]))] for y in range(len(list))]

    #building memo list from down to up

    if len(profit) == 1:
        return profit[0][home]

    if len(quarantine_time) <= 2 and len(profit[0]) <= 2:
        total = 0
        for i in range (len(profit)):
            total += profit[i][home]
        return total

    for i in range(len(list) - 1, -1, -1):
        # time and space complexity of this would be o(Nd) where N is the number of cities and d is the number of days
        for j in range(len(list[i])):
            if i == (len(list) - 1):
                memo[i][j] = list[i][j]
                memo2[i][j] = list[i][j]
            #if j is not the first city in the list, since they can only travel to city 1
            elif j == 0:
                memo[i][j] = list[i][j] + memo[i + 1][j]
                if i + quarantine_time[j + 1] + 1 < len(list) - 1:
                    # stay
                    if memo[(i + quarantine_time[j + 1] + 2)][j + 1] > memo[i + 1][j]:
                        # check come from right if available
                        memo[i][j] = list[i][j] + memo[(i + quarantine_time[j + 1] + 2)][j + 1]
                        memo2[i][j] = list[i][j] + memo[(i + quarantine_time[j + 1] + 2)][j + 1]

                if j + 2 < len(list[i]):
                    #checks if its better to skip
                    if i + quarantine_time[j + 2] + 3 < (len(list)):
                        if memo[i + quarantine_time[j + 2] + 3][j + 2] > memo[i + 1][j]:
                            memo[i][j] = list[i][j] + memo[i + quarantine_time[j + 2] + 3][j + 2]
                            memo2[i][j] = list[i][j] + memo[i + quarantine_time[j + 2] + 3][j + 2]


                else:
                    #if not just move right
                    memo[i][j] = list[i][j] + memo[i + 1][j]
                    if memo[i + 2][j + 1] > memo[i][j]:
                        memo[i][j] = memo[i + 1][j + 1]
            #if j is not the last city in the list, since they can only travel to city 2
            elif j == len(list[0]) - 1:
                if i + quarantine_time[j - 1] + 1 < len(list) - 1:
                    memo[i][j] = list[i][j] + memo[i + 1][j]
                    if memo[(i + quarantine_time[j - 1] + 2)][j - 1] > memo[i + 1][j]:
                        # check come from left if available
                        memo[i][j] = list[i][j] + memo[(i + quarantine_time[j - 1] + 2)][j - 1]
                        memo2[i][j] = list[i][j] + memo[(i + quarantine_time[j - 1] + 2)][j - 1]
                else:
                    memo[i][j] = list[i][j] + memo[i + 1][j]
                    if memo[i + 2][j - 1] > memo[i][j]:
                        memo[i][j] = memo[i + 1][j - 1]
            else:
                memo[i][j] = list[i][j] + memo[i + 1][j]
                if i + quarantine_time[j - 1] + 2 < (len(list)):
                    if memo[(i + quarantine_time[j - 1] + 2)][j - 1] > memo[i + 1][j]:
                        memo[i][j] = list[i][j] + memo[(i + quarantine_time[j - 1] + 2)][j - 1]
                        memo2[i][j] = list[i][j] + memo[(i + quarantine_time[j - 1] + 2)][j - 1]


                if i + quarantine_time[j + 1] + 2 < (len(list)):
                    # check if i can come from the right
                    if memo[i + quarantine_time[j + 1] + 2][j + 1] > memo[i + 1][j]:
                        memo[i][j] = list[i][j] + memo[i + quarantine_time[j + 1] + 2][j + 1]
                        memo2[i][j] = memo[i + quarantine_time[j + 1] + 2][j + 1]
                if j + 2 < len(list[i]):
                    #check if skip right is better
                    if i + quarantine_time[j + 2] + 3 < (len(list)) and i != 0:
                        if memo[i + quarantine_time[j + 2] + 3][j + 2] > memo[i + 1][j]:
                            memo[i][j] = list[i][j] + memo[i + quarantine_time[j + 2] + 3][j + 2]
                            memo2[i][j] = list[i][j] + memo[i + quarantine_time[j + 2] + 3][j + 2]
                    elif i + quarantine_time[j + 2] + 3 < (len(list)) and i == 0:
                        # check if skip right is better
                        if memo[i + quarantine_time[j + 2] + 3][j + 2] > memo[i + 1][j]:
                            memo[i][j] = memo[i + quarantine_time[j + 2] + 3][j + 2]
                            memo2[i][j] = memo[i + quarantine_time[j + 2] + 3][j + 2]
                if j - 2 >= 0:
                    # check if skip left is better
                    if i + quarantine_time[j - 2] + 3 < (len(list)):
                        if memo[i + quarantine_time[j - 2] + 3][j - 2] > memo[i + 1][j] and i!= len(list) -1:
                            memo[i][j] = list[i][j] + memo[i + quarantine_time[j - 2] + 3][j - 2]
                            memo2[i][j] = list[i][j] + memo[i + quarantine_time[j - 2] + 3][j - 2]
                        elif memo[i + quarantine_time[j - 2] + 3][j - 2] > memo[i + 1][j] and i== len(list) -1:
                            memo[i][j] = list[i][j] + memo[i + quarantine_time[j - 2] + 3][j - 2]
                            memo2[i][j] = memo[i + quarantine_time[j - 2] + 3][j - 2]

    for i in range (len(memo2[0])-1):
        #checks if memo2 (memo that doesnt allow stay, has higher profits or not).
        # time and space complexity of this would be o(Nd) where N is the number of cities and d is the number of dayss
        if i != len(memo2)-1:
            if quarantine_time[i+1] + 1 < len(memo2):
                if memo2[0][i+1] == 0:
                    memo2[0][i] = memo[quarantine_time[i + 1] + 1][i + 1]
                    if memo2[0][i] > memo [0][i]:
                        memo[0][i] = memo2[0][i]

            if memo[0][i] < memo2[0][i+1] - list[0][i+1]:
                memo[0][i] = memo2[0][i+1]
        if i != 0:
            if memo [0][i] < memo2[0][i-1]:
                memo[0][i] = memo2[0][i-1]


    for i in range(len(list) - 1, -1, -1):
        #creation of memo 3, collects the value if all items were to skip everything up until the last valid option towards the right
        # time and space complexity of this would be o(Nd) where N is the number of cities and d is the number of days
        for j in range(len(list[i])):
            if i == (len(list) - 1):
                memo3[i][j] = list[i][j]
            travel = len(list[0]) - 1 - j
            if i + 1 + travel + quarantine_time[travel + j] < (len(list)):
                memo3[i][j] = list[i][j] + memo[i + 1 + quarantine_time[travel + j] + travel][j + travel]

    for i in range(len(list) - 1, -1, -1):
        #creation of memo4, collects the values if all items were to skip towards the left of the list
        for j in range(len(list[i])):
            if i == (len(list) - 1):
                memo4[i][j] = list[i][j]
            travel = j
            if i + 1 + quarantine_time[0] + travel < len(list) and j != 0:
                memo4[i][j] = list[i][j] + memo[i + 1 + quarantine_time[0] + travel][0]
    #checks if value in memo 3 or memo4 yields higher profits for us compared to out current memo
    # time and space complexity of this would be o(N) where N is the number of cities

    if home == 0:
        #if it does, update it (checks right)
        if memo3[quarantine_time[home+1]][home+1] > memo[0][home]:
            memo[0][home] = memo3[quarantine_time[home+1]][home+1]
        if memo4[quarantine_time[home+1]][home+1] > memo[0][home]:
            memo[0][home] = memo4[quarantine_time[home+1]][home+1]
    elif home == len(list[0]) -1:
        if quarantine_time[home-1] < len(list)-1:
        # if it does, update it (checks left)
            if list[0][home] + memo3[quarantine_time[home-1]][home-1] > memo[0][home]:
                memo[0][home] = memo3[quarantine_time[home-1]][home - 1]
            elif list[0][home] + memo4[quarantine_time[home-1]][home-1] > memo[0][home]:
                memo[0][home] = memo4[quarantine_time[home-1]][home - 1]
    else:

        #if it does, update it (checks both)
            if quarantine_time[home+1]+2 < len(list)-1:
                if quarantine_time[home +1]+2 < len(list) - 1:
                    if list[0][home] + memo3[quarantine_time[home+1]+2][home+1] > memo[0][home]:
                        memo[0][home] = list[0][home]+ memo3[quarantine_time[home+1]+2][home+1]
                    if list[0][home] + memo4[quarantine_time[home + 1] + 2][home + 1] > memo[0][home]:
                        memo[0][home] = list[0][home] + memo4[quarantine_time[home + 1] + 2][home + 1]

            if quarantine_time[home - 1] + 2 < len(list) - 1:
                if list[0][home] + memo3[quarantine_time[home-1]+2][home-1] > memo[0][home]:
                    memo[0][home] = list[0][home]+ memo3[quarantine_time[home-1]+2][home - 1]
                if list[0][home] + memo4[quarantine_time[home-1]+2][home-1] > memo[0][home]:
                    memo[0][home] = list[0][home]+ memo4[quarantine_time[home-1]+2][home - 1]


    return memo[0][home]







