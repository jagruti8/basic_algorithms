# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 08:12:25 2020

@author: JAGRUTI
"""


## Represents a single node in the Trie

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.data = ""
        # English letter has 26 alphabets
        self.next = [None for _ in range(26)]
        # to check if a node represents a word
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        # to make the trie case-insensitive
        if 65<=ord(char)<=90:
            char = chr(ord(char)+32)
        index = ord(char) - 97
        # insert node at the index corresponding to that letter like index for a is 0, b is 1, c is 2 and so, on
        self.next[index] = TrieNode()
        # add data to child node
        self.next[index].data += char
        return self.next[index]
    
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point

        # list of words with the suffix
        list_words = []
         
        # loop through the node's children to find the list of suffices
        for index in self.next:
            # if child exists
            if index is not None:
                # move node to child
                node = index
                # add data at child
                word = suffix + index.data
                # recurse through ".suffixes()" to traverse the entire depth of that node and get a list of words
                list_words_recursion = index.suffixes(word)
                # if node represents a word, add it to the existing list obtained from recursion 
                if index.is_word:
                    list_words_recursion.append(word)
                # add list of words obtained from recursion to list of words in the present execution call
                list_words += list_words_recursion 
        # return list of words obtained in this execution
        return list_words
            
## The Trie itself containing the root node and insert/find functions

class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        
        if len(word) == 0:
            print("Error!\nNo word for insertion\nPlease insert a word")
            return
        
        # traverse the trie strating from root
        node = self.root
        for index, char in enumerate(word):
            
            # to make case-insensitive
            ascii_value = ord(char)
            if 65<=ascii_value<=90:
                ascii_value += 32
            ascii_value -= 97
            
            # if character is not added to node's children break from the loop  
            # insert the word from that character onwards as written in the while loop below
            if node.next[ascii_value] is None:
                break
                
            # if character is added to node's children, shift to the child node
            node = node.next[ascii_value]
            
        # insert the word 
        while(index<len(word)):
            char = word[index]
            node = node.insert(char)
            index += 1
        # the last node represents a word
        node.is_word = True
                           
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        
        # traverse from the root
        node = self.root
        for index, char in enumerate(prefix):
            
            # to make case-insensitive
            ascii_value = ord(char)
            if 65<=ascii_value<=90:
                ascii_value += 32
            ascii_value -= 97
            
            # return "None" if character is not added to node's children
            if node.next[ascii_value] is None:
                return None
            node = node.next[ascii_value]
            
        return node
    
# The below implementation is a mixture of both edge cases and normal cases
## 1
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
prefixes = ['', 't', 'tr', 'a', 'p', 'an', 'fun', 'o']
for prefix in prefixes:
    node = MyTrie.find(prefix)
    if node:
        list_of_words = node.suffixes()
        print("prefix: {}, suffixes: {}".format(prefix, list_of_words))
    else:
        print("prefix: {} does not exist".format(prefix))

## Output for above implementation       
"""
prefix: , suffixes: ['antagonist', 'anthology', 'antonym', 'ant', 'factory', 'function', 'fun', 'trie', 'trigger', 'trigonometry', 'tripod']
prefix: t, suffixes: ['rie', 'rigger', 'rigonometry', 'ripod']
prefix: tr, suffixes: ['ie', 'igger', 'igonometry', 'ipod']
prefix: a, suffixes: ['ntagonist', 'nthology', 'ntonym', 'nt']
prefix: p does not exist
prefix: an, suffixes: ['tagonist', 'thology', 'tonym', 't']
prefix: fun, suffixes: ['ction']
prefix: o does not exist
"""

## 2
MyTrie = Trie()
wordList = []
for word in wordList:
    MyTrie.insert(word)
prefixes = ['', 't', 'tr', 'a', 'p', 'an', 'fun', 'o']
for prefix in prefixes:
    node = MyTrie.find(prefix)
    if node:
        list_of_words = node.suffixes()
        print("prefix: {}, suffixes: {}".format(prefix, list_of_words))
    else:
        print("prefix: {} does not exist".format(prefix))

## Output for above implementation  
"""
prefix: , suffixes: []
prefix: t does not exist
prefix: tr does not exist
prefix: a does not exist
prefix: p does not exist
prefix: an does not exist
prefix: fun does not exist
prefix: o does not exist
"""

## 3
MyTrie = Trie()
wordList = ["", "", ""]
for word in wordList:
    MyTrie.insert(word)
    
## Output
"""
Error!
No word for insertion
Please insert a word
Error!
No word for insertion
Please insert a word
Error!
No word for insertion
Please insert a word
"""
prefixes = ['', 't', 'tr', 'a', 'p', 'an', 'fun', 'o']
for prefix in prefixes:
    node = MyTrie.find(prefix)
    if node:
        list_of_words = node.suffixes()
        print("prefix: {}, suffixes: {}".format(prefix, list_of_words))
    else:
        print("prefix: {} does not exist".format(prefix))

## Output for above implementation
"""
prefix: , suffixes: []
prefix: t does not exist
prefix: tr does not exist
prefix: a does not exist
prefix: p does not exist
prefix: an does not exist
prefix: fun does not exist
prefix: o does not exist
"""

## 4
import random

MyTrie = Trie()
wordList = []
word = "abcdefghijklmnopqrstuvwxyz"
for i in range(10):
    list_word = []
    for j in word:
        list_word += [j for i in range(i)]
    random.shuffle(list_word)
    list_word1 = ''.join(list_word)  
    wordList.append(list_word1)
    
for word in wordList:
    MyTrie.insert(word)
    
## Output
"""
Error!
No word for insertion
Please insert a word
"""

prefixes = ['', 't', 'tr', 'a', 'p', 'an', 'fun', 'o']
for prefix in prefixes:
    node = MyTrie.find(prefix)
    if node:
        list_of_words = node.suffixes()
        print("prefix: {}, suffixes_length: {}".format(prefix, len(list_of_words)))
    else:
        print("prefix: {} does not exist".format(prefix))
        
## Output - The below may show different values for different runs due to random.shuffle
"""
prefix: , suffixes_length: 9
prefix: t does not exist
prefix: tr does not exist
prefix: a does not exist
prefix: p, suffixes_length: 1
prefix: an does not exist
prefix: fun does not exist
prefix: o does not exist
"""
