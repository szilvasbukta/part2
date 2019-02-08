
# Report functions


def get_most_played(file_name):
    with open(file_name, 'r') as opened_file:
        most_copies = ['', 0]   # game title, copies_sold
        for line in opened_file:
            line = line.split("\t")
            if float(line[1]) > float(most_copies[1]):
                most_copies[1] = line[1]
                most_copies[0] = line[0]
        return most_copies[0]


def sum_sold(file_name):
    count = float(0)
    with open(file_name, 'r') as f:
        for line in f:
            game_info = line.split("\t")
            count += float(game_info[1])
    return count


def get_selling_avg(file_name):
    with open(file_name, 'r') as f:
        games = 0
        sold_copies = float(0)
        for line in f:
            line = line.split("\t")
            games += 1
            sold_copies += float(line[1])
        output = sold_copies / float(games)
    return output
     
                
def count_longest_title(file_name):
    with open(file_name, 'r') as opened_file:
        characters_long = [0]
        for line in opened_file:
            line = line.split("\t")
            if len(line[0]) > characters_long[0]:
                characters_long[0] = len(line[0])
        return(characters_long[0])


def get_date_avg(file_name):
    with open(file_name, 'r') as f:
        dates = 0
        years = 0
        for line in f:
            game_info = line.split('\t')
            dates += 1
            years += int(game_info[2])
        avg_date = int(years / dates)+1
    return avg_date


def get_game(file_name, title):
    with open(file_name, 'r') as f:
        for line in f:
            line = line.split("\t")
            line[4] = line[4].strip("\n")
            line[1] = float(line[1])
            line[2] = int(line[2])
            if line[0] == title:
                return line


def get_date_ordered(file_name):
    years = []
    ordered_titles = []
    with open(file_name, 'r') as f:
        for line in f:
            game_info = line.split('\t')
            game_info[2] = int(game_info[2])
            if len(ordered_titles) == 0 or game_info[2] < years[-1]:
                ordered_titles.append(game_info[0])
                years.append(game_info[2])
            else:
                for y, year in enumerate(years):
                    if game_info[2] == year and (game_info[0]).lower() < (ordered_titles[y]).lower():
                        ordered_titles.insert(y, game_info[0])
                        years.insert(y, game_info[2])
                        break
                    elif game_info[2] > year:
                        ordered_titles.insert(y, game_info[0])
                        years.insert(y, game_info[2])
                        break
        return ordered_titles   
