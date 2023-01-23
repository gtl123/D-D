from Class import Player
from Class import Monster

print("Starting Tournament")
print("A Vampire appeared!")
print("It's armoured with leather and has a scimitar with an additional shortbow")
p = Player()
m = Monster(_name="Vampire")
rm = 0
while rm != "dead":
    rm = p.attack(attacker_name=m.name,
                  attacker_HP=m.Monster_HP,
                  attacker_strengh=m.Monster_Strengh,
                  attacker_armourClass=m.Monster_ArmourClass,
                  attacker_Emotional_attachment=m.Monster_Emotional_Attachment)
    if rm != None and "dead" and "escaped":
        m.HP = rm
    elif rm == "escaped":
        print("You live happily ")
        break
    elif rm == "dead":
        break
    rm2 = m.attack(p.AC, p.HP)
    if rm2 != None:
        if rm2 == "palyer dead":
            break
        else:
            p.HP = rm2
