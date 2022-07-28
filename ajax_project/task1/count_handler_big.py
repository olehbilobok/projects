def read_file(log_file):
    # Extract data from the log file

    with open(log_file) as file:
        return file.readlines()


def get_data(logs):
    # Get ids of devices which passed test and failed

    bad_devices_data = []
    good_devices_data = []

    for line in logs:
        if 'BIG' in line:
            data = (line[line.index("'") + 1: line.rindex(";")]).split(';')
            id_value = data[2]
            state = data[-1]

            if state == '02' and id_value not in good_devices_data:
                good_devices_data.append(id_value)
            elif state == 'DD' and id_value not in bad_devices_data:
                bad_devices_data.append(id_value)

    return good_devices_data, bad_devices_data


def get_unique_id(good_dev_data, bad_dev_data):
    # Get the new set, that contains only the elements that are NOT present in both sets

    return set(good_dev_data).symmetric_difference(bad_dev_data)


def represent_data(good_dev_data, bad_dev_data):
    # Terminal's output of received data

    print(f'__________Failed test {len(bad_dev_data)} devices__________')
    for device in bad_dev_data:
        print(f'    Device {device} was removed')
    print()
    print(f'__________Success test {len(good_dev_data)} devices__________')
    for device in good_dev_data:
        print(f'    Device {device} sent success statuses')


def main():
    # Call functions

    logs = read_file('app_2.log')
    good_dev_data, bad_dev_data = get_data(logs)
    good_unique_id = get_unique_id(good_dev_data, bad_dev_data)
    represent_data(good_unique_id, bad_dev_data)


if __name__ == '__main__':
    main()
