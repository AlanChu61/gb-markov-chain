"""Generate Markov text from text files."""

from random import choice
import sys
import string


def open_and_read_file(file_path):
    # Beacsue we do input_path = sys.argv[1:]
    # so file_path is a list
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = ""
    for file in file_path:
        contents += open(file).read()

    return contents


def make_chains(text_string, size):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # 1 split the string
    text_list = text_string.strip().split()
    # 2 iterate the list and find something added to dict
    chains = {}

    for i in range(0, len(text_list)-size):
        #key = (text_list[i],text_list[i+1])
        # for loop -> size
        key = tuple(text_list[i:i+size])
        # print('key:',key)
        # chains[key] =chains.get(key,[]).append(text_list[i+2])
        if chains.get(key) == None:
            chains[key] = [text_list[i+size]]
        else:
            chains[key].append(text_list[i+size])

    # print('chains:',chains)
    # print('-----')
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    # words_keys = list(chains.keys())

    # if ('Would', 'you') in list(chains.keys()):
    #     current_key = ('Would', 'you')
    # elif ('Four', 'score') in list(chains.keys()):
    #     current_key = ('Four', 'score')
    # else:
    #     print("Wrong file!")
    current_key = list(chains.keys())[0]
    # print('Current_key:',current_key)
    words.extend(list(current_key))
    while True:
        try:
            first_value = choice(chains[current_key])
            words.append(first_value)  # add new value into words list
            # print(first_value)
            if first_value[-1] in string.punctuation:
                return " ".join(words)
            new_key = (current_key[-1], first_value)
            current_key = new_key
        except KeyError:
            return " ".join(words)

    """
     >> Would you could you with a fox?(stop here?) Would you like them, Sam I am?
    regex
    if word[-1] in '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
    word[-1] = true: stop 
    """

    # words= ['whoud', "you"]
    # dict['whoud', "you"]=['and','hello'] (random choict) # hello
    # words= ['whoud', "you",'hello']
    # 1) keys = last two terms -> chains[keys]
    # 2) add the value to the words[]
    # 3) keep take last two terms from list ->step 1

    # ('whoud', "you") = ['and','hello'])
    # you + add
    # 1 current_key
    # 2 find something from current_key's value(random.choice) here
    # 3 current[-1] + current_key's value = new_key
    # 4 Go back to step 1 ...

    # last step join the list into a string

    # your code goes here


# input_path = 'gettysburg.txt'
input_path = sys.argv[1:]
# python3 markov.py abc.txt bcd.txt
# ['abc.txt','bcd.txt']

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
size = int(input("Enter n from grams?"))
chains = make_chains(input_text, size)

# Produce random text
random_text = make_text(chains)

print('random text: ', random_text)
