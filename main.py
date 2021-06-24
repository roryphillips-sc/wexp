# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def parse_csv(filename):
    with open(filename, "r") as data:
        header = next(data)
        cols = header.strip().split(',')
        # ['id', 'name', 'color']

        should_read = True
        records = []
        while should_read:
            row = ""
            try:
                row = next(data)
            except StopIteration:
                should_read = False
                continue

            points = row.strip().split(',')
            # ['1', 'test', 'red']
            record = {}
            for i in range(0, len(cols)):
                # start at 0, finish at length of columns list
                # For each column, get the same index from the point
                record[cols[i]] = points[i]

            records.append(record)
        return records


def import_into_database(records):



def main(name):
    data = parse_csv("./demo.csv")
    print(data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
