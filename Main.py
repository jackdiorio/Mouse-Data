import datetime
from Mouse import Mouse #"from (Mouse.py file) import (the class Mouse itself)"

# Keeping example from google sheet (thank you tommy its very well done!)
jesus = Mouse("Jesus", datetime.date(2023, 12, 25), "none", "none", "black", "a", "a")
ophelia = Mouse("Ophelia", datetime.date(2023, 11, 20), "none", "none", "brindle", "Avy", "a")

# Mate them and get punnet square for locus A (only one supported as of yet)
my_punnet = jesus.mate(ophelia, "A")

print(my_punnet)