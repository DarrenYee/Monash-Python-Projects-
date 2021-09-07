"""
Name: Darren Yee Jer Shien
StudentID: 31237223
FIT2004 Assignment 3
"""
#Assignment Q1
class Node:
    def __init__(self, word=0, freq = 0,prev = 0,fake_link=None):
        """
        This initializes the Node class for Q1, Called every time a new node is to be created (aka there is a branch).
        By utilizing all the payload saved here, we can ensure that we do not exceed the complexity of query when comparing
        lexicographical order.
        Time complexity = O(1) since we only assign values here and create a constant size [None]*5 in the
        self.link param.
        :param word: saves the word in the node
        :param freq: saves the frequency of the word in the node
        :param prev: The current smallest index of branch
        :param fake_link: fake_link that links to the best result when queried on this specific node
        """
        self.link = [None] * 5
        self.fake_link = fake_link
        self.prev = prev
        self.word = word
        self.freq = freq

class SequenceDatabase:
    """
    SequenceDatabase class that helps the create the trie needed in order to store and query the words
    """
    def __init__(self,best=False):
        """
        Initializes the root of the trie by creating a new node using the Node class.
        :param best: checks whether a branch occurs.
        """
        self.best = best
        self.root = Node()

    def finder(self, cur, b):
        """
        Helper function to check whether each node is either: a) has a larger frequency, b) has the same frequency but
        lexicographically smaller, or c) whether it is the same lexicographical ranking and self.best is true (aka
        branch has occured.
        The time complexity is O(len(s)) since all the operations are just assignment and comparisons which are O(1)
        :param cur: current node that we are checking
        :param b: the node that we are parsing up from the recursion
        :return: returns b node back
        """
        if cur.freq < b.freq:
            #if it has a higher freq, update the fake_link to the b node that is parsed from the recursion
            cur.fake_link = b
            cur.prev = cur.index
            cur.freq = b.freq
        elif cur.index < cur.prev and b.freq == cur.freq:
            #if the prev index is bigger than the cur (lexicographically larger), update the fake_link to the node that is
            #parsed from the recusion
            self.best = True
            cur.fake_link = b
            cur.prev = cur.index
            cur.freq = b.freq
        elif cur.index == cur.prev:
            # if the word at the current index is lexicographically equal, check if self,best is true(aka branched)
            # if it is, update the fake_link to b
            if self.best is not False:
                cur.fake_link = b
                cur.prev = cur.index
                cur.freq = b.freq
        else:
            self.best = False
        return b

    def addSequence(self, word):
        """
        Addes the word into the trie, done using recursion in order to parse up information.
        Time complexity = O(len(q)) where q is the word that we are adding
        :param word: the word that we are trying to add into the trie
        """
        cur = self.root
        self.best = False
        b = self.insert_recur_aux(cur, 0, word)
        self.finder(cur, b)

    def insert_recur_aux(self, cur, i, word):
        """
        Auxiliary function that adds each character of i into the trie. Will call itself up until the point where i+1
        (a) is equals to len(word) which represents that all characters inside of the word has been added into the trie.
        :param cur: current node
        :param i: index of the character that we are adding
        :param word: the word that we are adding
        :return: returns b before i is equals to the length of the word, else it will return the current node.
        """
        if i == len(word):
            index = 0
            if cur.prev is None:
                #sets the current index as the previously smallest lexicographical index if it is None
                cur.prev = index
            if cur.link[index] is not None:
                # if it has been traversed before, add the frequency by one, this means that the word already exists in
                # the trie
                cur = cur.link[index]
                cur.link[index] += 1
                cur.index = index
                cur.freq = cur.link[index]
            else:
                if cur.prev is None:
                    # sets the current index as the previously smallest lexicographical index if it is None
                    cur.prev = index
                #if it hasn't been traversed before, create a new branching node and set the frequency to 1
                cur.index = index
                cur.link[index] = Node()
                cur = cur.link[index]
                cur.index = index
                cur.word = word
                cur.link[index] = 1
                cur.freq = cur.link[index]
            return cur
        else:
            cur.index = ord(word[i]) - 65 + 1
            if cur.prev is None:
                #sets the current index as the previously smallest lexicographical index if it is None
                cur.prev = ord(word[i]) - 65 + 1
            if cur.link[cur.index] is not None:
                #if it is not none, it means that it has been traversed before so we dont have to create a new branching
                #node
                #Calls finder helper on cur and b
                cur = cur.link[cur.index]
                cur.word = word
                a = i + 1
                if a == len(word):
                    cur.index = 0
                b = self.insert_recur_aux(cur, a, word)
                return self.finder(cur, b)
            else:
                #if it hasn't been traversed before, create a new branching node.
                #Calls the finder helper on cur and b
                self.index = cur.index
                if cur.prev is None:
                    cur.prev = ord(word[i]) - 65 + 1
                cur.link[cur.index] = Node()
                cur = cur.link[cur.index]
                cur.word = word
                a = i + 1
                b = self.insert_recur_aux(cur, a, word)
                return self.finder(cur, b)

    def query(self, word):
        """
        Traverses through the node and returns the fake_link of the word that we are looking for.
        Time comeplxity = O(len(s)) where s is the word that we are looking for
        :param word: word that we are querying
        :return: returns word contained in the fake_link of the node that we have traversed to.
        """
        cur = self.root
        for char in word:
            index = ord(char) - 65 + 1
            if cur.link[index] is not None:
                cur = cur.link[index]
            else:
                return None
        if cur.fake_link is not None:
            return cur.fake_link.word


