from unitclass import Unit

class Mage(Unit):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_rolls, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_rolls, dice_sides, unit_type, valid_targets)
        self.upgrade = ""

    def arcane_training(self):
        self.upgrade = input(f"choose upgrade for {self.name} from: "", adept, master --> ")

        if self.upgrade == "":
            return
        elif self.upgrade == "adept":
            self.health += 40
        elif self.upgrade == "master":
            self.health += 80
        else:
            print("Invalid input for upgrade. Choose from: "", adept, master.")
            self.arcane_training()

    def upgrades(self):
        self.arcane_training()

class SpiritWalker(Mage):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_rolls, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_rolls, dice_sides, unit_type, valid_targets)

    def arcane_training(self):
        self.upgrade = input(f"choose upgrade for {self.name} from: "", adept, master --> ")

        if self.upgrade == "":
            return
        elif self.upgrade == "adept":
            self.health += 60
        elif self.upgrade == "master":
            self.health += 120
        else:
            print("Invalid input for upgrade. Choose from: "", adept, master.")
            self.arcane_training()

class DruidOfTheClaw(Mage):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_rolls, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_rolls, dice_sides, unit_type, valid_targets)

    def arcane_training(self):
        self.upgrade = input(f"choose upgrade for {self.name} from: "", adept, master --> ")

        if self.upgrade == "":
            return
        elif self.upgrade == "adept":
            self.health += 75
        elif self.upgrade == "master":
            self.health += 150
        else:
            print("Invalid input for upgrade. Choose from: "", adept, master.")
            self.arcane_training()