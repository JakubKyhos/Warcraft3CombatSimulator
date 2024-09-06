from unitclass import Unit
import time
import random

class Warior(Unit):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)
        self.weapon_upgrade = ""
        self.armor_upgrade = ""
        self.armor_update()
        self.get_dice_rolls()

    def armor_update(self):
        self.weapon_upgrade = input(f"choose weapon upgrade for {self.name} from: "", basic, advanced, expert --> ")

        if self.armor_upgrade == "":
            return
        elif self.armor_upgrade == "basic":
            self.armor += 2
        elif self.armor_upgrade == "advanced":
            self.armor += 4
        elif self.armor_upgrade == "expert":
            self.armor += 6
        else:
            print("Invalid input for armor upgrade. Choose from: "", basic, advanced, expert.")
            self.armor_update()

    def get_dice_rolls(self):
        self.armor_upgrade = input(f"choose armor upgrade for {self.name} from: "", basic, advanced, expert --> ")

        if self.weapon_upgrade == "":
            return
        elif self.weapon_upgrade == "basic":
            self.dice_rolls += 1
        elif self.weapon_upgrade == "advanced":
            self.dice_rolls += 2
        elif self.weapon_upgrade == "expert":
            self.dice_rolls += 3
        else:
            print("Invalid input for weapon upgrade. Choose from: "", basic, advanced, expert.")
            self.get_dice_rolls()

class Mortar_team(Warior):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)

    def Fragmentation_Shards_upgrade(self,target):
        upgrade = input(f"Do you want Fragmentation Shards upgrade for {self.name}? [y/n] --> ")

        if upgrade == "y" and (target.armor_type == "unarmored" or target.armor_type == "medium"):
            self.damage += 25               # I have no clue how this upgrade works exactly because when I test it in game, it does not seem to make any difference.
        elif upgrade == "n" or target.armor_type != "unarmored" or target.armor_type != "medium":
            return
        else:
            print("Invalid input for Fragmentation Shards upgrade. Choose from: [y/n].")
            self.Fragmentation_Shards_upgrade(target)

class Dragonhawk_Rider(Warior):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)
        self.Animal_War_Training_upgrade()

    def Animal_War_Training_upgrade(self):
        upgrade = input(f"Do you want Animal War Training upgrade for {self.name}? [y/n] --> ")

        if upgrade == "y":
            self.health += 100
        elif upgrade == "n":
            return
        else:
            print("Invalid input for Animal War Training upgrade. Choose from: [y/n].")
            self.Animal_War_Training_upgrade()

class Knight(Dragonhawk_Rider):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)

    def Sundering_Blades_upgarde(self, target):
        upgrade = input(f"Do you want Sundering Blade upgarde for {self.name}? [y/n] --> ")

        if upgrade == "y" and target.armor_type == "medium":
            self.dmgmult += 0.1
        elif upgrade == "n"or target.armor_type != "medium":
            return
        else:
            print("Invalid input for Animal War Training upgrade. Choose from: [y/n].")
            self.Sundering_Blades_upgarde(target)

class Grunt(Warior):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)
        self.Brute_Strength_upgrade()

    def Brute_Strength_upgrade(self):
        upgrade = input(f"Do you want Brute Strength upgrade for {self.name}? [y/n] --> ")

        if upgrade == "y":
            self.health += 125
            self.damage += 3
        elif upgrade == "n":
            return
        else:
            print("Invalid input for Brute Strength upgrade. Choose from: [y/n].")
            self.Brute_Strength_upgrade()