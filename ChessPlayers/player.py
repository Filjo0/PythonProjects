class Player:
    def __str__(self) -> str:
        if any(char.isdigit() for char in self.dod):
            return "Player: full name is %s, was born in %s in %s and died in %s" % (
                self.full_name, self.country, self.dob, self.dod)
        else:
            return "Player: full name is %s, was born in %s in %s" % (
                self.full_name, self.country, self.dob)

    def __repr__(self) -> str:
        return super().__repr__()

    def __init__(self, last_name, first_name, full_name, country, dob, dod):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.country = country
        self.dob = dob
        self.dod = dod
