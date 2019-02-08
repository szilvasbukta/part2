
# Report functions


def sum_sold(file_name):
    count = float(0)
    with open(file_name, 'r') as f:
        for line in f:
            game_info = line.split("\t")
            count += float(game_info[1])
    return count
