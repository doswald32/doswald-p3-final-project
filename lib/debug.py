#!/usr/bin/env python3
# lib/debug.py

from models.patron import Patron

import ipdb

def reset_database():
    Patron.drop_table()
    Patron.create_table()

reset_database()

Keith = Patron("Keith", "Stone", 34)
Amy = Patron("Amy", "Adams", 46)

Keith.save()
Amy.save()

ipdb.set_trace()


