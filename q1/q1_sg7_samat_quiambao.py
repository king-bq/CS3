class Glassware:
    def __init__(self, capacityIn_mL: float = 250):
        self.capacityIn_mL = capacityIn_mL
        
class Beaker(Glassware):
    def __init__(self, capacityIn_mL: float = 250):
        super().__init__(capacityIn_mL)
        
    def __del__(self):
        print("A beaker is gone.")
        
class Tray:
    def __init__(self):
        self.beakers = [Beaker() for _ in range(5)]
        
    def __del__(self):
        print("Tray is gone.")
        
myTray = Tray()
print(f"A tray with {len(myTray.beakers)} beakers was created.\n")

del myTray
