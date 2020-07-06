from spells import Spell, MagicMissile, Drain, Shield, Poison, Recharge, Effect, ShieldEffect
import itertools

PLAYER_HP = 50
PLAYER_MP = 500
PLAYER_DAMAGE = 0
PLAYER_ARMOR = 0

BOSS_HP = 55
BOSS_MP = 0
BOSS_DAMAGE = 8
BOSS_ARMOR = 0

class LivingObject:
    def __init__(self, hp: int, mp: int, damage: int, armor: int):
        self.hp = hp
        self.mp = mp
        self.damage = damage
        self._armor = armor

        self.effects = []

    @property
    def dead(self) -> bool:
        return self.hp <= 0

    @property
    def armor(self) -> int:
        return self._armor

    def add_effect(self, effect: Effect):
        effect_type = type(effect)
        if any(isinstance(effect, effect_type) for effect in self.effects):
            raise Exception(f"{repr(effect)} is already applied.")

        self.effects.append(effect)

    def tick_effects(self, other: "LivingObject"):
        for effect in self.effects:
            if self.__class__ == Player:
                effect.on_tick(boss=other, player=self)
            else:
                effect.on_tick(boss=self, player=other)
            
        self.effects = [eff for eff in self.effects if eff.counter > 0]

    def normal_attack(self, other: "LivingObject"):
        dmg = self.damage - other.armor
        other.hp -= dmg

        print(f"Boss attacks for {dmg} damage.")

    def cast_spell(self, other: "LivingObject", spell: Spell):
        if self.__class__ == Player:
            spell.on_cast(boss=other, player=self)
        else:
            spell.on_cast(boss=self, player=other)

        self.mp -= spell.mana_cost

class Boss(LivingObject):
    def __init__(self):
        super().__init__(BOSS_HP, BOSS_MP, BOSS_DAMAGE, BOSS_ARMOR)


class Player(LivingObject):
    def __init__(self):
        super().__init__(PLAYER_HP, PLAYER_MP, PLAYER_DAMAGE, PLAYER_ARMOR)

    @property
    def armor(self) -> int:
        if any(isinstance(eff, ShieldEffect) for eff in self.effects):
            return self._armor + 7
        return self._armor


if __name__ == "__main__":
    all_spells = [Poison, MagicMissile, Drain, Recharge, Shield]
    # FIXME:
    # I have no idea how to create the spell sets to check against...
    # Code works fine when checking examples
    spell_sets = []

    mana_winning_totals = []

    for spells in spell_sets:
        player = Player()
        boss = Boss()

        total_mana_costs = 0

        while True:
            # Player turn
            print("\n-- Player turn --")
            print(f"- Player has {player.hp} hit points, {player.armor} armor, {player.mp} mana")
            print(f"- Boss has {boss.hp} hit points")
            player.tick_effects(boss)
            
            boss.tick_effects(player)

            if boss.dead:
                print("Boss kiled by player")
                break

            # attack
            spell = spells.pop()()
            if player.mp <= spell.mana_cost:
                print("Player has no mana to use any more skills.")
                break
            player.cast_spell(boss, spell)
            total_mana_costs += spell.mana_cost

            if boss.dead:
                print("Boss killed by player")
                mana_winning_totals.append(total_mana_costs)
                break

            # Boss turn
            print("\n-- Boss turn --")
            print(f"- Player has {player.hp} hit points, {player.armor} armor, {player.mp} mana")
            print(f"- Boss has {boss.hp} hit points")
            player.tick_effects(boss)
            boss.tick_effects(player)

            if boss.dead:
                print("Boss killed by player")
                mana_winning_totals.append(total_mana_costs)
                break

            # attack
            boss.normal_attack(player)

            if player.dead:
                print("Player killed by boss")
                break

    print("\nResult", min(mana_winning_totals))
