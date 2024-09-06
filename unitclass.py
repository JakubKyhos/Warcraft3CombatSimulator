import time
import random

class Unit:
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides,
                unit_type, valid_targets):

        self.name = name
        self.health = health
        self.damage = damage
        self.damage_type = damage_type
        self.armor = armor
        self.armor_type = armor_type
        self.attack_speed = attack_speed
        self.dice_sides = dice_sides
        self.unit_type = unit_type
        self.valid_targets = valid_targets
        self.dice_rolls = 1
        self.damage_reduction = 0.0
        self.dmgmult = 1.0

    def update_damage_multiplier(self, target):
        damage_multipliers = {("normal", "medium"): 1.5,
                            ("normal", "fortified"): 0.7,
                            ("piercing", "medium"): 0.75,
                            ("piercing", "light"): 2,
                            ("piercing", "unarmored"): 1.5,
                            ("piercing", "fortified"): 0.35,
                            ("magic", "heavy"): 2,
                            ("magic", "medium"): 0.75,
                            ("magic", "light"): 1.25,
                            ("magic", "fortified"): 0.35,
                            ("siege", "medium"): 0.5,
                            ("siege", "unarmored"): 1.5,
                            ("siege", "fortified"): 2
                            }

        key = (self.damage_type, target.armor_type)
        self.dmgmult = damage_multipliers.get(key, 1.0)

    def calculate_damage(self):
        new_damage = 0
        num_of_rolls = self.dice_rolls
        while num_of_rolls > 0:
            roll = random.randrange(1,self.dice_sides+1)
            new_damage += roll
            num_of_rolls -= 1
        return new_damage
    
    def calculate_damage_reduction(self):
        self.damage_reduction = (self.armor * 0.06) / (1 + 0.06 * self.armor)

    def can_attack_unit(self, target):
        return target.unit_type in self.valid_targets
    
    def crit_chance(self):
            return 1.0
    
    def attack_unit(self,target):
        while self.is_alive() and target.is_alive():
            time.sleep(self.attack_speed)
            if not self.is_alive():
                return
            elif not target.is_alive():
                return
            new_damage = self.calculate_damage()
            crit = self.crit_chance()
            if not self.can_attack_unit(target):
                print(f"{self.name} can't attack {target.name}.")
                return
            total_damage = round((self.damage + new_damage) * self.dmgmult * (1 - target.damage_reduction) * crit)
            target.health -= total_damage
            print(f"{self.name} does {total_damage} damage, leaving {target.name} with {target.health} health.")

    def is_alive(self):
        return self.health > 0

class Kodo_Beast(Unit):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)

    def War_Drums_upgrade(self):
        upgrade = input(f"Do you want War Drums upgrade for {self.name}? [y/n] --> ")

        if upgrade == "y":
            self.dmgmult += 0.2
        elif upgrade == "n":
            self.dmgmult += 0.1
        else:
            print("Invalid input for War Drums upgrade. Choose from: [y/n].")
            self.War_Drums_upgrade()

class Dire_Wolf(Unit):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)

    def crit_chance(self):
        return 2.0 if random.random() < 0.2 else 1.0