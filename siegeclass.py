from unitclass import Unit
import time
import random

class Siege(Unit):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides,
                 weapon_upgrade=None,
                 can_attack_ground=False, can_attack_air=False, air_unit=False):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, can_attack_ground, can_attack_air, air_unit)
        self.weapon_upgrade = weapon_upgrade
        self.choose_upgrades()
        self.get_dice_rolls()

    def choose_upgrades(self):
        self.weapon_upgrade = input(f"choose weapon upgrade for {self.name} from: None, basic, advanced, expert --> ")

    def get_dice_rolls(self):
        if self.weapon_upgrade == "None":
            return
        elif self.weapon_upgrade == "basic":
            self.dice_rolls += 1
        elif self.weapon_upgrade == "advanced":
            self.dice_rolls += 2
        elif self.weapon_upgrade == "expert":
            self.dice_rolls += 3
        else:
            print("Invalid input for weapon upgrade. Choose from: None, basic, advanced, expert.")
            self.choose_upgrades()
            self.get_dice_rolls()