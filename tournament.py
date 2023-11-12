class Tournament:
    def __init__(self):
        self.day = 1  # This attribute displays the current day of the tournament, mainly used for debugging.

    def match(self, country_a, country_b):
        # This function determines which country is the winner of the match.
        # The country with the highest strength wins.
        # If both countries have equal strength, the winning country comes earlier in the alphabet.
        # The supporters of the losing country go home the next day.
        if country_a.strength > country_b.strength:
            country_b.advance_day()
            country_b.lost()
            return country_a
        elif country_a.strength < country_b.strength:
            country_a.advance_day()
            country_a.lost()
            return country_b
        elif country_a.country_name < country_b.country_name:
            country_b.lost()
            country_b.advance_day()
            return country_a
        else:
            country_a.advance_day()
            country_a.lost()
            return country_b

    def semifinal_match(self, country_a, country_b):
        # This function is for the third-place match.
        if country_a.strength > country_b.strength:
            country_b.lost()
            return country_a
        elif country_a.strength < country_b.strength:
            country_a.lost()
            return country_b
        elif country_a.country_name < country_b.country_name:
            country_b.advance_day()
            return country_a
        else:
            country_a.advance_day()
            return country_b

    def advance_day(self):
        # This function advances the current day of the tournament.
        self.day += 1
