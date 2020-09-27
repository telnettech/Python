class RaceCar:
    def __init__(self, color, fuel_remaining, laps = 0, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = laps 👈#Attribute is set here

        for keys, values in kwargs.items():
            setattr(self, keys, values)

    def run_lap(self, length):
        self.fuel_remaining -= (length * 0.125)
        self.laps += 1👈#This is now valid
