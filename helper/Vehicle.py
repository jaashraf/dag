class Vehicle:
    def __init__(self, createdAt, color, fuel, type, vehicle, vid, id):
        self.createdAt = createdAt
        self.color = color
        self.fuel = fuel
        self.type = type
        self.vehicle = vehicle
        self.vid = vid
        self.id = id

    def getCreatedAt(self):
        return self.createdAt

    def getColor(self):
        return self.color

    def getFuel(self):
        return self.fuel

    def getType(self):
        return self.type

    def getVehicle(self):
        return self.vehicle

    def getVid(self):
        return self.vid

    def getId(self):
        return self.id

    def __str__(self):
        return self.createdAt + " " + self.color + " " + self.fuel + " " +\
               self.type + " " + self.vehicle + " " + self.vid + " " + self.id