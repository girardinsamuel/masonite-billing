"""Billing Settings"""
from masonite.environment import env

DRIVERS = {
    "default": "stripe",
    "stripe": {
        "client": env("STRIPE_CLIENT"),
        "secret": env("STRIPE_SECRET"),
        "currency": "usd",
    },
    "paddle": {
        "client": env("STRIPE_CLIENT"),
        "secret": env("STRIPE_SECRET"),
        "currency": "usd",
    },
}
