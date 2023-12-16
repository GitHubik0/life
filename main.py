import random

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength += 1
            return False
        else:
            print('The car cannot move')
            return False

brands_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
                 'DEO': {'fuel': 50, 'strength': 40, 'consumption': 10},
                 'Tesla': {'fuel': 60, 'strength': 100, 'consumption': 6},
                 'Ferari': {'fuel': 150, 'strength': 100, 'consumption': 10}}

class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {'Java developer': {'salary': 50, 'gladness_less': 10},
            'Python developer': {'salary': 150, 'gladness_less': 15},
            'Web design': {'salary': 100, 'gladness_less': 1}}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

class Cat_life:
    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.progress = 5
        self.eat = 30
        self.energy = 25
        self.alive = True

    def to_study(self):
        print('Час для навчання команд')
        self.progress += 15
        self.gladness -= 5
        self.eat -= 5
        self.energy -= 20

    def to_sleep(self):
        print('Час для сну')
        self.gladness += 10
        self.eat -= 15
        self.energy += 40

    def to_chill(self):
        print('Час для відпочинку')
        self.progress -= 5
        self.gladness += 15
        self.eat -= 5
        self.energy -= 5

    def to_eat(self):
        print('Час для їжі')
        self.gladness += 10
        self.eat += 35
        self.energy += 15

    def to_go_walk(self):
        print('Час для прогулянки')
        self.gladness += 10
        self.eat += -10
        self.energy += -15

    def is_alive(self):
        if self.progress <= -15:
            print('Йди розвивайся!')
            self.alive = False

        elif self.gladness <= -15:
            print('Упс, в тебе депресія.')
            self.alive = False

        elif self.progress >= 250:
            print('Молодець, ти став найрозумнішим котом світу!')
            self.alive = False

        elif self.eat <= -20:
            print('Ти зголоднів.')
            self.alive = False

        elif self.eat >= 250:
            print('Ти став жирним. Тебе здали в притулок >:(')
            self.alive = False

        elif self.energy <= -20:
            print('У тебе не було енергії щоб гратися. Твої господарі здали тебе в притулок!')
            self.alive = False

        elif self.energy >= 250:
            print('У тебе було забагато енергії. Твої господарі здали тебе в притулок!')
            self.alive = False

    def end_of_the_day(self):
        print(f"Щастя - {self.gladness}")
        print(f"Розум - {round(self.progress, 2)}")
        print(f"Їжа - {round(self.eat, 3)}")
        print(f"Енергія - {round(self.energy, 4)}")

    def live(self, day):
        day = 'Day ' + str(day) + ' of ' + self.name + ' life'
        print(f"{day:^50}")
        kubik = random.randint(1, 5)
        if kubik == 1:
            self.to_study()
            self.end_of_the_day()
            self.is_alive()
        elif kubik == 2:
            self.to_sleep()
            self.end_of_the_day()
            self.is_alive()
        elif kubik == 3:
            self.to_chill()
            self.end_of_the_day()
            self.is_alive()
        elif kubik == 4:
            self.to_eat()
            self.end_of_the_day()
            self.is_alive()
        elif kubik == 5:
            self.to_go_walk()
            self.end_of_the_day()
            self.is_alive()


class Human:
    def __init__(self, name='Human', job=None, car=None, home=None):
        self.name = name
        self.car = car
        self.job = job
        self.home = home
        self.money = 1500
        self.gladness = 200
        self.satiety = 200
        self.cat = None

    def get_cat(self, name):
        self.cat = Cat_life(name)

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage = 'fuel':
            print('FUEL!!!!!')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('FOOD!!!')
            self.money -= 50
            self.home.food += 50
        elif manage == 'sweets':
            print('SWETTS!!!!')
            self.satiety += 100
            self.money -= 20

    def chill(self):
        self.gladness += 50
        self.home.mess += 20

    def clean_home(self):
        self.gladness += 10
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f'Day today {day} of {self.name}'
        print(f"{day:=^50}", '\n')
        human_indexes = self.name + ' s indexes'
        print(f"{human_indexes:+^50}", '\n')
        print(f" MONEY - {self.money}")
        print(f" SATIETY - {self.satiety}")
        print(f" GLADNESS - {self.gladness}")
        home_index = "Home indexes"
        print(f" {home_index:^50}")
        print(f" FOOD - {self.home.food}")
        print(f"MESS - {self.home.mess}")
        car_indexes = 'car!!'
        print(f" {car_indexes:+^50}")
        print(f" FUEL - {self.car.fuel}")
        print(f"STRENGTH - {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print('DEPRESSION')
            return False
        if self.satiety < 0:
            print('DEAD')
            return False
        if self.money < -500:
            print('CREDIT')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Select HOME')
            self.get_home()
        if self.car is None:
            print('CAR SELECT')
            self.get_car()
        if self.job is None:
            print('SELECT JOB')
            self.get_job()
            print(f"I dont have jon - a job is -- {self.job} with salary")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print('EAT')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print('CHILL-Clean')
                self.clean_home()
            else:
                print('chill')
                self.chill()
        elif self.money < 0:
            print('work!')
            self.work()
        elif self.car.strength < 15:
            print('REPPAIR')
            self.to_repair()
        elif dice == 1:
            print('chill')
            self.chill()
        elif dice == 2:
            print('Work')
            self.work()
        elif dice == 3:
            print('CLEAN')
            self.clean_home()
        elif dice == 4:
            print('SWEETS')
            self.shopping(manage='sweets')

nick = Human(name='Ivan')
nick.get_cat('Patrik')
nick.get_job()

for day in range(1, 366):
    if nick.live(day) == False:
        break