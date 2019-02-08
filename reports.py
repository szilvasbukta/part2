
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
