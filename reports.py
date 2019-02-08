
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
        
