
# Report functions


def sum_sold(file_name):
    count = float(0)
    with open(file_name, 'r') as f:
        for line in f:
            game_info = line.split("\t")
            count += float(game_info[1])
    return count


def get_selling_avg(file_name):
    with open(file_name, 'r') as f:
        games= 0
        sold_copies = float(0)
        for line in f:
            line = line.split("\t")
            games += 1
            sold_copies += float(line[1])
        output = sold_copies / float(games)
    return output


def get_game(file_name, title):
    with open(file_name, 'r') as f:
        for line in f:
            line = line.split("\t")
            line[4] = line[4].strip("\n")
            line[1] = float(line[1])
            line[2] = int(line[2])
            if line[0] == title:
                return line
