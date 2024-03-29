"""
File: babynames.py
Name: Linda
-----------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

integrate all name data from all files, and search the name by target with case-insensitive
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    if name not in name_data:
        year_and_rank = {}
        year_and_rank[year] = rank
        name_data[name] = year_and_rank
    else:
        name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    rank_number = 0
    with open(filename, 'r') as f :
        for line in f:
            line = line.strip()
            data = line.split(',')
            if rank_number == 0:
                year = data[0]
            else:
                rank = data[0]
                rank = rank.strip()
                # male name
                name1 = data[1]
                name1 = name1.strip()
                # female name
                name2 = data[2]
                name2 = name2.strip()
                if name1 not in name_data:
                    year_and_rank = {}
                    year_and_rank[year] = rank
                    name_data[name1] = year_and_rank
                else:
                    if year not in name_data[name1]:
                        name_data[name1][year] = rank
                if name2 not in name_data:
                    year_and_rank = {}
                    year_and_rank[year] = rank
                    name_data[name2] = year_and_rank
                else:
                    if year not in name_data[name2]:
                        name_data[name2][year] = rank
            rank_number += 1


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for i in range(len(filenames)):
        filename = filenames[i]
        with open(filename, 'r') as f:
            rank_number = 0
            for line in f:
                line = line.strip()
                data = line.split(',')
                if rank_number == 0:
                    year = data[0]
                    year = year.strip()
                else:
                    rank = data[0]
                    rank = rank.strip()
                    # male name
                    name1 = data[1]
                    name1 = name1.strip()
                    # female name
                    name2 = data[2]
                    name2 = name2.strip()
                    if name1 not in name_data:
                        year_and_rank = {}
                        year_and_rank[year] = rank
                        name_data[name1] = year_and_rank
                    else:
                        if year not in name_data[name1]:
                            name_data[name1][year] = rank
                    if name2 not in name_data:
                        year_and_rank = {}
                        year_and_rank[year] = rank
                        name_data[name2] = year_and_rank
                    else:
                        if year not in name_data[name2]:
                            name_data[name2][year] = rank
                rank_number += 1

    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    matching_names =[]
    target = target.lower()
    for name in name_data:
        name = name.lower()
        if target in name:
            name = string_manipulation(name)
            matching_names.append(name)

    return matching_names

def string_manipulation(name):
    """
    :param name: lower case, the name contained within name_data and included target word
    :return: the name with upper case in first letter
    """
    ans = ""
    for i in range(len(name)):
        if i == 0 :
            ans += name[i].upper()
        else:
            ans += name[i].lower()
    return ans


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
