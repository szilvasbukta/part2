
# Printing functions

from reports import *


def main():
    while True:
        user_input = int(input('''
1) Get_most_played   9) EXIT
2) Sum_sold
3) Get_selling_avg
4) Count_longest_title
5) Get_date_avg
6) Get_game
7) Count_grouped_by_genre
8) Get_date_ordered
\nChoose a function 1 - 8: '''))
        if user_input == 1:
            print("\nWhat is the title of the most played game?\n")
            print("\n",get_most_played("game_stat.txt"),"\n")
        elif user_input == 2:
            print("\nHow many copies have been sold total?\n")
            print("\n",sum_sold("game_stat.txt"),"\n")
        elif user_input == 3:
            print("\nWhat is the average selling?\n")
            print("\n",get_selling_avg("game_stat.txt"),"\n")
        elif user_input == 4:
            print("\nHow many characters long is the longest title?\n")
            print("\n",count_longest_title("game_stat.txt"),"\n")
        elif user_input == 5:
            print("\nWhat is the average of the release dates?\n")
            print("\n",get_date_avg("game_stat.txt"),"\n")
        elif user_input == 6:
            print("\nWhat is the alphabetical ordered list of the titles?\n")
            title = input("Choose a title: ")
            for prop in get_game('game_stat.txt',title):
                print(str(prop))
        elif user_input == 7:
            print("\nHow many games are there grouped by genre?\n")
            for genre, count in count_grouped_by_genre('game_stat.txt').items():
                print(genre+"  "+str(count))
        elif user_input == 8:
            print("\nWhat is the date ordered list of the games?\n")
            for i in get_date_ordered("game_stat.txt"):
                print(i, end = "\n")
        elif user_input == 9:
            exit()


if __name__ == "__main__":
    main()