class OrfFinder:
    def __init__(self,word):
        """
        Initializes two Tries. One for prefix and one for suffix. This is used in order for us to be able to find all
        the possible word within the suffix and prefixes without exceeding the required complexity.
        The complexity of this would be O(N2) where n is the length of the genome since we are adding the words twice,
        once iterating from the end of the string and the other from the start.
        The attribute self.prefix.pre tells the program to choose whether to insert it from front to back or back to
        front.
        :param word: the genome String
        """
        self.prefix = Genome()
        self.original_word = word
        self.suffix = Genome()
        self.prefix.pre = True
        self.prefix.addGenome(word)
        self.prefix.pre = False
        self.suffix.addGenome(word)

    def find(self, prefix, suffix):
        """
        First we do a search on the prefix trie and then we reverse the suffix and search it in the suffix trie.
        If we what we found from either of the tries are empty, we return [] which means it is an invalid input. Else
        we will loop through the possible index and slice the original word before adding it into the result list. Once
        All of this is done, we will then return the result list.
        The time complexity is ((len(start)+len(end)+U) where U is the number of characters in the output list since it
        is bounded by the slicing action to get the output.
        :param prefix: prefix that we are looking for
        :param suffix: suffix that we are looking for
        :return:
        """
        #search prefix in pre
        pre = self.prefix.search(prefix)
        #search suffix in sur after reversing it
        suf = self.suffix.search(suffix[::-1])
        result_list = []
        # if len == 0 means it is invalid
        if len(pre) == 0 or len(suf) == 0:
            return result_list
        #loop through the index and append the once with valid index into the result list
        for i in range (len(pre)):
            for j in range (len(suf)):
                #checks if either the prefix is smaller than the difference between original word length and suffix and also
                #whether the index of suf[i] - pre[j] is larger or equals to the total length of both suffix and prefix combined
                #which would represent a valid input.
                if pre[i] <len(self.original_word) - len(suffix) and pre[i] < suf[j]-1 and suf[j] - pre[i] >= len(prefix)+len(suffix):
                    result_list.append(self.original_word[pre[i]:suf[j]])
        return result_list

class Node_Q2:
    def __init__(self):
        """
        :param link: A fixed size array that allows for all the possible branches and its index A,B,C,D and the terminal
        word is an empty list that allows us to append all the possible start or end index into the list
        The time complexity of this is O(1) since we are creating a fixed sized array along with an empty list.
        """
        # terminal $ at index 0 along with the four different alphabets ABCD.
        self.link = [None] * 5
        self.word = []

class Genome:
    def __init__(self,word = None,pre = False):
        """
        Time complexity of this is O(1) since we are only creating the root node and binding variables.
        :param word: the word
        :param pre: Determines whether we need to add in from front to back (prefix) or back to front (suffix)
        """
        # root does not save anything.
        self.root = Node_Q2()
        self.word = word
        self.pre = pre

    def addGenome(self, word):
        """
        If self.pre is true, we will add the words in starting from index i up to len(word)-1 which will give us all the
        possible prefixes. On the other hand, if self.pre is false, we will add it from the index [len(word)] all the
        way back to 0 which gives us all the possible sufixes of the word.
        The time_complexity of this would be O(N2) where N is the length of the genome.
        :param word: word that we are adding
        :return:
        """
        cur = self.root
        self.k = 0
        self.suffix = False
        if self.pre == True:
            for i in range (len(word)):
                self.index = i
                self.insert_recur_aux(cur, i, word,len(word)-1)
        else:
            for j in range (len(word),0,-1):
                self.suffix = True
                self.index = j
                self.insert_recur_aux(cur, j-1, word,0)

    def insert_recur_aux(self, cur, i, word,end):
        """
        Same implementation as q1. But we set the ending point ourselves when calling it instead of it just ending at
        index 0. By doing this, it allows us to be able to add in all the possible prefix and suffix without needing to
        slice the word at the start which would add a lost of unnecessary complexity.
        The time complexity of this is O(n) where n is the length of the word that we are adding in.
        :param cur: cur node
        :param i: starting point
        :param word: word that we are adding
        :param end: ending point
        :return:
        """
        if i == end:
            index = 0
            if cur.link[index] is not None:
                cur = cur.link[index]
                cur.word.append(self.index)
            else:
                cur.link[index] = Node_Q2()
                cur = cur.link[index]
                cur.word.append(self.index)
            return
        else:
            index = ord(word[i]) - 65 + 1
            if cur.link[index] is not None:
                cur = cur.link[index]
                cur.word.append(self.index)
            elif cur.link[index] is None:
                cur.link[index] = Node_Q2()
                cur = cur.link[index]
                cur.word.append(self.index)
            if self.suffix == True:
                a = i-1
            else:
                a = i + 1
            self.insert_recur_aux(cur, a, word,end)


    def search(self, word):
        """
        Similar search method as Q1, but this will return [] if the prefix or suffix is not valid.
        The time complexity is O(len(n)) where n is the prefix/suffix we are adding in.
        :param word: the prefix or suffix that we are looking for
        :return:
        """
        cur = self.root
        for char in word:
            index = ord(char) - 65 + 1
            if cur.link[index] is not None:
                cur = cur.link[index]
            else:
                return []
        return cur.word


