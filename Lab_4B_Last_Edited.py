# -*- coding: utf-8 -*-
"""
Created on Mon Nov 5 21:05:46 2018

@author: Ricardo
"""
# Course: CS2302
# Author: Ricardo Godoy
# Assignment: Lab 4 B
# T.A: Saha, Manoj
# Instructor: Diego Aguirre
# Date of last modification: 11/11/18


# This program reads a file that contains all english words and inserts them into a hash table, selected
# by the user. The program prints the anagrams of a specific word, only if it is in the hash table.
# Along with that, the program also computes the word with the most number of anagrams and the
# number of anagrams of each word


# HashTable class using chaining.
class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=26):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
      
    # Inserts a new item into the hash table.
    def insert(self, item):
        # get the bucket list where this item will go.
        bucket = (ord(item[:1].lower())-97) % len(self.table)
#        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        bucket_list.append(item.lower())
         
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = (ord(key[:1].lower())-97) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        if key in bucket_list:
            # find the item's index and return the item that is in the bucket list.
            item_index = bucket_list.index(key)
            return bucket_list[item_index]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)
            
    def avg_comparisons(self):
        count = 0
        for i in range(len(self.table)):
            count += len(self.table[i])
        return str(sum / len(self.table))
    
    def load_factor(self):
        return self.size / len(self.tableq)

class Counter:
    
    
    def __init__(self):
        self.count = 0         
            
#####################################################################################
def create_hash(filename):
    english_words = HashTable()
    with open (filename) as file:
        for line in file:
            ln = line.lower()
            english_words.insert(ln.replace("\n", ""))


    return english_words

def count_anagrams(obj, word, prefix=""):
    #Counts the anagrams found in the tree
          
    if len(word) <= 1:
        str = prefix + word
        if english_words.search(str):
            obj.count = obj.count + 1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated.
                count_anagrams(obj, before + after, prefix + cur)  
    return obj.count
            
def max_anagrams(obj, filename):
    #Computes the word with the maximum number of anagrams
    file = open(filename)
    max_count = 0
    max_word = ""
    
#    num_words = 4
    for line in file:
        obj = Counter()
        obj.count = count_anagrams(obj, line.replace("\n", ""))  # -1 index means last one
#        print(line[0:-1], obj.count)
#        print(obj.count)
        if obj.count > max_count:
            max_count = obj.count
            max_word = line.replace("\n", "")
            
    print("Word with more anagrams: " + max_word)
    print("Max number of anagrams: " + str(max_count))
            
def print_anagrams(word, prefix=""): 
    #Prints the anagrams of a specific word
    if len(word) <= 1:
        str = prefix + word

        if english_words.search(str):
            print(prefix + word)
            
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur 
            after = word[i + 1:] # letters after cur
            
            if cur not in before: # Check if permutations of cur have not been generated. 
                print_anagrams(before + after, prefix + cur)
            
        

def main():
    global english_words
    english_words = HashTable()
    file = "words_short.txt"
    
    size = input("Enter the size of the table: ")
    english_words = HashTable(int(size))
    english_words = create_hash(file) 
    
    anagram_word = input("Which word do you want to permutate? ")
    print_anagrams(anagram_word)
    

    
main()