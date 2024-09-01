import threading
from unitclass import Unit
from hybridclass import Hybrid
from wariorclass import Warior
from siegeclass import Siege
from mageclass import Mage, SpiritWalker, DruidOfTheClaw

def main():
    test = Mage("shaman",100,5,"piercing",0,"unarmored",1.5,4,None,True,True,True)
    test2 = Hybrid("gargoyle",100,5,10,"normal","piercing",0,"heavy",1,1.5,4,8,None,None,True,True,False)
    if isinstance(test,Hybrid):
        test.enemy_is_air_unit(test2)
    if isinstance(test2,Hybrid):
        test2.enemy_is_air_unit(test)
    test.update_damage_multiplier(test2)
    test2.update_damage_multiplier(test)
    test.calculate_damage_reduction()
    test2.calculate_damage_reduction()
    t1 = threading.Thread(target=test.attack_unit, args=(test2,))
    t2 = threading.Thread(target=test2.attack_unit, args=(test,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    if not test.is_alive():
        print(f"{test.name} is dead {test2.name} has won.")
    if not test2.is_alive():
        print(f"{test2.name} is dead {test.name} has won.")


    print(f"{test.name} has {test.damage} damage, {test.damage_type} type, {test.dmgmult} multyplier, {test.attack_speed} speed, {test.dice_sides} dice sides.")
    print(f"{test2.name} has {test2.damage} damage, {test2.damage_type} type, {test2.dmgmult} multyplier, {test2.attack_speed} speed, {test2.dice_sides} dice sides.")
if __name__=="__main__":
    main()