from Statue import Statue
class Swap:

##################################################################################

    def __init__(self,originShape, originPos, targetShape, targetPos, perfect):
        self.originPos = originPos
        self.originShape = originShape
        self.targetShape = targetShape
        self.targetPos = targetPos
        self.perfect = perfect

##################################################################################

    def __str__(self):
        return f"{Statue(self.originPos).name} {self.originShape} <--> {Statue(self.targetPos).name} {self.targetShape} | Perfect Swap: {self.perfect}"

##################################################################################
