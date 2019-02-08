
# Export functions

from reports import *


def main():
    needed_file = input("\nChoose a file where to export: ")
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
        with open(needed_file+".txt", "a") as opened_file:
            if user_input == 1:
                print("\nWhat is the title of the most played game?\n")
                opened_file.write("What is the title of the most played game: "+str(get_most_played("game_stat.txt"))+"\n")
            elif user_input == 2:
                print("\nHow many copies have been sold total?\n")
                opened_file.write("How many copies have been sold total: "+str(sum_sold("game_stat.txt"))+"\n")
            elif user_input == 3:
                print("\nWhat is the average selling?\n")
                opened_file.write("What is the average selling: "+str(get_selling_avg("game_stat.txt"))+"\n")
            elif user_input == 4:
                print("\nHow many characters long is the longest title?\n")
                opened_file.write("How many characters long is the longest title: "+str(count_longest_title("game_stat.txt"))+"\n")
            elif user_input == 5:
                print("\nWhat is the average of the release dates?\n")
                opened_file.write("What is the average of the release dates: "+str(get_date_avg("game_stat.txt"))+"\n")
            elif user_input == 6:
                print("\nWhat properties has a game?\n")
                title = input("Choose a game title: ")
                opened_file.write("What properties has a game?\n\n")
                for properties in get_game("game_stat.txt", title):
                    opened_file.write(str(properties)+"\n")
            elif user_input == 7:
                print("\nHow many games are there grouped by genre?\n")
                opened_file.write("How many games are there grouped by genre?\n\n")
                for genre_group, count in count_grouped_by_genre('game_stat.txt').items():
                    opened_file.write(genre_group+" : "+str(count)+"\n")
            elif user_input == 8:
                print("\nWhat is the date ordered list of the games?\n")
                opened_file.write("What is the date ordered list of the games(descending):\n")
                for games in get_date_ordered("game_stat.txt"):
                    opened_file.write(games+"\n")
            elif user_input == 9:
                exit()
            opened_file.write("\n")


if __name__ == "__main__":
    main()
