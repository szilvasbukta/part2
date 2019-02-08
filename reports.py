
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
