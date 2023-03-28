from .audition import Audition

class Role:
    
    all = []

    def __init__(self, character_name):
        self.character_name = character_name
        Role.all.append(self)

    # returns all of the auditions associated with this role.
    @property
    def auditions(self):
        return [r for r in Audition.all if r.role == self]
    
    # returns a list of names from the actors associated with this role.
    @property
    def actors(self):
        return [a for a in self.auditions]
    
    # returns a list of locations from the auditions associated with this role.
    @property
    def locations(self):
        return [l.location for l in self.auditions]
    
    # returns a unique list of strings for all the character names
    # who have been hired.
    @classmethod
    def silver_screen(cls):
        hired = list({h for h in cls.all})
        for character in Audition.all:
            if character.hired == True:
                hired = character.role.character_name
                return hired
        else:
            return hired


        
