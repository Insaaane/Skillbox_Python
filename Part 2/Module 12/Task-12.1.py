class Property():
    def __init__(self, worth: float) -> None:
        self.worth = worth

    def calculateTax(self):
        pass


class Apartment(Property):
    def __init__(self, worth: float) -> None:
        super().__init__(worth)

    def calculateTax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth: float) -> None:
        super().__init__(worth)

    def calculateTax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth: float) -> None:
        super().__init__(worth)

    def calculateTax(self):
        return self.worth / 500


entities = [Apartment, Car, CountryHouse]
money = float(input("Введите количество денег: "))
tax_sum = 0

for i, entity in enumerate(["квартир", "машин", "дач"]):
    for j in range(int(input(f"Введите количество {entity}: "))):
        tax_sum += entities[i](int(input(f"Введите стоимость {j+1}-й: "))).calculateTax()

delta = abs(money - tax_sum)
print(f"{'После уплаты налогов у вас останется' if money >= tax_sum else 'На уплату налогов вам не хватит'}"
      f" {delta} денег")


