import string
from dictionary import Dictionary
from hash_table import LinearProbeHashTable
from enum import Enum
from typing import Tuple
from list import ArrayList
import sys

sys.setrecursionlimit(9999)

class Rarity(Enum):
    """Initializes the rarity class with enum classes so that those symbolic names (Mispelt, Common, Uncommon and Rare)
     will have a constant value bound to it so 1 ,2 ,3 ,4 respectively """
    MISSPELT = 1
    COMMON = 2
    UNCOMMON = 3
    RARE = 4

class Frequency:

    def __init__(self):
        """initializes the frequency class just like the ones in the dictionary method"""
        self.hash_table = LinearProbeHashTable (250726, 1000081)
        self.dictionary = Dictionary (250726, 1000081)
        self.dictionary.load_dictionary ("english_large.txt")
        self.max_word = (" ",0)

    def add_file (self,filename:str) -> None:
        """
        This method is used to create the hash_table for other files depending on what filename is inserted. It will
        first read the source file and then insert each and every one of the words into the hash_table while recording
        the total amount of times each words were inserted. The precondition for this would be that the filename must
        always be in string form or else this method will not work. This method will not return anything and its only
        function is just to convert everything from the file into hash_table
        """
        def remove_all_punc (word:str):
            punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            x = str(word)
            for i in x:
                if i in punctuation:
                    x = x.replace(i, " ")
            return x
        f = open (filename, encoding= "utf-8")
        for line in f:
            line = line.rstrip()
            for word in line.split():
                word = remove_all_punc(word)
                if word is not None:
                    word = word.lower()
                    if self.dictionary.hash_table.__contains__(word):
                        if self.hash_table.__contains__(word):
                            counter = self.hash_table.__getitem__(word) + 1
                            if counter >= self.max_word[1]:
                                self.max_word = (word, counter)
                            self.hash_table.__setitem__(word,counter)
                        else:
                            self.hash_table.__setitem__ (word,1)
        f.close()

    def rarity (self,word:str) -> Rarity:
        """This method is used to count and get us what rarity level each word is. They will be classified into the four
            main enum classes that we have initialized above and will return the value based on the ones that we
            assigned above. The expected return of this method would be the enumeration that represents what rarity level
            the specific word is.
        """
        maximum_value = self.max_word[1]
        if self.hash_table.__getitem__(word.lower()) >= (maximum_value / 100):
            return Rarity.COMMON
        elif self.hash_table.__getitem__(word.lower()) < (maximum_value /100):
            return Rarity.RARE
        elif self.hash_table.__getitem__(word.lower()) < (maximum_value /100) and self.hash_table.__getitem__(word.lower()) >= (maximum_value/1000):
            return Rarity.UNCOMMON
        else:
            return Rarity.MISSPELT

    def partition (self,list):
        """Partition method needed to make quick_sort work."""
        pivot = list[0][1]
        swap_pos = 1
        x = 1
        while x < len(list):
            if list[x][1] > pivot:
                list[x], list[swap_pos]= list[swap_pos], list[x]
                swap_pos = swap_pos + 1
            x += 1
        list [0], list[swap_pos -1 ] = list [swap_pos -1], list [0]
        return swap_pos - 1

    def quick_sort (self,list):
        """ Code adapted and modified from FIT1045 Lecture 16. This method uses quicksort to allow us to sort the ArrayList
            recursively. Recursion limit was set to 1000000 to prevent it from hitting the limit when sorting the ArrayList.
            The ArrayList from above is passed into this method where it will return the sorted list.
            complexity: O(n^2)
        """
        if len(list) <= 1:
            return list
        pivot_pos = self.partition(list)
        pivot = list[pivot_pos]
        sorted_right = self.quick_sort(list[pivot_pos + 1:])
        sorted_left = self.quick_sort(list[:pivot_pos])
        return sorted_left + [pivot] + sorted_right

    def ranking(self) -> ArrayList[Tuple]:
        """This method will take in an ArrayList (not a python list as stated in the assignment) and will then sort the
            list based on the amount of times that each words appear. The expected return will be the sorted ArrayList
            (using quicksort) in descending order.
        """
        my_array_list = ArrayList(self.hash_table.__len__())
        index = 0
        for x in range(self.hash_table.table.__len__()):
            if self.hash_table.table[x] is not None:
                my_array_list.__setitem__(index, self.hash_table.table[x])
                index += 1
        return self.quick_sort(my_array_list.array)

def frequency_analysis () -> None:
    """
    This will ask the users for the amount of rankings that the user wants and will utilise the ranking method above to
    return the ranking, frequency of the word appearing and the rarity level.
    :return: The list of rankings that the user asks for
    """
    freq = Frequency()
    boolean = True
    freq.add_file("84-0.txt")
    ranking = freq.ranking()
    print("Enter number of rankings")
    while boolean is True:
        number = input()
        try:
            val = int (number)
        except ValueError:
            print(' This is not a number ')
            break
        try:
            for x in range (int(number)):
                print ("The Ranking for the word selected {"+str(ranking[x][0])+"} is "+ str(x+1))
                print ("The amount of times that it has appeared inside the file is "+str(ranking[x][1]))
                print ("The rarity rating of the word would be " + str(freq.rarity(str(ranking[x][0]))))
            boolean = False
        except IndexError:
            boolean = False


if __name__ == "__main__":
    frequency_analysis()




















        