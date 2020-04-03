from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import itertools
import csv
import random
import pandas as pd
import requests
import time


author = 'Your name here'

doc = """
Your app description
"""

def make_field(choice):
    return models.StringField(
        choices=choice,
        label="",
        widget=widgets.RadioSelectHorizontal,
    )
def extend_treatment(list_of_lists):
    treat = []
    for list in list_of_lists:
        treat.extend(10*list)
    return treat

def get_tweets(datafile):
    """Reads in datafile with html and returns them as a list.

    Args: datafile in folder data as string.
    Out: list of htmls.
    """
    with open('data/{}'.format(datafile), newline='') as f:
       reader = pd.read_csv(f)
       tweets = reader['0'].tolist()
       return tweets

class Constants(BaseConstants):
    name_in_url = 'rate_tweets'
    players_per_group = None
    num_participants = 4
    num_rounds = 40

    #Choices for different StringFields
    positive =[["Negativ","Negativ"],["Neutral","Neutral"],["Positiv","Positiv"],["Nicht zutreffend", "Nicht zutreffend"]]
    optimistic = [["Pessimistisch","Pessimistisch"],["Neutral","Neutral"],["Optimistisch","Optimistisch"],["Nicht zutreffend", "Nicht zutreffend"]]
    happiness = [["Verärgert","Verärgert"],["Neutral","Neutral"],["Zufrieden","Zufrieden"],["Nicht zutreffend", "Nicht zutreffend"]]
    emotional = [["Sachlich","Sachlich"],["Emotional","Emotional"],["Nicht zutreffend", "Nicht zutreffend"]]
    choices = [['positive'], ['optimistic'], ['happiness'], ['emotional']]


    tweets = get_tweets("html_test_data.csv")

    # Treatments as list of list.
    treatment_cycles = []
    tweet_cycles = []
    for i in range(num_participants):
        # Makes personalized random cycle of treatment/tweets
        shuffled_rating = random.sample(choices, len(choices))
        shuffled_tweets = random.sample(tweets, len(tweets))
        #Expands treatments to 10 rounds per treatment.
        real_treatments = extend_treatment(shuffled_rating)
        # Turns treatment/tweets into cycles and stores them in a list.
        treatment_cycle = itertools.cycle(real_treatments)
        tweet_cycle = itertools.cycle(shuffled_tweets)

        tweet_cycles.append(tweet_cycle)
        treatment_cycles.append(treatment_cycle)

class Subsession(BaseSubsession):
    def creating_session(self):
        count = 0
        for p in self.get_players():
            p.treatment = next(Constants.treatment_cycles[count])
            p.tweet = next(Constants.tweet_cycles[count])
            count += 1

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    tweet = models.StringField()
    treatment = models.StringField()
    pos_rating = make_field(Constants.positive)
    opt_rating = make_field(Constants.optimistic)
    hap_rating = make_field(Constants.happiness)
    emo_rating = make_field(Constants.emotional)
