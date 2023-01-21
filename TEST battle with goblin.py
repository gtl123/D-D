import random
import time

#Strength
s1 = random.randint(1,6)
s2 = random.randint(1,6)
s3 = random.randint(1,6)
s4 = random.randint(1,6)
strength = s1 + s2 + s3 + s4

#Dexterity
d1 = random.randint(1,6)
d2 = random.randint(1,6)
d3 = random.randint(1,6)
d4 = random.randint(1,6)
dexterity = d1 + d2 + d3 + d4

#Constitution
c1 = random.randint(1,6)
c2 = random.randint(1,6)
c3 = random.randint(1,6)
c4 = random.randint(1,6)
constitution = c1 + c2 + c3 + c4

#intelligence
i1 = random.randint(1,6)
i2 = random.randint(1,6)
i3 = random.randint(1,6)
i4 = random.randint(1,6)
intelligence = i1 + i2 + i3 + i4

#Wisdom
w1 = random.randint(1,6)
w2 = random.randint(1,6)
w3 = random.randint(1,6)
w4 = random.randint(1,6)
wisdom = w1 + w2 + w3 + w4

#Charisma
ch1 = random.randint(1,6)
ch2 = random.randint(1,6)
ch3 = random.randint(1,6)
ch4 = random.randint(1,6)
charisma = ch1 + ch2 + ch3 + ch4

#Multipliers
sm = random.randint(0,3)
dm = random.randint(0,3)
cm = random.randint(0,3)
im = random.randint(0,3)
wm = random.randint(0,3)
chm = random.randint(0,3)

#listing all variable in groups inputted into other variables
list1 = [s1,s2,s3,s4]
list2 = [d1,d2,d3,d4]
list3 = [c1,c2,c3,c4]
list4 = [i1,i2,i3,i4]
list5 = [w1,w2,w3,w4]
list6 = [ch1,ch2,ch3,ch4]

#ordering variables fron lowest to highest
list1.sort()
list2.sort()
list3.sort()
list4.sort()
list5.sort()
list6.sort()

#old variable are replaced with them but minus the smallest number in their list
strength = strength - list1[0]
dexterity= dexterity - list2[0]
constitution = constitution - list3[0]
intelligence = intelligence - list4[0]
wisdom = wisdom - list5[0]
charisma = charisma - list6[0]


#Goblin health points
GHP = 7
#Goblin armour class
GAC = 15

#health points
HP = 8 + cm
#armour class
AC = 10 + dm


print("A goblin appeared!")
print("It's armoured with leather and has a scimitar with an additional shortbow")




def battleX():
    print("What do you do?")
    print("Option 1 : sword")
    print("Option 2 : longbow")
    option = input("Option:")
    print("**********")
    

    if option == "1":
        mhr = random.randint(1,20) + sm
        if mhr < GAC:
            print("Missed!")
            print("*******")
            battleY()
        else:
            print("SUCCESS!")
            DRS = random.randint(1,6) + 2
            GHP = GHP - DRS
            if GHP <= 0:
                print("Goblin has been eliminated")
                print("**************************")
            else:
                print("The goblin has tooken",DRS,"damage")
                print("**********************************")
                battleY()
            

    if option == "2":
        rhr = random.randint(1,20) + dm
        if rhr < GAC:
            print("Missed!")
            print("*******")
            battleY()
        else:
            print("SUCCESS!")
            DRL = random.randint(1,8)
            GHP = GHP - DRL
            if GHP <= 0:
                print("Goblin has been eliminated")
                print("**************************")
            else:
                print("The goblin has tooken",DRL,"damage")
                print("**********************************")
                battleY()
            
    else:
        battleX()
            


def battleY():
    GCW = random.randint(0,1)

    if GCW == 1:
        print("Goblin is going to use a scimitar")
        GHR = random.randint(1,20) + 4
        if GHR <= AC:
            print("The goblin missed it's attack!")
            battleX()
        
        else:
            print("The goblin has hit it's attack!")
            DRSCG = random.randint(1,6) + 2
            HP = HP - DRSCG
            if HP <= 0:
                print("You have been eliminated!!!")
            else:
                print("You have tooken",DRSCG,"damage")
                print("******************************")
                battleX()
            

    if GCW == 2:
        printt("Goblin is going to use a shortbow")
        GHR = random.randint(1,20) + 4
        if GHR < AC:
            print("The goblin missed it's attack!")
            print("******************************")
            battleX()
        else:
            print("The goblin has hit it's attack!")
            DRSBG = random.randint(1,6) + 2
            HP = HP - DRSBG
            if HP <= 0:
                print("You have been eliminated!!!")
            else:
                print("You have tooken",DRSBG,"damage")
                print("******************************")
                battleX()

battleX(GHP = 7)
        

    
    
    
    

        

    
    

