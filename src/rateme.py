import random

class Connect:
    def output(self):
        rated = random.randrange(1,100)
        if rated <= 40:
            x = (f"You are ugly {rated}/100. Eww")
        elif rated >= 41 and rated <= 67:
            x = (f"Mehh {rated}/100. Not worthy my time")
        elif rated < 75 and rated >= 68:
            x = (f"You look handsome {rated}/100. OMG pretty hooman")
        else:
            x = (f"Marry me {rated}/100. Here's a kiss 😘")
        
        self.x = x