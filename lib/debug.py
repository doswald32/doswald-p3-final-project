#!/usr/bin/env python3
# lib/debug.py

from models.patron import Patron
import datetime

import ipdb

def reset_database():
    Patron.drop_table()
    Patron.create_table()

reset_database()

Keith = Patron("Keith", "Stone", datetime.date(1978, 1, 11))
print(Keith)

Keith.save()
print(Keith)

Amy = Patron("Amy", "Adams", datetime.date(1988, 12, 22))
print(Amy)

Amy.save()
print(Amy)

ipdb.set_trace()


