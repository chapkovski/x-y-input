from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Input(Page):
    form_model = 'player'
    form_fields = ['x','y']


class Results(Page):
    pass

page_sequence = [
    Input,
    Results
]
