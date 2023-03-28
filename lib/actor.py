from .audition import Audition

class Actor:
    
    def __init__(self, name):
        self.name = name


    # returns a list of auditions this actor attended
    @property
    def auditions(self):
        return [a for a in Audition.all if a.actor == self]
    
    # returns a list of roles the actor auditioned for
    @property
    def roles(self):
        return [r for r in self.auditions]
    
    # returns a list of strings with all the different character names
    # this actor auditioned for
    @property
    def characters(self):
        return [n.role.character_name for n in self.auditions]
    
    # returns a list of strings with all the different character names
    #  that this actor has been **hired** for
    @property
    def paychecks(self):
        hired_list = "Position Still Avaiable"
        for role in self.auditions:
            if role.hired == True:
                hired_list = role.actor.name
                return hired_list
        else:
            return hired_list
        