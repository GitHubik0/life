import random

class Car:
    def __init__(self, car, model, price):
        self.car = car
        self.model = model
        self.price = price
        self.driver = None

    def set_driver(self, driver, day):
        if driver.money >= self.price and self not in driver.cars:
            self.driver = driver
            driver.cars.append(self)
            driver.money -= self.price
            print(f"День {day}: {driver.name} купив {self.car} {self.model} за {self.price} гривень")
        elif self in driver.cars:
            print(f"День {day}: {driver.name} вже має {self.car} {self.model}")
        else:
            print(f"День {day}: {driver.name} не має достатньо грошей для покупки {self.car} {self.model}")

    def display_driver(self):
        return self.driver.name if self.driver else None

class Driver:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cars = []
        self.alive = True

    def own_car(self, cars, day):
        car_to_buy = random.choice(cars)
        car_to_buy.set_driver(self, day)

    def display_cars(self):
        return ', '.join([f'{car.car} {car.model}' for car in self.cars]) if self.cars else None

    def work(self, day):
        earnings = random.randint(200, 500)
        self.money += earnings
        print(f"День {day}: {self.name} заробив {earnings} гривень")

    def eat(self, day):
        food_cost = random.randint(100, 300)
        if self.money >= food_cost:
            self.money -= food_cost
            print(f"День {day}: {self.name} витратив {food_cost} гривень на їжу")
        else:
            print(f"День {day}: {self.name} не має достатньо грошей на їжу і тому він помер. Він мав би заплатити {food_cost} гривень за їжу")
            self.alive = False

cars = [
    Car('Toyota', 'Corolla', random.randint(500, 2000)),
    Car('Toyota', 'Camry', random.randint(500, 2000)),
    Car('Ford', 'Mustang', random.randint(500, 2000)),
    Car('Ford', 'F-150', random.randint(500, 2000)),
    Car('BMW', 'X5', random.randint(500, 2000)),
    Car('BMW', 'X3', random.randint(500, 2000)),
    Car('Audi', 'A4', random.randint(500, 2000)),
    Car('Audi', 'A6', random.randint(500, 2000)),
    Car('Mercedes-Benz', 'C-Class', random.randint(500, 2000)),
    Car('Mercedes-Benz', 'E-Class', random.randint(500, 2000))
]

driver = Driver('David', 1500)

for day in range(1, 32):
    print(f"\nДень {day}:")
    if driver.alive:
        driver.work(day)
        driver.eat(day)
        if driver.alive:
            driver.own_car(cars, day)
            print(f"День {day}: {driver.name} має {len(driver.cars)} автомобілів: {driver.display_cars()}")
            print(f"День {day}: {driver.name} має {driver.money} гривень")
    else:
        break

if driver.alive:
    print(f"\n{driver.name} має наступні автомобілі: {driver.display_cars()}")
    if len(driver.cars) >= 6:
        print(f"{driver.name} прожив гарне життя")
else:
    print(f"\n{driver.name} помер")