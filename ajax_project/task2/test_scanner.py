from tasks.task2.scanner_handler import CheckQr


class TestCheckQr(CheckQr):

    def check_in_db(self, qr):

        if len(qr) % 2:
            return True

    def get_color(self, device):

        if self.color:
            print(f'device: {device} color: {self.color}')

        else:
            print(self.send_error(f"device {device} doesn't have any colors"))


obj = TestCheckQr()

print('---------device & colors ----------')
print()

for x in range(1, 8):

    device = '*' * x

    if not obj.check_in_db(device):

        print(obj.send_error(f'device {device} not in db'))
        # print(obj.can_add_device(f'device {device} was added successfully'))

    obj.check_scanned_device(device)
    obj.get_color(device)
    print()
