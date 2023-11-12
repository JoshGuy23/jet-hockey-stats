import pandas
from country import Country
from tournament import Tournament

# Read in data
data = pandas.read_csv("country_info.csv")


def round_1(competitors, tourney):
    # This function covers the round one matches.
    # In round 1, there are 2 matches per day.
    winners = []
    i = 0
    while i < len(competitors):
        competitor_1 = competitors[i]
        competitor_2 = competitors[i+1]
        competitor_3 = competitors[i+2]
        competitor_4 = competitors[i+3]

        # Get the winners of each match.
        winner_1 = tourney.match(competitor_1, competitor_2)
        winner_2 = tourney.match(competitor_3, competitor_4)

        winners.append(winner_1)
        winners.append(winner_2)

        i += 4

        # Advance to the next day.
        for c in competitors:
            c.advance_day()
        tourney.advance_day()
    return winners


def quarterfinals(competitors, tourney):
    # This function covers the quarterfinal matches
    winners = []
    i = 0
    while i < len(competitors):
        competitor_1 = competitors[i]
        competitor_2 = competitors[i+1]

        # Get the winners of the quarterfinals.
        winner = tourney.match(competitor_1, competitor_2)
        winners.append(winner)

        i += 2
        # Advance to the next day.
        for c in competitors:
            c.advance_day()
        tourney.advance_day()
    return winners


def semifinals(competitors, losers, tourney):
    # This function covers the semifinal matches.
    winners = []
    i = 0
    while i < len(competitors):
        competitor_1 = competitors[i]
        competitor_2 = competitors[i+1]

        # Get the winners of each semifinal match.
        winner = tourney.match(competitor_1, competitor_2)
        winners.append(winner)

        # Get the loser of each semifinal mathc.
        if winner == competitor_1:
            competitor_2.active = True
            losers.append(competitor_2)
        else:
            competitor_1.active = True
            losers.append(competitor_1)

        i += 2
        # Advance to the next day.
        for c in competitors:
            c.advance_day()
        tourney.advance_day()
    return winners


def finals(competitors, losers, tourney):
    # This function covers the finals matches.
    finalists = []

    # Get the third-place winner.
    third = tourney.semifinal_match(losers[0], losers[1])
    third.lost()

    # Advance to the day of the final match.
    for c in competitors:
        c.advance_day()
    tourney.advance_day()

    # Get the winner of the tournament.
    competitor_1 = competitors[0]
    competitor_2 = competitors[1]
    winner = tourney.match(competitor_1, competitor_2)

    # Get the top 3 finalists.
    finalists.append(winner)
    if winner == competitor_1:
        finalists.append(competitor_2)
    else:
        finalists.append(competitor_1)
    finalists.append(third)

    # Advance to the final day of the tournament.
    for c in competitors:
        c.advance_day()
    tourney.advance_day()

    return finalists


