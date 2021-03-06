from django.db import models


class Building(models.Model):
    BuildingName = models.CharField(max_length=20)

    def name(self):
        return (self.BuildingName)

    def __str__(self):
        return (self.BuildingName)


class Location(models.Model):
#    BLDGNum = models.CharField(max_length=4)
    BLDGName = models.ForeignKey(Building, on_delete=models.CASCADE)
    Floor = models.IntegerField()
    RoomNum = models.IntegerField()
    RoomDescription = models.CharField(max_length=50)

    def name(self):
        return (self.BLDGName + "is the location")

    def __str__(self):
        return (str(self.BLDGName) + " " + str(self.RoomNum))

class Supply(models.Model):
    item = models.CharField(max_length=50)

    def __str__(self):
        return (str(self.item))





class Regiment(models.Model):
    # Cannot put the personnel in here or company we need other relational tables.
    RegNum = models.IntegerField()
    RegSupplyLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
    #RegimentSupplyNCO = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    #RegimentSupplyOfficer = models.ForeignKey(Personnel, related_name= "personnel", on_delete=models.CASCADE)

    def __str__(self):
        if self.RegNum == 1:
            return "1st REG"
        elif self.RegNum == 2:
            return "2nd REG"
        elif self.RegNum == 3:
            return "3rd REG"
        elif self.RegNum == 4:
            return "4th REG"

class Company(models.Model):
    CompanyName = models.CharField(max_length=2) #A, B, C, etc.
    #SupplyOfficer = models.ForeignKey(Personnel, related_name = "companies", null=True, on_delete=models.CASCADE ) #Alpha, Bravo, Charlie etc.
    regiment = models.ForeignKey(Regiment, on_delete=models.CASCADE) #1,2,3,4
    #SupplyNCO = models.ForeignKey(Personnel, related_name = "Scompanies", null=True, on_delete=models.CASCADE ) #Go Buffs!  Go Greeks, etc.
    LocationID = models.ForeignKey(Location, on_delete=models.CASCADE) #Buffalos, Greeks.

    def __str__(self):
        return (str(self.CompanyName) + '-' + str(self.regiment))


class Personnel(models.Model):
    xNum = models.CharField(max_length=6)
    jobTitle = models.CharField(max_length=15)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    phoneNum = models.CharField(max_length=10)
    #companyLabel = models.CharField(max_length = 2)
    #regimentLabel = models.ForeignKey(Regiment, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.jobTitle + ": " + self.xNum

# class CompanyHasPersonnel(models.Model):
#     person = models.ForeignKey(Personnel, on_delete=models.CASCADE)
#     Co = models.ForeignKey(Company, on_delete=models.CASCADE)


class CompanyHasSupply(models.Model):
    Item = models.ForeignKey(Supply, on_delete=models.CASCADE) #A, B, C, etc.
    NumAvailable = models.IntegerField() #Alpha, Bravo, Charlie etc.
    CompanyLabel = models.ForeignKey(Company, on_delete=models.CASCADE) #1,2,3,4
    Location = models.ForeignKey(Location, on_delete=models.CASCADE) #Go Buffs!  Go Greeks, etc.
    #Location_ID = models.ForeignKey(Locations, on_delete=models.CASCADE) #Buffalos, Greeks.

    def __str__(self):
        return ("Company " + str(self.CompanyLabel) + " has " + str(self.NumAvailable) + " " + str(self.Item) + "(s)")
        #"You have " + str(self.NumAvailable) + " " + str(self.Item) + "s")


class CompanyNeedsSupply(models.Model):
    Item = models.ForeignKey(Supply, on_delete=models.CASCADE)
    NumRequested = models.IntegerField()
    CompanyLabel = models.ForeignKey(Company, on_delete=models.CASCADE)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return "This company needs " + str(self.NumRequested) + " " + str(self.Item) + "at " + str(self.Location)

class RegHasSupply(models.Model):
    item = models.CharField(max_length=15)
    NumberAvailable = models.IntegerField()
    RegimentID = models.ForeignKey(Regiment, on_delete=models.CASCADE)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return "REG " + str(self.RegimentID) + " has " + str(self.NumberAvailable) + " " + str(self.item) + " at " + str(self.Location)

class RegHasPersonnel(models.Model):
    Reg = models.ForeignKey(Regiment, on_delete=models.CASCADE)
    person = models.ForeignKey(Personnel, on_delete=models.CASCADE)

    def __str__(self):
        return self.person