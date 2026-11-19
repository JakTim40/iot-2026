class WaterPump:
    def __init__(self, power=0, brand="Невідомо", water_volume=0, price=0, color="Синій"):
        self.__power = power
        self.__brand = brand
        self.__water_volume = water_volume
        self.price = price
        self.color = color

    def get_power(self):
        return self.__power

    def get_brand(self):
        return self.__brand

    def get_water_volume(self):
        return self.__water_volume

    def __str__(self):
        return f"Насос {self.__brand}: потужність {self.__power} Вт, качає {self.__water_volume} л/год, ціна {self.price} грн, колір {self.color}"

    def __repr__(self):
        return f"WaterPump({self.__power}, '{self.__brand}', {self.__water_volume}, {self.price}, '{self.color}')"

    def __del__(self):
        print(f"Об'єкт насоса {self.__brand} видалено")


def main():
    pump1 = WaterPump()
    pump2 = WaterPump(750, "Bosch", 3000, 4500, "Зелений")
    pump3 = WaterPump(1100, "Grundfos", 5000, 8200, "Червоний")

    print("--- Насос 1 ---")
    print("Виробник:", pump1.get_brand())
    print("Потужність:", pump1.get_power())
    print("Об'єм води:", pump1.get_water_volume())
    print("Ціна:", pump1.price)
    print("Колір:", pump1.color)
    print("str:", str(pump1))
    print("repr:", repr(pump1))

    print("\n--- Насос 2 ---")
    print("Виробник:", pump2.get_brand())
    print("Потужність:", pump2.get_power())
    print("Об'єм води:", pump2.get_water_volume())
    print("Ціна:", pump2.price)
    print("Колір:", pump2.color)
    print("str:", str(pump2))
    print("repr:", repr(pump2))

    print("\n--- Насос 3 ---")
    print("Виробник:", pump3.get_brand())
    print("Потужність:", pump3.get_power())
    print("Об'єм води:", pump3.get_water_volume())
    print("Ціна:", pump3.price)
    print("Колір:", pump3.color)
    print("str:", str(pump3))
    print("repr:", repr(pump3))
    print()


main()