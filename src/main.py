from src.algorithm import solve

EXIT = False
CHALLENGE = False

##INITIALISE#################################################################

challenge = input("Verity challenge?[y/n]: ")
if challenge == "y": CHALLENGE = True
inside = input("Enter inside shape config[x,x,x]: ")
outside_pre = input("Enter outside shape config[xx,xx,xx]: ")
outside_pre = outside_pre.split(",")
outside = []
for shape in outside_pre:
    outside.append(list(shape))
##SOLVE######################################################################
print("Outside Shapes: "+str(outside))
instructions = solve(inside,outside,challenge)
for instr in instructions:
    print(instr)

#############################################################################