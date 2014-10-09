#!/usr/bin/env python

from sys import argv
import random, string

def make_chains(corpus, num):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    new_corpus = "" 
    
    for char in corpus:

        # leave out certain kinds of punctuation
        if char in "_*": # NOT WORKING DELETE THIS or char == "--":
            continue
        
        # put everything else in the new_corpus string      
        else:
            new_corpus += char

    list_of_words = new_corpus.split()

    d = {}

    
    for i in range( (len(list_of_words) - num) ):
        prefix = []
        
        for j in range(num):
            prefix.append(list_of_words[i + j])
        prefix = tuple(prefix)
        
#        prefix = (list_of_words[i], list_of_words[i+1], list_of_words[i+2])
        suffix = list_of_words[i+num] 

        if prefix not in d:
            d[prefix] = [suffix]  # initializes the suffix as a list
        else:
            d[prefix].append(suffix)
    return d
        
def make_text(chains, num):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # create a list of chain's keys, then return one of the keys at random
    random_prefix = random.choice(chains.keys())

    # from the list of values for the chosen key, return one value at random
    random_suffix = random.choice(chains[random_prefix])
    
    # initialize an empty string for our random text string
    markov_text = ""

    # iterate over prefix's tuple and add each word to the random text string
    for word in random_prefix:
        markov_text += word + " "

    # then add the suffix
    markov_text += random_suffix + " "

    # rename random_prefix and random_suffix so that we can call them
    # in a the following for loop
    prefix = random_prefix
    suffix = random_suffix

    for i in range(100):

        # create a new prefix from the last items in the most recent prefix and
        # the most recent suffix
        newprefix = []

        for j in range(1, num):
            newprefix.append(prefix[j])
        newprefix.append(suffix)
        prefix = tuple(newprefix)

        # choose a random suffix from the new prefix's values
        suffix = random.choice(chains[prefix])

        # add it all to the random text string
        markov_text += "%s " % (suffix)

    return markov_text
#### TO DO: FIX TWEETMASH ######
def tweetmash(markov_text):
    oneforty = ""
    while len(oneforty) < 140:
        for char in markov_text:
            oneforty += char
    words = oneforty.split()

    for word in words:
        if not word.istitle():
            continue
    print oneforty
###########################

def main():
    script, filename1, filename2, num = argv
    num = int(num)
    fin1 = open(filename1)
    input_text = fin1.read()
    fin2 = open(filename2)
    input_text += fin2.read()
    fin1.close()
    fin2.close()


    chain_dict = make_chains(input_text, num)
    random_text = make_text(chain_dict, num)
    random_tweet = tweetmash(random_text)
    print random_tweet



if __name__ == "__main__":
    main()