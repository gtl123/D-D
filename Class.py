import random
import time

# Strength
s1 = random.randint(1, 6)
s2 = random.randint(1, 6)
s3 = random.randint(1, 6)
s4 = random.randint(1, 6)
strength = s1 + s2 + s3 + s4

# Dexterity
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
d4 = random.randint(1, 6)
dexterity = d1 + d2 + d3 + d4

# Constitution
c1 = random.randint(1, 6)
c2 = random.randint(1, 6)
c3 = random.randint(1, 6)
c4 = random.randint(1, 6)
constitution = c1 + c2 + c3 + c4

# intelligence
i1 = random.randint(1, 6)
i2 = random.randint(1, 6)
i3 = random.randint(1, 6)
i4 = random.randint(1, 6)
intelligence = i1 + i2 + i3 + i4

# Wisdom
w1 = random.randint(1, 6)
w2 = random.randint(1, 6)
w3 = random.randint(1, 6)
w4 = random.randint(1, 6)
wisdom = w1 + w2 + w3 + w4

# Charisma
ch1 = random.randint(1, 6)
ch2 = random.randint(1, 6)
ch3 = random.randint(1, 6)
ch4 = random.randint(1, 6)
charisma = ch1 + ch2 + ch3 + ch4

# Multipliers
sm = random.randint(0, 3)
dm = random.randint(0, 3)
cm = random.randint(0, 3)
im = random.randint(0, 3)
wm = random.randint(0, 3)
chm = random.randint(0, 3)

# listing all variable in groups inputted into other variables
list1 = [s1, s2, s3, s4]
list2 = [d1, d2, d3, d4]
list3 = [c1, c2, c3, c4]
list4 = [i1, i2, i3, i4]
list5 = [w1, w2, w3, w4]
list6 = [ch1, ch2, ch3, ch4]

# ordering variables fron lowest to highest
list1.sort()
list2.sort()
list3.sort()
list4.sort()
list5.sort()
list6.sort()

class Player():

    def __init__(self):
        self.strength = strength - list1[0]
        self.dexterity = dexterity - list2[0]
        self.constitution = constitution - list3[0]
        self.intelligence = intelligence - list4[0]
        self.wisdom = wisdom - list5[0]
        self.charisma = charisma - list6[0]

        # health points
        self.HP = 8 + cm
        # armour class
        self.AC = 10 + dm

    def attack(self,attacker_armourClass,attacker_HP):
        print("What do you do?")
        print("Option 1 : sword")
        print("Option 2 : longbow")
        option = input("Option:")
        print("**********")
        AAC = attacker_armourClass
        AHP = attacker_HP
        if option == "1":
            mhr = random.randint(1, 20) + sm
            if mhr < AAC:
                print("Missed!")
                print("*******")

            else:
                print("SUCCESS!")
                DRS = random.randint(1, 6) + 2
                AHP = AHP - DRS
                if AHP <= 0:
                    print("Goblin has been eliminated")
                    print("**************************")
                    return "dead"
                else:
                    print("The goblin has tooken", DRS, "damage")
                    print("**********************************")


        if option == "2":
            rhr = random.randint(1, 20) + dm
            if rhr < AAC:
                print("Missed!")
                print("*******")

            else:
                print("SUCCESS!")
                DRL = random.randint(1, 8)
                AHP = AHP - DRL
                if AHP <= 0:
                    print("Goblin has been eliminated")
                    print("**************************")
                else:
                    print("The goblin has tooken", DRL, "damage")
                    print("**********************************")


class Goblin():

    def __init__(self):
        # Goblin health points
        self.GHP = 7
        # Goblin armour class
        self.GAC = 15

    def attack(self,player_armourClass,player_HP):

        PAC = player_armourClass # PAC(player_armour class)
        GCW = random.randint(0, 2)
        PHP = player_HP # PHP(Player HP)
        if GCW == 1:
            print("Goblin is going to use a scimitar")
            GHR = random.randint(1, 20) + 4
            if GHR <= PAC:
                print("The goblin missed it's attack!")


        else:
            print("The goblin has hit it's attack!")
            DRSCG = random.randint(1, 6) + 2
            PHP = PHP - DRSCG
            if PHP <= 0:
                print("You have been eliminated!!!")
                return "dead"
            else:
                print("You have tooken", DRSCG, "damage")
                print("******************************")


        if GCW == 2:
            print("Goblin is going to use a shortbow")
            GHR = random.randint(1, 20) + 4
            if GHR < PAC:
                print("The goblin missed it's attack!")
                print("******************************")

            else:
                print("The goblin has hit it's attack!")
                DRSBG = random.randint(1, 6) + 2
                PHP = PHP - DRSBG
                if PHP <= 0:
                    print("You have been eliminated!!!")
                else:
                    print("You have tooken", DRSBG, "damage")
                    print("******************************")

