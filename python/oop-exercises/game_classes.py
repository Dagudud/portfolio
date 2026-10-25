class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health
        self.__stamina = stamina

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, new_health):
        if new_health > 100:
            self.__health = 100
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} накладывает повязку из целебных трав'
              f' {target.__class__.__name__}')
        target.health += 10
        self.stamina -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}'
              f'\nУ {self.__class__.__name__} осталось {self.stamina} едениц запаса сил')
        print('---------------')

    #def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} наносит урон мечом'
              f' {target.__class__.__name__}')
        target.health -= 3
        print(f'Здаровье у {target.__class__.__name__} понижено до {target.health}')
        print('---------------')

    #def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nStamina: {self.stamina}')
        print('---------------')

class Mage:
    def __init__(self, health=60, mana=100):
        self.__health = health
        self.__mana = mana

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, new_health):
        if new_health > 100:
            self.__health = 100
        elif new_health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    def heals(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} применяет заклинание лечения'
              f' к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено до {target.health}'
              f'\nУ {self.__class__.__name__} осталось {self.mana} едениц магии')
        print('---------------')

    #def attacks(self, target):
        print('---------------')
        print(f'{self.__class__.__name__} наносит урон магией'
              f' {target.__class__.__name__}')
        target.health -= 3
        print(f'Здаровье у {target.__class__.__name__} понижено до {target.health}')
        print('---------------')
    
    #def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.health}',
              f'\nMana: {self.mana}')
        print('---------------')

unit1 = Warrior(50, 50)

print(unit1.health)
unit1.health -= 1000000000
print(unit1.__dict__)
#unit2 = Warrior(stamina=110)
#unit3 = Mage()
#unit4 = Mage(health=50, mana=110)

#unit1.attacks(unit3)
#unit3.attacks(unit1)