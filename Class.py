import random


def Roll(d):
    return random.randint(1, int(d))


# Strength
s1 = Roll(6)
s2 = Roll(6)
s3 = Roll(6)
s4 = Roll(6)
strength = s1 + s2 + s3 + s4

# Agility
a1 = Roll(6)
a2 = Roll(6)
a3 = Roll(6)
a4 = Roll(6)
Agility = a1 + a2 + a3 + a4

# Emotional_Attachment
E_A1 = Roll(6)
E_A2 = Roll(6)
E_A3 = Roll(6)
E_A4 = Roll(6)
Emotional_Attachment = E_A1 + E_A2 + E_A3 + E_A4

# intelligence
i1 = Roll(6)
i2 = Roll(6)
i3 = Roll(6)
i4 = Roll(6)
intelligence = i1 + i2 + i3 + i4

# Wisdom
w1 = Roll(6)
w2 = Roll(6)
w3 = Roll(6)
w4 = Roll(6)
wisdom = w1 + w2 + w3 + w4

# Charisma
ch1 = Roll(6)
ch2 = Roll(6)
ch3 = Roll(6)
ch4 = Roll(6)
charisma = ch1 + ch2 + ch3 + ch4

# Multipliers
Strengh_Multipler = Roll(3)
Aglity_Mulitpler = Roll(3)
Emotional_Attachment__Mulitpler = Roll(3)
Inteligence_Mulitpler = Roll(3)
Wisdom_Mulitpler = Roll(3)
Charisma_Mulitpler = Roll(3)

# listing all variable in groups inputted into other variables
list1 = [s1, s2, s3, s4]
list2 = [a1, a2, a3, a4]
list3 = [E_A1, E_A2, E_A3, E_A4]
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


# Emotional Attachment for a monste can range from 0 --> 20


class Player:

    def __init__(self):
        self.strength = strength - list1[0]
        self.Agility = Agility - list2[0]
        self.Emotional_Attachment = Emotional_Attachment - list3[0]
        self.intelligence = intelligence - list4[0]
        self.wisdom = wisdom - list5[0]
        self.charisma = charisma - list6[0]

        # health points
        self.HP = 8 + Emotional_Attachment__Mulitpler
        # armour class
        self.AC = 10 + Aglity_Mulitpler

    def attack(self, attacker_name, attacker_armourClass, attacker_HP, attacker_strengh, attacker_Emotional_attachment):
        print("What do you do?")
        print("Option 1 : RUN")
        print("Option 2 : FIGHT")
        print("Option 3 : Declare Truce")
        option = input("Option:")
        print("**********")
        if option == "1":
            if attacker_strengh > self.strength:
                Metres = self.strength + 23
                print(
                    f"you Run for your life as the {attacker_name} chases you sadly after {Metres} metres your energy depleats and the {attacker_name} is behind you ")
                print(f"Ha HA HA where will you go now ?? says the {attacker_name}")
            else:
                print(f"You manage to escape the {attacker_name}")
                return "escaped"
        elif option == "2":
            print("What do you use?")
            print("Option 1 : Sword")
            print("Option 2 : dagger")
            print("Option 3 : a spell")
            option = input("Option:")
            print("**********")
            if option == "1":
                Damage_armour = Roll(20) + Strengh_Multipler
                if Damage_armour < attacker_armourClass:
                    print("Missed!")
                    print("*******")
                else:
                    print("SUCCESS!")
                    Damage_hp = Roll(10) + 5
                    attacker_HP = attacker_HP - Damage_hp
                    if attacker_HP <= 0:
                        print(f"{attacker_name} has been eliminated")
                        print("**************************")
                        return "dead"
                    else:
                        print(f"The {attacker_name} has taken", Damage_hp, "damage")
                        print("**********************************")
                        return Damage_hp

            elif option == "2":
                Damage_armour = Roll(10) + Strengh_Multipler
                if Damage_armour < attacker_armourClass:
                    print("Missed!")
                    print("*******")
                else:
                    print("SUCCESS!")
                    Damage_hp = Roll(6) + 2
                    attacker_HP = attacker_HP - Damage_hp
                    if attacker_HP <= 0:
                        print(f"{attacker_name} has been eliminated")
                        print("**************************")
                        return "dead"
                    else:
                        print(f"The {attacker_name} has taken", Damage_hp, "damage")
                        print("**********************************")
                        return Damage_hp

            elif option == "3":
                print("You say a spell will it work ?")
                Damage_armour = Roll(10) + Inteligence_Mulitpler
                if Damage_armour < attacker_armourClass:
                    print("Sadly your souls power is still too weak ")
                    print("******************************************")
                else:
                    print("SUCCESS! Looks like Your spell worked ")
                    print("******************************************")
                    Damage_hp = Roll(6) + 2
                    attacker_HP = attacker_HP - Damage_hp
                    if attacker_HP <= 0:
                        print(f"WOW! The {attacker_name} has pulled back and has been eliminated well done")
                        print("***************************************************************************")
                        return "dead"
                    else:
                        print(f"The {attacker_name} has taken", Damage_hp, "damage")
                        print("***************************************************")
                        return Damage_hp
            else:
                print("INVALID ENTRY")

        elif option == "3":
            Probablity_of_acceptance = Roll(100 * (attacker_Emotional_attachment / 20))
            if Probablity_of_acceptance == 1:
                print(f"fThe {attacker_name} Looks Down at you and admires your attachment to his kind")
                print(f"I guess i will find food some where else ")
                print(f"The {attacker_name} walks away util you cannot see him ")
                print(f"Your Intelligence{self.intelligence} increase by one ")
                self.intelligence += 1

            else:
                print("Ha Ha Ha did you really think your sadness will affect me !!")
                print("DIEEE DIEEE!!")


class Monster:

    def __init__(self, _name):
        self.Monster_HP = Roll(20) + 5
        self.Monster_ArmourClass = Roll(20) + 5
        self.name = _name
        self.Monster_Emotional_Attachment = Roll(20)
        self.Monster_Strengh = Roll(20)+10

    def attack(self, player_armourClass, player_HP):
        GCW = Roll(2)
        Player_HP = player_HP  # Player_HP(Player HP)
        if GCW == 1:
            print(f"{self.name} is going to use a scimitar")
            GHR = Roll(20) + 4
            if GHR <= player_armourClass:
                print(f"The {self.name} missed it's attack!")


        else:
            print(f"The {self.name} has hit it's attack!")
            Damage = Roll(6) + 2
            Player_HP = Player_HP - Damage
            if Player_HP <= 0:
                print("You have been eliminated!!!")
                return "player dead"
            else:
                print("You have taken", Damage, "damage")
                print("******************************")
                return Damage

        if GCW == 2:
            print(f"{self.name} is going to use a shortbow")
            GHR = Roll(20) + 4
            if GHR < player_armourClass:
                print(f"The {self.name}  missed it's attack!")
                print("******************************")

            else:
                print(f"The {self.name}  has hit it's attack!")
                Damage = Roll(6) + 2
                Player_HP = Player_HP - Damage
                if Player_HP <= 0:
                    print("You have been eliminated!!!")
                    return "player dead"
                else:
                    print("You have tooken", Damage, "damage")
                    print("******************************")
                    return Damage