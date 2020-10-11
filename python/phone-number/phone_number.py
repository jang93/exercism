import re

class PhoneNumber:
    _pattern = re.compile(r'''
        ^\+?1?               # Country Code
        (?:[-. ]+)*          # Divider
        \(?([2-9]\d\d)\)?    # Area Code
        [-. ]*               # Divider
        ([2-9]\d\d)          # Exchange Code
        [-. ]*               # Divider
        (\d{4})$             # Subscriber number
        ''', re.VERBOSE)

    def __init__(self, number):
        self.number = self.clean_up(number)
        self.area_code = self.number[0:3]

    def clean_up(self, number):
        match = self._pattern.search(number.strip())
        if match is None:
            raise ValueError('Invalid phone number format')
        return f'{match.group(1)}{match.group(2)}{match.group(3)}'

    def pretty(self):
        return f'({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}'
