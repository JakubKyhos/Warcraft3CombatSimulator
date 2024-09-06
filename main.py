import threading
from unitclass import Unit, Kodo_Beast, Dire_Wolf
from hybridclass import Hybrid, Flying_Machine
from wariorclass import Warior, Mortar_team, Dragonhawk_Rider, Knight
from siegeclass import Siege
from mageclass import Mage, SpiritWalker, DruidOfTheClaw

def main():
    test = Dire_Wolf("Dire Wolf",100,5,"normal",0,"unarmored",1.5,4,"range",["air","range","melee"])
    test2 = Flying_Machine("Flying machine",100,5,10,"normal","piercing",0,"heavy",1,1.5,4,8,"air",["air"])
    if isinstance(test,Hybrid):
        test.enemy_is_air_unit(test2)
    if isinstance(test2,Hybrid):
        test2.enemy_is_air_unit(test)
    if isinstance(test,Mortar_team):
        test.Fragmentation_Shards_upgrade(test2)
    if isinstance(test2,Mortar_team):
        test2.Fragmentation_Shards_upgrade(test)
    test.update_damage_multiplier(test2)
    test2.update_damage_multiplier(test)
    if isinstance(test,Knight):
        test.Sundering_Blades_upgarde(test2)
    if isinstance(test2,Knight):
        test2.Sundering_Blades_upgarde(test)
    if isinstance(test,Kodo_Beast):
        test.War_Drums_upgrade()
    if isinstance(test2,Kodo_Beast):
        test2.War_Drums_upgrade()
    test.calculate_damage_reduction()
    test2.calculate_damage_reduction()
    t1 = threading.Thread(target=test.attack_unit, args=(test2,))
    t2 = threading.Thread(target=test2.attack_unit, args=(test,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    if not test.is_alive():
        print(f"{test2.name} has won with {test2.health} health.")
    if not test2.is_alive():
        print(f"{test.name} has won with {test.health} health.")


    print(f"{test.name} has {test.damage} damage, {test.damage_type} type, {test.dmgmult} multyplier, {test.attack_speed} speed, {test.dice_sides} dice sides.")
    print(f"{test2.name} has {test2.damage} damage, {test2.damage_type} type, {test2.dmgmult} multyplier, {test2.attack_speed} speed, {test2.dice_sides} dice sides.")
if __name__=="__main__":
    main()