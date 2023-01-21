import random
import sys
import re

def main():
    path = input("Enter a path to the .txt file containing places and descriptions (or press enter if the file is in the same directory as this executable): ")
    # if user does not enter a path, assemble path under assumption places.txt is in same directory as executable
    if (path == ""):
        path = re.sub('\..*', '', sys.argv[0]).replace('MythologicalPlacesGenerator', 'places.txt')
    file = open(path, encoding='utf-8')

    places = []
    descriptions = []

    # populate places from .txt
    line = ''
    while line != 'end_of_places\n':
        line = file.readline()
        if line != 'end_of_places\n':
            places.append(line.replace("\n", ""))

    # populate descriptions from .txt
    while line != 'end_of_file':
        line = file.readline()
        if line != 'end_of_file':
            descriptions.append(line.replace("\n", ""))

    # generate places
    print("Press enter to continue generating or exit to stop")
    continue_generating = True
    while continue_generating:
        index = random.randint(0, len(places) - 1)
        print(places[index] + ": " + descriptions[index], end="")

        user_in = input('')
        if (user_in == "exit"):
            continue_generating = False

if __name__ == '__main__':
    main()