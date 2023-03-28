import ipdb
from lib import *

# Test your code below...

r1 = Role("Cinderella")
r2 = Role("Jasmine")

act1 = Actor("Vanessa")
act2 = Actor("Kimberly")

a1 = Audition("NYC", True, r1, act1)
a2 = Audition("CO", False, r1, act2)
a1 = Audition("FL", False, r2, act1)



# the below line allows us to stop & try stuff!
ipdb.set_trace()