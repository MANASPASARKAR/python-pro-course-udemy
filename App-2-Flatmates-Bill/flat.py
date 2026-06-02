class Bill:
    """
    object that contains data about a bill,
    such as total amount and period of bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

    """
    creates a flatmate that is a person, has a name and
    pays some amount of the bill
    based on the days he lives in the house
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house


    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return weight * bill.amount
