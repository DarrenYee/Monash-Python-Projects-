""" Version 0 of Task 1 and 2. Some problems need to be fixed before its ready for submission. Class concept might be wrong.
"""


class Fighters:

    def _init_ (self, life: int, experience: int) -> None:                                              #initialise for fighter catagory
        """ Precondition: life and experience value must be greater or equal to 0 """
        if life < 0 or experience < 0:
            raise ValueError
        self.life = life
        self.experience = experience

    def is_alive(self) -> bool:                                                                         #function in class to check if life is over 0 (therefore unit is alive)
        if self.life <= 0:
            return False
        return True

    def lose_life(self, lost_life : int) -> None:                                                       #function for the program to decrease health with the number entered
        if lost_life < 0:                           #checks precondition
            raise ValueError
        self.life -= lost_life

    def gain_experience (self, gained_experience: int):
        if gained_experience <0:                       #checks precondition
            raise ValueError
        self.experience += gained_experience

    def get_experience (self) -> int:                                                                   #function to get experience
        return self.experience

    def get_speed (self) -> int:                                                                        #function to get speed
        return self.speed

    def get_cost (self) -> int:                                                                         #function to get cost
        return self.cost

    def attack_damage (self) -> int:                                                                    #function to get damage
        return self.damage

    def defend (self, damage:int):                                                                      #function to check for defense against attack
        if damage < 0 :                             #checks precondition
            raise ValueError
        self.life -= damage

    def __str__(self) -> str:
        return str(self, self.life, self.experience)

class Soldier (Fighters):
    def _init_(self, life: 3, experience: 0, cost: 1,speed: 1) -> None:                        #initialises the soldier class
        self.life = life
        self. experience = experience
        self.cost = cost
        self.speed = speed + self.experience

    def is_alive(self) -> bool:                                                                 #inherited from fighter class
        if self.life <= 0:
            return False
        return True

    def experience(self):                                                                       #inherited from fighter class
        if self.life > 0:
            self.experience += 1

    def attack_damage(self) -> int:                                                             #modified according to soldier's own stats
        return 1+ self.experience

    def defend(self, damage: int):
        if damage < 0:                                                                          # checks precondition
            raise ValueError
        self.life -= damage

    def gain_experience(self, gained_experience: 1):                                            #for exp gains
        if gained_experience < 0:  # checks precondition
            raise ValueError
        self.experience += gained_experience

    def defend (self, damage:int):                                                              #modified
        if damage < 0 :                             #checks precondition
            raise ValueError
        self.life -= damage

    def lose_life(self, lost_life : 1) -> None:                                                 #function for the program to decrease health with the number entered
        if lost_life < 0:                           #checks precondition
            raise ValueError
        self.life -= lost_life

class Archer (Fighters):                                                                        #initialises the archer class
    def _init_(self, life: 3, experience: 0, cost: 2,speed: 3) -> None:
        self.life = life
        self.experience = experience
        self.cost = cost
        self.speed = speed

    def is_alive(self) -> bool:
        if self.life <= 0:
            return False
        return True

    def experience(self):
        if self.life > 0:
            self.experience += 1

    def attack_damage(self) -> int:
        return 1+ self.experience

    def defend (self, damage:int):
        if damage < 0 :                             #checks precondition
            raise ValueError
        if damage > self.experience:
            self.life -=1

    def gain_experience(self, gained_experience: 1):
        if gained_experience < 0:  # checks precondition
            raise ValueError
        self.experience += gained_experience

    def defend (self, damage:int):
        if damage < 0 :                             #checks precondition
            raise ValueError
        self.life -= damage

    def lose_life(self, lost_life : 1) -> None:                                                 #function for the program to decrease health with the number entered
        if lost_life < 0:                           #checks precondition
            raise ValueError
        self.life -= lost_life



class Cavalry (Fighters):                                                                       #initialises the cavalry class
    def _init_(self, life: 4, experience: 0, cost: 3,speed: 2) -> None:
        self.life = 4
        self.experience = 0
        self.cost = 3
        self.speed = 2

    def is_alive(self) -> bool:
        if self.life <= 0:
            return False
        return True

    def experience(self):
        if self.life > 0:
            self.experience += 1

    def attack_damage(self) -> int:
        return 2* self.experience

    def defend (self, damage:int):
        if damage < 0 :                             #checks precondition
            raise ValueError
        self.life -= damage

    def gain_experience(self, gained_experience: 1):
        if gained_experience < 0:  # checks precondition
            raise ValueError
        self.experience += gained_experience

    def defend (self, damage:int):
        if damage < 0 :                             #checks precondition
            raise ValueError
        if damage > (self.experience/2):
            self.life-=damage


    def lose_life(self, lost_life : 1) -> None:                                                       #function for the program to decrease health with the number entered
        if lost_life < 0:                           #checks precondition
            raise ValueError
        self.life -= lost_life




