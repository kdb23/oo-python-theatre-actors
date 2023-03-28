
class Audition:
    
    all = []

    def __init__(self, location, hired, role, actor):
        self.location = location
        self.hired = hired
        self.role = role
        self.actor = actor
        Audition.all.append(self)

    @property
    def call_back(self):
        self.hired = True