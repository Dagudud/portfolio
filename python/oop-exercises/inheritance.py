from game_classes import Warrior, Mage 
import random

class Archer(Warrior):
    def __init__(self, health=100, stamina=100, arrows=20):
        super().__init__(health)
        self.__stamina = stamina
        self.arrows = arrows

    @property
    def stamina(self):
        return self.__stamina
    
    @stamina.setter
    def stamina(self, new_stamina):
        if new_stamina > 100:
            self.__stamina = 100
        elif new_stamina < 0:
            self.__stamina = 0
        else:
            self.__stamina = new_stamina

    def sniper_shot(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} выполняет снайперский выстрел в'
              f' {target.__class__.__name__}')
        target.health -= 15
        self.__stamina -= 30
        self.arrows -= 1
        print(f'Здаровье у {target.__class__.__name__} понижено до {target.health}')
        print(f'У {self.__class__.__name__} осталось {self.arrows} стрел и {self.__stamina} стамины')
        print('---------------')

    def __critical_hit(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} наносит критический урон стрелой'
              f' {target.__class__.__name__}')
        target.health -= 15
        self.arrows -= 1
        print(f'Здаровье у {target.__class__.__name__} понижено до {target.health}')
        print(f'У {self.__class__.__name__} осталось {self.arrows} стрел')
        print('---------------')

    def attacks(self, target):
        x = random.randint(0, 100)
        if x >= 0 and x <= 30:
            self.__critical_hit(target)
        else:
            print('---------------')
            print(f'{self.__class__.__name__} использует лук против'
                f' {target.__class__.__name__}')
            target.health -= 4
            self.arrows -= 1
            print(f'Здаровье у {target.__class__.__name__} понижено до {target.health}')
            print(f'У {self.__class__.__name__} осталось {self.arrows} стрел')
            print('---------------')

    def introduces(self):
        super().introduces()
        print('---------------')
        print(f'Arrows: {self.arrows}')
        print('---------------')

class Alchemist(Mage):
    def __init__(self, health=100, mana=100, flasks=10):
        super().__init__(health, mana)
        self.flasks = flasks

    def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} использует бутыль с огнём против'
              f' {target.__class__.__name__}, \nно при этом задевая себя')
        target.health -= 10
        self.health -= 3
        self.flasks -= 1
        print(f'Здаровье у {target.__class__.__name__} понижено до {target.health}')
        print(f'Здаровье у {self.__class__.__name__} понижено до {self.health}')
        print(f'У {self.__class__.__name__} осталось {self.flasks} алхимических бутылей')
        print('---------------')

unit1 = Archer()
unit2 = Archer()
unit3 = Warrior()
unit4 = Mage()
unit5 = Alchemist()

unit2.sniper_shot(unit3)