from typing import Union
import itertools


class Item:
    def __init__(self, name: str, cost: int, damage: int, armor: int):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __repr__(self) -> str:
        return f"<Item {self.name}>"


class Player:
    def __init__(self, weapon, armor=None, ring_1=None, ring_2=None):
        self._weapon: Union[Item, None] = weapon
        self._armor: Union[Item, None] = armor
        self._ring_1: Union[Item, None] = ring_1
        self._ring_2: Union[Item, None] = ring_2

        self.equipment = [self._weapon, self._armor, self._ring_1, self._ring_2]

        self.hp = 100

    def __repr__(self) -> str:
        eq = ", ".join([eq.name for eq in self.equipment if eq])
        return (f"<Player hp={self.hp} damage={self.damage} armor={self.armor} "
                f"equipment={eq}>")

    @property
    def equipment_cost(self) -> int:
        return sum([eq.cost for eq in self.equipment if eq])
            
    @property
    def damage(self) -> int:
        return sum([eq.damage for eq in self.equipment if eq])

    @property
    def armor(self) -> int:
        return sum([eq.armor for eq in self.equipment if eq])

    def attack(self, boss) -> bool:
        """Returns True if killed, False if still alive"""
        dmg = self.damage - boss.armor
        if dmg < 1:
            dmg = 1

        boss.hp -= dmg

        if boss.hp <= 0:
            return True

        return False


class Boss:
    def __init__(self):
        self.hp = 109
        self.damage = 8
        self.armor = 2

    def __repr__(self) -> str:
        return f"<Boss hp={self.hp} damage={self.damage} armor={self.armor}>"

    def attack(self, player) -> bool:
        """Returns True if killed, False if still alive"""
        dmg = self.damage - player.armor
        if dmg < 1:
            dmg = 1

        player.hp -= dmg

        if player.hp <= 0:
            return True

        return False


if __name__ == "__main__":
    weapons = [Item("Dagger", 8, 4, 0), Item("Shortsword", 10, 5, 0),
               Item("Warhammer", 25, 6, 0), Item("Longsword", 40, 7, 0),
               Item("Greataxe", 74, 8, 0)]

    armor = [Item("Leather", 13, 0, 1), Item("Chainmail", 31, 0, 2),
             Item("Splintmail", 53, 0, 3), Item("Bandedmail", 75, 0, 4),
             Item("Platemail", 102, 0, 5)]

    rings = [Item("Damage +1", 25, 1, 0), Item("Damage +2", 50, 2, 0),
             Item("Damage +3", 100, 3, 0), Item("Defense +1", 20, 0, 1),
             Item("Defense +2", 40, 0, 2), Item("Defense +3", 80, 0, 3)]

    # Create all possible equipment sets
    # weapons
    # weapons + armor
    # weapons + armor + any_ring
    # weapons + armor + ring_1 + ring_2
    # weapons + any ring
    # weapons + ring_1 + ring_2
    weapons_eq = [{"weapon": weapon} for weapon in weapons]
    weapons_ring_eq = [{"weapon": eq[0], "ring_1": eq[1]} for eq in itertools.product(weapons, rings)]
    weapons_armor_eq = [{"weapon": eq[0], "armor": eq[1]} for eq in itertools.product(weapons, armor)]
    weapons_armor_ring_eq = [{"weapon": eq[0], "armor": eq[1], "ring_1": eq[2]} for eq in itertools.product(weapons, armor, rings)]
    weapons_ring_1_and_2_eq = []
    for ring_1 in rings:
        weapons_ring_1_and_2_eq.extend([
            {
                "weapon": eq[0],
                "ring_1": ring_1,
                "ring_2": eq[1]
            } for eq in itertools.product(weapons,
                                          list(filter(lambda r: r is not ring_1, rings)))
        ])
    weapons_armor_ring_1_and_2_eq = []
    for ring_1 in rings:
        weapons_armor_ring_1_and_2_eq.extend([
            {
                "weapon": eq[0],
                "armor": eq[1],
                "ring_1": ring_1,
                "ring_2": eq[2]
            } for eq in itertools.product(weapons,
                                          armor,
                                          list(filter(lambda r: r is not ring_1, rings)))
        ])

    eq_sets = []
    eq_sets.extend(weapons_eq)
    eq_sets.extend(weapons_ring_eq)
    eq_sets.extend(weapons_armor_eq)
    eq_sets.extend(weapons_armor_ring_eq)
    eq_sets.extend(weapons_ring_1_and_2_eq)
    eq_sets.extend(weapons_armor_ring_1_and_2_eq)

    # Turn based stuff
    wins_equipment_costs = []
    print_log = False

    for eq_set in eq_sets:
        player = Player(**eq_set)
        boss = Boss()

        if print_log:
            print(f"{player} vs. {boss}")

        turn_count = 1
        while True:
            if player.attack(boss):
                if print_log:
                    print(f"Round {turn_count+1}")
                    print("Player killed boss")
                wins_equipment_costs.append(player.equipment_cost)
                break

            if boss.attack(player):
                if print_log:
                    print(f"Round {turn_count+1}")
                    print("Boss killed player")
                break

            if print_log:
                print(f"Round {turn_count}")
                print(player)
                print(boss)
                print("------------")

            turn_count += 1

    print(min(wins_equipment_costs))
