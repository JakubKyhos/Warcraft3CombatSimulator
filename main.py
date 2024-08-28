import threading
from unitclass import Unit
from hybridclass import Hybrid
from wariorclass import Warior
from siegeclass import Siege
from mageclass import Mage, SpiritWalker, DruidOfTheClaw

def main():
    test = Siege("glaive thrower",200,20,"normal",0,"heavy",1.0,18,None,True,False,False)
    test2 = Warior("Troll Headhunter",150,20,"normal",0,"medium",2.31,5,None,None,True,True,True)
    test.update_damage_multiplier(test2)
    test.calculate_damage_reduction()
    test2.update_damage_multiplier(test)
    test2.calculate_damage_reduction()



if __name__=="__main__":
    main()