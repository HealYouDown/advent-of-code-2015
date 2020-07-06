# Effects

class Effect:
    def __init__(self, name: str, duration: int):
        self.name = name
        self.duration = duration

        self.counter = duration

    def __repr__(self):
        return f"<Effect {self.name}>"

    def on_tick(self, boss: "Boss", player: "Player"):
        raise NotImplementedError


class ShieldEffect(Effect):
    def __init__(self):
        super().__init__("Shield", 6)

    def on_tick(self, boss: "Boss", player: "Player"):
        self.counter -= 1
        print(f"Shield timer is now {self.counter}.")


class PoisonEffect(Effect):
    def __init__(self):
        super().__init__("Poison", 6)

    def on_tick(self, boss: "Boss", player: "Player"):
        self.counter -= 1
        print(f"Posion deals 3 damage; its timer is now {self.counter}")
        boss.hp -= 3


class RechargeEffect(Effect):
    def __init__(self):
        super().__init__("Recharge", 5)

    def on_tick(self, boss: "Boss", player: "Player"):
        self.counter -= 1
        print(f"Recharge provides 101 mana; its timer is now {self.counter}")
        player.mp += 101

# Spells

class Spell:
    def __init__(self, name: str, mana_cost: int):
        self.name = name
        self.mana_cost = mana_cost

    def __repr__(self):
        return f"<Spell {self.name}>"

    def on_cast(self, boss: "Boss", player: "Player"):
        raise NotImplementedError


class MagicMissile(Spell):
    def __init__(self):
        super().__init__("Magic Missile", 53)

    def on_cast(self, boss: "Boss", player: "Player"):
        print("Player casts Magic missile, dealing 4 damage.")
        boss.hp -= 4


class Drain(Spell):
    def __init__(self):
        super().__init__("Drain", 73)

    def on_cast(self, boss: "Boss", player: "Player"):
        print("Player casts Drain, dealing 2 damage and healing 2 hit points.")
        boss.hp -= 2
        player.hp += 2


class Shield(Spell):
    def __init__(self):
        super().__init__("Shield", 113)

    def on_cast(self, boss: "Boss", player: "Player"):
        print("Player casts Shield, icreasing armor by 7.")
        player.add_effect(ShieldEffect())


class Poison(Spell):
    def __init__(self):
        super().__init__("Poison", 173)

    def on_cast(self, boss: "Boss", player: "Player"):
        print("Player casts Posion.")
        boss.add_effect(PoisonEffect())


class Recharge(Spell):
    def __init__(self):
        super().__init__("Recharge", 229)

    def on_cast(self, boss: "Boss", player: "Player"):
        print("Player casts Recharge.")
        player.add_effect(RechargeEffect())
