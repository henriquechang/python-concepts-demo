from collections import namedtuple

Customer = namedtuple('Customer', 'name')


class ChargeItem:

    def __init__(self, terminal, days, price):
        self.terminal = terminal
        self.days = days
        self.price = price

    def total(self):
        return self.price * self.days


class Charges:
    def __init__(self, customer, charge_item, promotion=None):
        self.customer = customer
        self.charge_list = list(charge_item)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.charge_list)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Charges total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def trimester_use_promo(charges):
    return charges.total() * .05 if sum(charge.days for charge in charges.charge_list) >= 90 else 0


def monthly_charge_promo(charges):
    discount = 0
    for charge in charges.charge_list:
        if charge.days >= 30:
            discount += charge.total() * .15
    return discount
