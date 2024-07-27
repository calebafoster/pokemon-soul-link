def add(table):
    new_table = table
    while True:
        response = input()

        if not response:
            return new_table

        new_table.append(response.split(','))

def remove(table):
    new_table = table
    while True:
        if len(new_table) == 1:
            print('nothing to remove')
            return new_table
        print("removing")
        response = input()
        if not response:
            return new_table
        for x, mon in enumerate(new_table):
            if mon[0] == response:
                new_table.pop(x)
