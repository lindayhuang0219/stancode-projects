"""
File: boggle.py
Name: Linda
----------------------------------------
Each player searches for words that can be constructed from the letters of sequentially adjacent cubes,
where "adjacent" cubes are those horizontally, vertically, and diagonally neighboring.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'  # This is the filename of an English dictionary

words = [] 				 # This is the list of an English dictionary
count = 0 				 # the number of anagrams for the word input by user

COL_AND_ROW = 4 		 # the number of column and row in the game
word_lst = []  			 # the word list input by user and arrange by row
anagram_lst = []   		 # the list of anagrams in the dictionary


def main():
	"""
	Each player searches for words that can be constructed from the letters of sequentially adjacent cubes and
	prints the final count result on the console.
	"""
	if input_word():
		read_dictionary()
		find_start_place(word_lst)
		print(f'There are {count} words in total.')


def input_word():
	"""
	input the word by user and change the type from string to list
	:return: bool, the format of the word input by user is legal or not
	"""
	global word_lst
	index = 0
	while index < COL_AND_ROW :
		word = input(str(f'{index+1} row of letters: '))
		word = word.lower()
		word = word.split()
		for letter in word:
			if len(letter) != 1:
				print('Illegal input')
				return False
		index +=1
		word_lst.append(word)
	return True


def find_start_place(word_lst):
	"""
	find the coordinate of each start alphabet, append the first word to the answer list, and enter into the recursion
	:param word_lst: lst, the word list input by user and arrange by row
	"""
	for j in range(COL_AND_ROW):
		for i in range(COL_AND_ROW):
			letter = word_lst[i][j]
			letter_x, letter_y = i , j
			ans_lst = []
			index_list = []
			ans_lst.append(letter)
			index_list.append((letter_x, letter_y))
			find_word_lst(letter,letter_x,letter_y,ans_lst, index_list)


def find_word_lst(letter,start_x,start_y,ans_lst, index_list):
	"""
	finds all the combinations for the word input by user
	and print the all answers, which are in the dictionary, on the console
	:param letter: str, the start alphabet
	:param start_x: int, the x coordinate of start alphabet
	:param start_y: int, the y coordinate of start alphabet
	:param ans_lst: lst, the process of the answer with list type
	:param index_list: lst, the list of index used in the finding process
	"""
	global count, anagram_lst
	neighbor_list = find_neighbor(start_x, start_y)
	if len(ans_lst) >= 4:
		word = string_manipulation(ans_lst)
		if word in words:
			if word not in anagram_lst:
				print(f'Found "{word}"')
				count += 1
				anagram_lst.append(word)
	for i in range(len(neighbor_list)):
		if neighbor_list[i] not in index_list:
			# Choose
			index_list.append(neighbor_list[i])
			neighbor_x, neighbor_y = neighbor_list[i]
			if 0 <= neighbor_x < COL_AND_ROW and 0 <= neighbor_y < COL_AND_ROW:
				ans_lst.append(word_lst[neighbor_x][neighbor_y])
				word = string_manipulation(ans_lst)
				if has_prefix(word):
					# Explore
					find_word_lst(letter,neighbor_x,neighbor_y,ans_lst, index_list)
				ans_lst.pop()
			index_list.pop()


def find_neighbor(x, y):
	"""
	find the all legal neighbor coordinate of start alphabet
	:param x: The x coordinate of start alphabet
	:param y: The y coordinate of start alphabet
	:return: lst, the all neighbor coordinate of start alphabet
	"""
	# upper-left
	if x == 0 and y == 0 :
		return [(x+1,y),(x,y+1),(x+1,y+1)]
	# lower-left
	elif x == 0 and y == COL_AND_ROW-1:
		return [(x + 1, y), (x, y - 1), (x + 1, y - 1)]
	# upper_right
	elif x == COL_AND_ROW-1 and y == 0:
		return [(x - 1, y), (x, y + 1), (x - 1, y + 1)]
	# lower-right
	elif x == COL_AND_ROW-1 and y == COL_AND_ROW-1:
		return [(x - 1, y), (x, y - 1), (x - 1, y - 1)]
	# upper horizontal
	elif 0 < x < COL_AND_ROW-1 and y == 0:
		return [(x - 1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y)]
	# left straight
	elif x == 0 and 0 < y < COL_AND_ROW-1:
		return [(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1)]
	# right straight
	elif x == COL_AND_ROW-1 and 0 < y < COL_AND_ROW-1:
		return [(x, y-1),(x-1, y-1),(x-1, y),(x-1, y+1),(x, y+1)]
	# down horizontal
	elif 0 < x < COL_AND_ROW-1 and y == COL_AND_ROW-1:
		return [(x-1,y), (x-1, y-1),(x, y-1),(x+1, y-1),(x+1,y)]
	# middle
	else:
		return [(x-1, y-1), (x-1 , y),(x-1, y+1),(x, y-1),(x, y+1),(x+1, y-1),(x+1, y),(x+1, y+1)]


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


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE and appends words in each line into a Python list
	"""
	global words
	with open(FILE, 'r') as f:
		for line in f:
			if len(line.strip()) >= 4:
				words.append(line.strip())


def has_prefix(sub_s):
	"""
	Tell the user "is there any words with prefix stored in the process of the answer in the dictionary?"
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in range(len(words)):
		word = str(words[i])
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
