from unitclass import Unit
import time
import random

class Mage(Unit):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)
        self.upgrade = ""
        self.choose_upgrade()
        self.has_upgrade()

    def choose_upgrade(self):
        self.upgrade = input(f"choose upgrade for {self.name} from: "", adept, master --> ")

    def has_upgrade(self):
        if self.upgrade == "":
            return
        elif self.upgrade == "adept":
            self.health += 40
        elif self.upgrade == "master":
            self.health += 80
        else:
            print("Invalid input for upgrade. Choose from: "", adept, master.")
            self.choose_upgrade()
            self.has_upgrade()

class SpiritWalker(Mage):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)

    def has_upgrade(self):
        if self.upgrade == "":
            return
        elif self.upgrade == "adept":
            self.health += 60
        elif self.upgrade == "master":
            self.health += 120
        else:
            print("Invalid input for upgrade. Choose from: "", adept, master.")
            self.choose_upgrade()
            self.has_upgrade()

class DruidOfTheClaw(Mage):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_sides, unit_type, valid_targets)

    def has_upgrade(self):
        if self.upgrade == "":
            return
        elif self.upgrade == "adept":
            self.health += 75
        elif self.upgrade == "master":
            self.health += 150
        else:
            print("Invalid input for upgrade. Choose from: "", adept, master.")
            self.choose_upgrade()
            self.has_upgrade()