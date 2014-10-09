#!/usr/bin/env python

from sys import argv
import random, string



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    new_corpus = "" 
    
    for char in corpus:

        # leave out certain kinds of punctuation
        if char in "_[]*" or char == "--":
            continue
        
        # put everything else in the new_corpus string      
        else:
            new_corpus += char

    list_of_words = new_corpus.split()

    d = {}
    for i in range( (len(list_of_words) - 2) ):

        prefix = (list_of_words[i], list_of_words[i+1])
        suffix = list_of_words[i+2] 
        
        if prefix not in d:
            d[prefix] = [suffix]  # initializes the suffix as a list
        else:
            d[prefix].append(suffix)

    # add link from end of wordlist to beginning of wordlist
    prefix = (list_of_words[-2], list_of_words[-1])
    suffix = list_of_words[0]
    d[prefix] = suffix

    return d

def make_text(chains):
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

    for i in range(1000):

        # create a new prefix from the last item in the old prefix and
        # the last suffix
        prefix = (prefix[1], suffix)

        # choose a random suffix from the new prefix's values
        suffix = random.choice(chains[prefix])

        # add it all to the random text string
        markov_text += "%s " % (suffix)

    return markov_text

def main():
    script, filename = argv
    fin = open(filename)
    input_text = fin.read()
    fin.close()


    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text




if __name__ == "__main__":
    main()