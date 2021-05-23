# AGAGD Models Imports
import agagd_core.models as agagd_models

# DJango Imports
import django_tables2
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils.safestring import mark_safe

# Base Bootstrap Column Attributes
default_bootstrap_column_attrs = {
    "th": {"class": "d-none d-lg-table-cell d-xl-table-cell"},
    "td": {"class": "d-none d-lg-table-cell d-xl-table-cell"},
}

# Column for the Winner of the Game
class WinnerColumn(tables.Column):
    def __init__(
        self,
        color="W",
        viewname=None,
        urlconf=None,
        args=None,
        kwargs=None,
        current_app=None,
        attrs=None,
        **extra
    ):
        super().__init__(
            attrs=attrs,
            linkify=dict(
                viewname=viewname,
                urlconf=urlconf,
                args=args,
                kwargs=kwargs,
                current_app=current_app,
            ),
            **extra
        )
        self.color = color

    def render(self, value, record):
        if record.result == self.color:
            self.attrs["td"] = {"class": "winner"}
        else:
            self.attrs["td"] = {"class": "runner-up"}
        return value


# Basic table which is use as as base for many of the game layouts.
class GameTable(tables.Table):
    game_date = tables.Column(verbose_name="Date", attrs=default_bootstrap_column_attrs)
    handicap = tables.Column(attrs=default_bootstrap_column_attrs)
    pin_player_1 = WinnerColumn(
        color="W",
        viewname="member_detail",
        verbose_name="White",
        kwargs={"member_id": tables.A("pin_player_1.member_id")},
    )
    pin_player_2 = WinnerColumn(
        color="B",
        viewname="member_detail",
        verbose_name="Black",
        kwargs={"member_id": tables.A("pin_player_2.member_id")},
    )
    tournament_code = tables.LinkColumn(
        verbose_name="Tournament",
        viewname="tournament_detail",
        kwargs={"tourn_code": tables.A("tournament_code.tournament_code")},
    )
