from algorithm import solve
import sys


if __name__ == "__main__":
    
    while True:
        instructions = []
        chal = False
        challenge = input("Verity challenge?[y/n](enter [e] for exit): ")
        if challenge == "y": chal = True
        if challenge == "e": sys.exit("Program Exit")
        inside = input("Enter inside shape config[x,x,x]: ")
        outside_pre = input("Enter outside shape config[xx,xx,xx]: ")
        outside_pre = outside_pre.split(",")
        outside = []
        for shape in outside_pre:
            outside.append(list(shape))

        print("Outside Shapes: "+str(outside))
        instructions = solve(inside,outside,chal)
        print("####################################################")
        for instr in instructions:
            print(instr)
        print("####################################################")


