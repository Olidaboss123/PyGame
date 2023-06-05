class Hawk:

    def __init__(self, species, flying_speed, size, name, dive_speed, dive, fly,
                 screech):
        self.species = "Species: " + species
        self.flying_speed = "Flying speed: " + str(flying_speed)
        self. size = "Size: " + str(size)
        self.name = "Name: " + name
        self.dive_speed = "Dive speed: " + str(dive_speed)
        self.dive = dive
        self.fly = fly
        self.screech = screech

    def dive_now(self):
        print(self.dive)

    def fly_now(self):
        print(self.fly)

    def screech_now(self):
        print(self.screech)
