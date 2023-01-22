from Class import Player
from Class import Goblin

print("Starting Tournament")
print("A goblin appeared!")
print("It's armoured with leather and has a scimitar with an additional shortbow")
p = Player()
G = Goblin()
rm = 0
while rm != "dead":
 rm  = p.attack(G.GAC,G.GHP)
 rm2 = G.attack(p.AC,p.HP)
 if rm2 == "dead":
    break

