class Country:
    def __init__(self, country_info):
        self.country_name = country_info.country
        self.supporters = country_info.supporters

        fan_percent = country_info.fans
        self.fans = self.supporters * fan_percent
        self.spending = country_info.spent
        self.strength = country_info.strength

        self.days_active = 1  # The number of days the team survives the tournament.
        self.active = True  # Determines whether supporters spend money as the tournament progresses.

    def lost(self):
        # This function makes sure supporters don't spend extra money when their team loses.
        self.active = False

    def advance_day(self):
        # This function advances the number of days survived, if the team is still in the tournament.
        if self.active:
            self.days_active += 1

    def num_supporters(self):
        # This function gets the number of ordinary supporters.
        ordinary_supporters = self.supporters - self.fans
        return ordinary_supporters

    def fan_spending(self):
        # This function gets the amount of money spent by fans.
        money = self.fans * self.spending * 18
        return money

    def supporter_spending(self):
        # This function gets the amount of money spent by ordinary supporters.
        supports = self.num_supporters()
        money = supports * self.days_active * self.spending
        return money

    def total_spending(self):
        # This function gets the total amount of money spent by all supporters.
        fan_money = self.fan_spending()
        supporter_money = self.supporter_spending()
        total = fan_money + supporter_money
        return total

    def fans_spent_more(self):
        # This function determines if fans have spent more than ordinary supporters.
        if self.fan_spending() > self.supporter_spending():
            return True
        else:
            return False
