from unitclass import Unit

class Siege(Unit):
    def __init__(self, name, health, damage, damage_type, armor, armor_type, attack_speed, dice_rolls, dice_sides, unit_type, valid_targets):
        super().__init__(name, health, damage, damage_type, armor, armor_type, attack_speed, dice_rolls, dice_sides, unit_type, valid_targets)
        self.weapon_upgrade = ""

    def get_dice_rolls(self):
        self.weapon_upgrade = input(f"choose weapon upgrade for {self.name} from: "", basic, advanced, expert --> ")

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

    def upgrades(self):
        self.get_dice_rolls()