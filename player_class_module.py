class Player:

    def __init__(self,con,int,wis,str,dex):
        self.con = con
        self.int = int
        self.wis = wis
        self.str = str
        self.dex = dex

    def navigate(self):
        print("The player is navigating")

    def swing(self):
        print("The player swings and gets a random swing score added to his dexterity")

    def heals(self):
        print("The player takes a restorative tincture")