import itertools
class Allergies:
    allergy_list = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

    def __init__(self, score):
        self.allergy_bool = []
        for _ in range(len(self.allergy_list)):
            self.allergy_bool.append(score%2 == 1)
            score //= 2

    def allergic_to(self, item):
        return self.allergy_bool[self.allergy_list.index(item)]

    @property
    def lst(self):
        return list(itertools.compress(self.allergy_list, self.allergy_bool))
