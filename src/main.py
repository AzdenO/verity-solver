from algorithm import solve



if __name__ == "__main__":
    

##INITIALISE#################################################################
    chal = False
    challenge = input("Verity challenge?[y/n]: ")
    if challenge == "y": chal = True
    inside = input("Enter inside shape config[x,x,x]: ")
    outside_pre = input("Enter outside shape config[xx,xx,xx]: ")
    outside_pre = outside_pre.split(",")
    outside = []
    for shape in outside_pre:
        outside.append(list(shape))
##SOLVE######################################################################
    print("Outside Shapes: "+str(outside))
    instructions = solve(inside,outside,chal)
    for instr in instructions:
        print(instr)

#############################################################################
