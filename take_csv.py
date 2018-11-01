import csv


def csv_data():
    listoflists = []
    lists = []
    with open('data.csv', 'rU') as f:  # opens PW file
        data = list(list(rec) for rec in csv.reader(f, delimiter=','))  # reads csv into a list of lists
        for row in data:
            listoflists.append((list(lists)))
            lists = []
            for username in row:
                lists.append(username)
    del listoflists[0]
    del listoflists[0]
    # print(listoflists[0][4])
    return listoflists

#csv_data()


