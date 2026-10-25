class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health
        self.__stamina = stamina

    def _get_health(self):
        return self.__health
    
    def _set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0

    def heals(self, target):
        print('---------------')
        if self.__stamina >= 20:
            print(f'{self.__class__.__name__} накладывает повязку из целебных трав'
                f' {target.__class__.__name__}')
            target._set_health(10)
            self.__stamina -= 20
            print(f'Здоровье у {target.__class__.__name__} повышено до {target._get_health()}'
                f'\nУ {self.__class__.__name__} осталось {self.__stamina} едениц запаса сил')
        else:
            print('Недостаточно сил для использования этой способности.')
        print('---------------')

    def attacks(self, target):
        print('---------------')
        if target._get_health() >= 4:
            print(f'{self.__class__.__name__} наносит урон мечом'
                f' {target.__class__.__name__}')
            target._set_health(-3)
            print(f'Здаровье у {target.__class__.__name__} понижено до {target._get_health()}')
        else:
            print(f'{self.__class__.__name__} наносит полдедний удар и побеждает {target.__class__.__name__}\n {target.__class__.__name__} покидает отряд')
        print('---------------')

    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nStamina: {self.__stamina}')
        print('---------------')

class Mage:
    def __init__(self, health=60, mana=100):
        self.__health = health
        self.__mana = mana

    def _get_health(self):
        return self.__health
    
    def _set_health(self, points):
        self.__health += points
        if self.__health > 60:
            self.__health = 60
        elif self.__health < 0:
            self.__health = 0

    def heals(self, target):
        print('---------------')
        if self.__mana >= 20:
            print(f'{self.__class__.__name__} применяет заклинание лечения'
                f' к {target.__class__.__name__}')
            target._set_health(10)
            self.__mana -= 20
            print(f'Здоровье у {target.__class__.__name__} повышено до {target._get_health()}'
                f'\nУ {self.__class__.__name__} осталось {self.__mana} едениц магии')
        else:
            print('Недостаточно сил для использования этой способности.')
        print('---------------')

    def attacks(self, target):
        print('---------------')
        if target._get_health() >= 4:
            print(f'{self.__class__.__name__} наносит урон магией'
                f' {target.__class__.__name__}')
            target._set_health(-3)
            print(f'Здаровье у {target.__class__.__name__} понижено до {target._get_health()}')
        else:
            print(f'{self.__class__.__name__} наносит последний удар и побеждает {target.__class__.__name__}\n {target.__class__.__name__} покидает отряд')
        print('---------------')
    
    def introduces(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__}',
              f'\nHealth: {self.__health}',
              f'\nMana: {self.__mana}')
        print('---------------')

#unit1 = Warrior(10, 50)
#unit2 = Mage(10, 50)

#unit2.attacks(unit1)
#unit2.attacks(unit1)
#unit2.attacks(unit1)
#unit2.attacks(unit1)