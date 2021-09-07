"""Name: Darren Yee Jer Shien
   Student ID: 31237223
   Assignment Name: FIT 1008 Interview Practical 3
   Task 1 / Task 2 """
from referential_array import ArrayR
import time
import timeit
from typing import Tuple
from hash_table import LinearProbeHashTable


class Dictionary:

    def __init__(self , hash_base : int , table_size: int) -> None:
        """initializes the dictionary class and creates a hash table based on hash_base and table_size
           does not expect any returns since it only initializes the data available
        """
        self.hash_base = hash_base
        self.table_size = table_size
        self.hash_table = LinearProbeHashTable(self.hash_base, self.table_size)
        self.time_taken = 0

    def load_dictionary (self, filename: str, time_limit: int = None) -> int:
        """reads a file and adds the words into hash table, sets the encoding to utf-8 as mentioned in the assignment
           timeit function is also used to record the amount of time taken so that it does not exceed the amount of time
           that time_limit sets (optional)
           The expected return for this would be an integer that represents the amount of words that were added into the
           table
        """
        f = open(filename, encoding="utf-8")
        number = 0
        start = 0
        end = 0
        for line in f:
            line = line.rstrip()
            try:
                if time_limit is None or time_limit > self.time_taken:
                    start += timeit.default_timer ()
                    self.add_word(line)
                    end += timeit.default_timer ()
                    self.time_taken = self.time_taken + (end - start)
                    number += 1
                    start = 0
                    end = 0
                else:
                    raise TimeoutError
            except TimeoutError:
                break
        f.close()
        return number

    def add_word(self, word:str) -> None:
        """adds given word to Hash Table after converting to lower case. Uses the method set item defined in hash_
        table
        """
        word = word.lower()
        self.hash_table.__setitem__(word,1)

    def find_word (self,word:str) -> bool:
        """Checks if word is inside dictionary. Will return True if it is. Uses the method contains defined in hash_
        table
        """
        if type(word) == str:
            word = word.lower
            return self.hash_table.__contains__(word)

    def delete_word (self, word:str) -> None:
        """deletes a given word from the hash table after converting it to lower case. Uses the method defined in hash_
        table
        """
        if type(word) == str:
            word = word.lower
            return self.hash_table.__delitem__(word)

    def menu(self) -> None:
        """gives users a menu to choose which operation they want the program to do. Will display 5 options that
           includes read file, add word, find word delete word and exit. The menu will then prompt the users to
           input what things that they
        """
        boolean = True
        while boolean is True:
            print("1. Read File")
            print("2. Add Word")
            print("3. Find Word")
            print("4. Delete Word ")
            print("5. Exit")
            print("Enter Option")
            a = input()
            if a == "1":                                                                                                #does the operation according to what the user asks for
                print ("Enter Filename:")
                b = input()
                if b is None:
                    raise TypeError
                self.load_dictionary(str(b))
                print ("File successfully added")
            elif a == "2":
                print("Enter Word:")
                b = input ()
                if b is None:
                    raise TypeError
                self.add_word(str(b))
                print (str(b)+" has been successfully added")
            elif a == "3":
                print("Enter Word:")
                b = input()
                if b is None:
                    raise TypeError
                self.find_word(b)
                if self.find_word(b) is True:
                    print (str(b)+" found in dictionary")
                else:
                    print (str(b)+" not found in dictionary")
            elif a == "4":
                print("Enter Word:")
                b = input()
                if b is None:
                    raise TypeError
                self.delete_word(str(b))
                print (str(b + " has been successfully deleted"))
            elif a == "5":
                break
            else:
                print ("Invalid Option")

class Statistics:
    "creates a new class statistics"

    def load_statistics (self, hash_base: int, table_size:int, filename:str,max_time:int ) -> tuple:
        """creates new dictionary with hash_base and table_size and then returns a tuple containing words, time, collision_count, probe_total, probe_max, rehash_count"""
        dict = Dictionary(hash_base, table_size)
        dict_words = dict.load_dictionary(filename, max_time)
        return (dict_words, dict.time_taken) + dict.hash_table.statistics()


    def table_load_statistics (self,max_time):
        """used to print stats for 3 files included in prac"""
        files = ["english_small.txt", "english_large.txt", "french.txt"]
        Table_Size = [250727,402221,1000081]
        base = [1,27183,250726]
        f = open("output_task2.csv","w")
        f.write("Filename" + "," + "Table Size" + "," + "Hash Base" + "," + "Words" + "," + "Time" + "," +"Collision Count" + "," + "Total Probe" + "," + "Probe Max"+ "," + "Rehash Count"+"\n")
        for i in files:
            if len(Table_Size) < 3:
                raise ValueError
            for j in range(len(Table_Size)):
                if len(base) < 3:
                    raise ValueError
                for k in range(len(base)):
                    f.write (i +"," + str(Table_Size[j]) + "," +str(base[k])+","+"," .join(map(str,self.load_statistics(base[k], Table_Size[j], i, max_time)))+"\n")

        f.close()

if __name__ == "__main__":
    "uses the most optimal pair as found in the graph"
    dictionary = Dictionary(250726,1000081)
    dictionary.menu()

#a = Statistics ()
#Statistics.table_load_statistics(a,10)