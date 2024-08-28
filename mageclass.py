from unitclass import Unit
import time
import random

class Mage(Unit):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides,
                 upgrade=None,
                 can_attack_ground=False, can_attack_air=False, air_unit=False):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, can_attack_ground, can_attack_air, air_unit)
        self.upgrade = upgrade
        self.choose_upgrade()
        self.has_upgrade()

    def choose_upgrade(self):
        self.upgrade = input(f"choose upgrade for {self.name} from: None, adept, master --> ")

    def has_upgrade(self):
        if self.upgrade == "None":
            return
        elif self.upgrade == "adept":
            self.health += 40
        elif self.upgrade == "master":
            self.health += 80
        else:
            print("Invalid input for upgrade. Choose from: None, adept, master.")
            self.choose_upgrade()
            self.has_upgrade()

class SpiritWalker(Mage):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides,
                 upgrade=None,
                 can_attack_ground=False, can_attack_air=False, air_unit=False):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, upgrade, can_attack_ground, can_attack_air, air_unit)

    def has_upgrade(self):
        if self.upgrade == "None":
            return
        elif self.upgrade == "adept":
            self.health += 60
        elif self.upgrade == "master":
            self.health += 120
        else:
            print("Invalid input for upgrade. Choose from: None, adept, master.")
            self.choose_upgrade()
            self.has_upgrade()

class DruidOfTheClaw(Mage):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides,
                 upgrade=None,
                 can_attack_ground=False, can_attack_air=False, air_unit=False):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, upgrade, can_attack_ground, can_attack_air, air_unit)

    def has_upgrade(self):
        if self.upgrade == "None":
            return
        elif self.upgrade == "adept":
            self.health += 75
        elif self.upgrade == "master":
            self.health += 150
        else:
            print("Invalid input for upgrade. Choose from: None, adept, master.")
            self.choose_upgrade()
            self.has_upgrade()