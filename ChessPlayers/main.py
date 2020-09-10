import csv

from player import Player


# adds players from csv file to a list 
def csv_filler(filename):
    players = []
    try:
        with open(filename, encoding="utf8") as input_file:
            reader = csv.reader(input_file,
                                delimiter=',',
                                quotechar='"',
                                skipinitialspace=True)
            for the_row in reader:
                players.append(Player(the_row[0], the_row[1], the_row[2], the_row[3], the_row[4], the_row[5]))
                # print(
                #     "last name=", the_row[0],
                #     "| first name=", the_row[1],
                #     "| full name=", the_row[2],
                #     "| country=", the_row[3],
                #     "| born=", the_row[4],
                #     "| died=", the_row[5])
            # print(str(players[1]))
        return players
    except IOError:
        return "File not found"


# sorts players in a list by their last name
def sorter_by_last_name(players):
    players.sort(key=lambda x: x.last_name)
    return players


# binary search algorithm that helps to find players by their last name
def binary_search(players, item):
    items_list = []
    first = 0
    last = len(players) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if players[mid].last_name == item:
            # adds players to another list
            # because it's possible to have more than one similar last name
            items_list.append(players[mid])
            players.remove(players[mid])
        else:
            if item < players[mid].last_name:
                last = mid - 1
            else:
                first = mid + 1
    return items_list


# extracts players from a list
def list_to_string(players):
    if len(players) > 0:
        for item in players:
            print(item)
        return players
    else:
        print("Player not found")


# main function
def main():
    file = "chess-players.csv"
    filled_players = csv_filler(file)
    sorted_players = sorter_by_last_name(filled_players)
    last_name_to_find = input("Please enter Last Name of a Chess Player that you are looking for: ")

    list_to_string(binary_search(sorted_players, last_name_to_find))


if __name__ == '__main__':
    main()
