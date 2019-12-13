class Character:
    MIN_HP = 0
    MIN_SPEED = 0

    def __init__(self, race: str, damage: int, armor: int):
        self._Character__hp = 100
        self._Character__race = race
        self.damage = damage
        self.armor = armor
        self.speed = 100

    def hit_pers(self, hit: int):
        self._Character__hp -= hit
        pass

    def dead(self):
        if self._Character__hp <= Character.MIN_HP:
            return 'You dead'

    @property
    def Character__hp(self):
        if self._Character__hp >= 0:
            return self._Character__hp
        else:
            return 0

    @property
    def Character__race(self):
        return self._Character__race


elf = Character('Elf', 20, 10)
while elf.Character__hp > 0:
    hit_m = int(input('Нанеси урон тваре '))
    elf.hit_pers(hit_m)
    print(f'Осталось {elf.Character__hp} HP')
    if elf.Character__hp <= 0:
        print(elf.dead())
        pass
