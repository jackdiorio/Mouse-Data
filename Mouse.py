import datetime

# Define mouse class
class Mouse():

    # Class constructor
    def __init__(self, name: str, birthday: datetime, father, mother, 
                 coat_color: str, pied: bool, coat_variety: str):

        # A mouse has a name and birthday
        self.name = name
        self.birthday = birthday

        # Mouse coat colors as standardized by the American Fancy Rat & Mouse
        # Association: https://www.afrma.org/fancymice.htm (ctrl-click link)

        self.coat_color = coat_color # coat colors as listed under SELF
        self.coat_variety = coat_variety # coat varieties

        self.pied = pied

        self.father = father
        self.mother = mother

# Mary and Jospeh are created yesterday (created on 1/25)
mary = Mouse("Mary", datetime.date(2024, 1, 24), "None", "None", "Coffee", False, "Satin")
joe = Mouse("Joseph", datetime.date(2024, 1, 24), "None", "None", "Black", True, "Frizzie")

# Jesus is born from mary and joseph today
jesus = Mouse("Jesus", datetime.datetime.today, joe, mary, "White", False, "Standard")

# Who is jesus' dad?
print("Jesus' father is " + jesus.father.name)