import csv


def open_file(file_name, operation):
    return open(file_name, operation)


def get_value(data, max_val=True):
    values = [int(x.split(';')[-1]) for x in data]
    return max(values) if max_val else min(values)


def read(file, max_val=None):

    data = [x[0] for x in csv.reader(file)]

    value = get_value(data, max_val) if max_val is not None else 0

    for i, row in enumerate(data, start=1):

        if value != 0 and int(row.split(';')[-1]) == value:
            print(i, row)
        elif value == 0:
            print(i, row)

    file.close()


def add(file, data):
    csv.writer(file, delimiter=';').writerow(data)
    file.close()


def delete(input_data, index):

    data = []
    with input_data as inp:
        reader = csv.reader(inp)
        for i, row in enumerate(reader, start=1):
            if i == index:
                action = input(f'are you sure you want to delete this row?\n{row[0]}\nyes or no\ntype here: ')
                if action == 'yes':
                    continue
            data.append(row)

    output_data = open_file('films.csv', 'w')

    with output_data as out:
        writer = csv.writer(out, delimiter=';')
        writer.writerows(data)


def edit(input_data, index):

    data = []
    with input_data as inp:
        reader = csv.reader(inp)
        for i, row in enumerate(reader, start=1):
            data.append(row)
            if i == index:
                action = input(f'do you want to change full row\n{row}\nyes or no\ntype here: ')
                if action == 'yes':
                    edited_row = input('Enter the new row splitted by comma\ntype here:')
                    data[index-1] = [row[0].replace(row[0], edited_row.replace(',', ';'))]
                else:
                    choice = input('if you want to edit:\n film name - enter 1\nnotes - enter 2\nrate - enter 3\n\
                    type here: ')
                    if choice == '1':
                        film_name = input('enter the new film_name:')
                        data[index-1] = [row[0].replace(row[0].split(';')[0], film_name)]
                    elif choice == '2':
                        notes = input('enter the new note:')
                        data[index - 1] = [row[0].replace(row[0].split(';')[1], notes)]
                    else:
                        notes = input('enter the rate which you want edit:')
                        data[index - 1] = [row[0].replace(row[0].split(';')[2], notes)]

    output_data = open_file('films.csv', 'w')

    with output_data as out:
        writer = csv.writer(out, delimiter=';')
        writer.writerows(data)


def main():

    # file_name = input('give me file name :)')
    while True:

        action = input('what do you wanna do ?)\ntype here: ')

        if action == 'read':

            file = open_file('films.csv', 'r')

            selection = input('do you need to get movies by rating? yes or no \ntype here: ')

            value = None

            if selection == 'yes':

                value = input('higher or lower?\n type here: ')

                value = True if value == 'higher' else False

            read(file, value)

        elif action == 'add':

            file = open_file('films.csv', 'a')

            data = input('add data \nfor example: name,notes,rating\ntype here:')

            add(file, [x.strip() for x in data.split(',')])

            print('was added successfully!')

        elif action == 'delete':

            input_data = open_file('films.csv', 'r')

            index = int(input('index for delete?\ntype here '))

            delete(input_data, index)

            print('was deleted successfully!')

        elif action == 'edit':

            input_data = open_file('films.csv', 'r')

            index = int(input('index for editind?\ntype here '))

            edit(input_data, index)

            print('was edited successfully!')

        elif action == 'stop':
            break


if __name__ == "__main__":
    main()
