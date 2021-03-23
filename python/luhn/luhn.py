

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        card_num_stripped = self.card_num.replace(' ', '')

        if len(card_num_stripped) <= 1 or not card_num_stripped.isdigit():
            return False

        output = [int(digit) for digit in card_num_stripped]
        for i in range(len(output) - 2, -1, -2):
            output[i] = output[i] * 2 -9 if output[i] * 2 > 9 else output[i] * 2
        return sum(output) % 10 == 0