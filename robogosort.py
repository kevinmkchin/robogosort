#ROBOgosort

import random

class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power

mark = Robot("MARK", 100)
alexa = Robot("ALEXA", 69)
bastion = Robot("NERF BASTION", 200)
codsworth = Robot("CODSWORTH", 77)
jeff = Robot("JEFF", 400)

robots = [mark, alexa, bastion, codsworth, jeff]

def sorted(robots):
    for i in range(len(robots)-1):
        if(robots[i].power < robots[i+1].power):
            return False
    return True

c = 0
while not sorted(robots):
    input("try sorting...")
    c += 1
    random.shuffle(robots)

print("fck robots")
print("Took {0} tries".format(c))
for r in robots:
    print ("Robot: {0} - Power: {1}".format(r.name, r.power))
