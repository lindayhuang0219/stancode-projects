"""
File: anagram.py
Name: Linda
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

words = []  # This is the list of an English dictionary
count = 0   # the number of anagrams for the word input by user


def main():
    """
    This program recursively finds all the anagram(s) for the word input by user and terminates when the
    input string matches the EXIT constant.
    """
    print(f'Welcome to stanCode "Anagram Generator\" (or {EXIT} to quit)')
    read_dictionary()
    word_input = str(input('Find anagrams for: '))
    print('Searching...')
    find_anagrams(word_input.lower())
    print(f'Welcome to stanCode "Anagram Generator\" (or {EXIT} to quit)')


def read_dictionary():
    """
    read file "dictionary.txt" stored in FILE and appends words in each line into a Python list
    """
    global words
    with open(FILE, 'r') as f:
        for line in f:
            words.append(line.strip())


def find_anagrams(s):
    """
    finds all the anagram(s) for the word input by user and print on the console
    :param s: the word input by user
    """
    word_list = sorted(s)
    anagrams_list = []
    find_anagrams_helper(word_list, anagrams_list, [], [])
    print(f'{count} anagrams:  {anagrams_list}')


def find_anagrams_helper(word_list, anagrams_list, ans_lst, index_list):
    """
    the helper function of find_anagrams()
    :param word_list: lst, the word input by user and arrange by sequence
    :param anagrams_list: lst, the list of anagrams in the dictionary
    :param ans_lst: lst, the process of the answer with list type
    :param index_list: lst, the list of index used in the finding process
    """
    global count

    if len(word_list) == len(ans_lst):
        word = string_manipulation(ans_lst)
        if word in words:
            if word not in anagrams_list:
                print(f'Found: {word}')
                print('Searching...')
                anagrams_list.append(word)
                count += 1
    else:
        for i in range(len(word_list)):
            if i not in index_list:
                # Choose
                index_list.append(i)
                ans_lst.append(word_list[i])
                word = string_manipulation(ans_lst)
                if has_prefix(word):
                    # Explore
                    find_anagrams_helper(word_list, anagrams_list, ans_lst, index_list)
                # Un-choose
                index_list.pop()
                ans_lst.pop()


def string_manipulation(ans_lst):
    """
    change the type of answer from list to string
    :param ans_lst: list, the process of the answer with list type
    :return: str, the process of the answer with string type
    """
    word = ""
    for i in range(len(ans_lst)):
        word += ans_lst[i]

    return word


def has_prefix(sub_s):
    """
    Tell the user "is there any words with prefix stored in the process of the answer in the dictionary?"
    :param sub_s: str, the process of the answer with string type
    :return: bool, is there any words with prefix stored in the process of the answer
    """
    for i in range(len(words)):
        word = str(words[i])
        if word.startswith(sub_s):
            return True
    return False



if __name__ == '__main__':
    main()
