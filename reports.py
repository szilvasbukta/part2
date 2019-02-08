
# Report functions


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