def basic_scenario():
    # This function covers questions 1-7.
    # The competing teams are from Abragda to Peaceland.
    competing_list = [Country(data.iloc[i]) for i in range(16)]
    disqualified_list = [Country(data.iloc[i]) for i in range(16, len(data))]
    tourney = Tournament()

    # Make sure the noncompeting teams don't count toward the final total.
    for c in disqualified_list:
        c.lost()

    # Get the round-1 winners.
    r1_winners = round_1(competitors=competing_list, tourney=tourney)

    # Advance the days to the beginning of the quarterfinals.
    for _ in range(2):
        for c in r1_winners:
            c.advance_day()
        tourney.advance_day()

    # Get the winners of the quarterfinals.
    qf_winners = quarterfinals(competitors=r1_winners, tourney=tourney)

    # Advance the days to the beginning of the semifinals.
    for c in qf_winners:
        c.advance_day()
    tourney.advance_day()

    # Get the winners and losers of the semifinals.
    losers = []
    sf_winners = semifinals(competitors=qf_winners, losers=losers, tourney=tourney)

    # Advance the days to the beginning of the finals.
    for _ in range(2):
        for c in sf_winners:
            c.advance_day()
        for lost in losers:
            lost.advance_day()
        tourney.advance_day()

    # Get the top 3 finalists.
    finalists = finals(competitors=sf_winners, losers=losers, tourney=tourney)
    print(f"The winner is {finalists[0].country_name}.")
    print(f"Second place is {finalists[1].country_name}.")
    print(f"Third place is {finalists[2].country_name}.")

    # Display the amount of days that ordinary supporters from Konka spent at the tournament.
    print(f"Ordinary Konkan supporters spent {competing_list[10].days_active} days in Fantastan.")

    fans = 0
    for c in competing_list:
        fans += c.fans

    for d in disqualified_list:
        fans += d.fans

    # Display the amount of fans that attended the tournament.
    print(f"A total number of {round(fans)} fans came to see the tournament.")

    supporters = 0
    for c in competing_list:
        supporters += c.num_supporters()

    # Display the amount of ordinary supporters that attended the tournament.
    print(f"A total number of {round(supporters)} ordinary supporters came to see the tournament.")

    fan_spending = 0
    for c in competing_list:
        fan_spending += c.fan_spending()

    for d in disqualified_list:
        fan_spending += d.fan_spending()

    # Display the total amount of money spent by fans.
    print(f"Fans spent a total of ${round(fan_spending)} during the tournament.")

    overzealous_fans = 0
    for c in competing_list:
        if c.fans_spent_more():
            overzealous_fans += 1

    # Display the number of participating teams whose fans spent more than the ordinary supporters.
    print(f"For {overzealous_fans} teams, fans spent more than ordinary supporters.")

    total_money = fan_spending
    for c in competing_list:
        total_money += c.supporter_spending()

    # Display the total amount of money made during the tournament.
    print(f"In total, ${round(total_money)} was made from fan and supporter spending.")


def alternate_scenario():
    # This function covers questions 8-9.
    # The competing countries are Fantastan and Lumania to Zamlos.
    competing_list = [Country(data.iloc[i]) for i in range(11, len(data))]
    competing_list.reverse()
    competing_list.append(Country(data.iloc[5]))

    disqualified_list = [Country(data.iloc[i]) for i in range(11) if i != 5]
    tourney = Tournament()

    # Make sure the noncompeting teams don't count toward the final total.
    for c in disqualified_list:
        c.lost()

    # Get the round-1 winners.
    r1_winners = round_1(competitors=competing_list, tourney=tourney)

    # Advance the days to the beginning of the quarterfinals.
    for _ in range(2):
        for c in r1_winners:
            c.advance_day()
        tourney.advance_day()

    # Get the quarterfinal winners.
    qf_winners = quarterfinals(competitors=r1_winners, tourney=tourney)

    # Advance the days to the beginning of the semifinals.
    for c in qf_winners:
        c.advance_day()
    tourney.advance_day()

    # Get the winners and losers of the semifinals.
    losers = []
    sf_winners = semifinals(competitors=qf_winners, losers=losers, tourney=tourney)

    # Advance the days to the beginning of the finals.
    for _ in range(2):
        for c in sf_winners:
            c.advance_day()

        for lost in losers:
            lost.advance_day()
        tourney.advance_day()

    # Get the top 3 finalists.
    finalists = finals(competitors=sf_winners, losers=losers, tourney=tourney)
    print(f"The winner is {finalists[0].country_name}.")
    print(f"Second place is {finalists[1].country_name}.")
    print(f"Third place is {finalists[2].country_name}.")

    total_spent = 0
    for c in competing_list:
        total_spent += c.total_spending()

    for d in disqualified_list:
        total_spent += d.fan_spending()

    # Display the total amount of money spent during the tournament.
    print(f"In total, ${round(total_spent)} was spent.")

    # Find the name of the country whose supporters spent the most at the tournament.
    spending_team = [c.country_name for c in competing_list]
    spending_amount = [c.total_spending() for c in competing_list]

    max_spending = max(spending_amount)
    index = spending_amount.index(max_spending)
    max_spender = spending_team[index]

    print(f"The supporters and fans of the team from {max_spender} spent the most money.")


basic_scenario()
# alternate_scenario()
