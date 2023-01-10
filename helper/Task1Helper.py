import csv
import datetime
import os.path

import requests
import json


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
        return self.createdAt + " " + self.color + " " + self.fuel + " " + \
               self.type + " " + self.vehicle + " " + self.vid + " " + self.id


url = "https://63a15662e3113e5a5c526b1f.mockapi.io/api/v1/vehicles"
filepath = "/Users/jaashraf/Desktop/dag/Data/"
csvHeader = ['createdAt', 'color', 'fuel', 'type', 'vehicle', 'vid', 'id']
vehicleFuelTypes = set(('Diesel', 'Electric', 'Gasoline', 'Hybrid'))


def getVehicleListAsJson():
    os.environ["no_proxy"] = "*"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Cannot access " + url + " . Response code : " + str(response.status_code))


def putDataIntoCSV(vehicleListJsonData, fuelType):
    vehicleList = convertJsonToObjectList(vehicleListJsonData)
    for item in vehicleList:
        if item.getFuel() == fuelType:
            row = [item.getCreatedAt, item.getColor,
                   item.getFuel, item.getType, item.getVehicle,
                   item.getVid, item.getId]
            f = open(filepath + "vehicle_" + item + ".csv", 'w')
            writer = csv.writer(f)
            writer.writerow(row)


def convertJsonToObjectList(jsonData):
    vehicleList = []
    for item in jsonData:
        vehicle = Vehicle(item["createdAt"], item["color"],
                          item["fuel"], item["type"],
                          item["vehicle"], item["vid"], item["id"])
        vehicleFuelTypes.add(item["fuel"])
        print(vehicle)
        vehicleList.append(vehicle)
    return vehicleList


# Function to create CSV files for the data storage
def createCSVFilesBasedFuelTypes():
    for item in vehicleFuelTypes:
        if not os.path.exists(filepath + "vehicle_" + item + ".csv"):
            f = open(filepath + "vehicle_" + item + ".csv", 'w')
            writer = csv.writer(f)
            writer.writerow(csvHeader)