class SouthParkCharacter:
    def __init__(self, name, catchphrase, health, weapon):
        self.name = name
        self.catchphrase = catchphrase
        self.health = health
        self.weapon = weapon
    def speak(self):
        print(self.name + ": " + self.catchphrase)

    def take_damage(self, amount):
        print(self.name + " takes " + str(amount) + " damage!")
        if self.weapon:
            print("Wait! " + self.name + " has " + str(self.weapon) + " equipped, so he lose only " + str(amount // 2) + " damage!")
            self.health -= amount // 2
        
        print(self.name + " has " + str(self.health) + " health remaining.")


cartman = SouthParkCharacter("Cartman", "Respect my authoritah!", 100, "knife")
kenny = SouthParkCharacter("Kenny", "Mmmph mmmph!", 80, "slingshot")
stan = SouthParkCharacter("Stan", "Oh my God, they killed Kenny!", 90, "baseball bat")

cartman.speak()
kenny.speak()
stan.speak()
cartman.take_damage(20)
kenny.take_damage(10)
stan.take_damage(15)
