#!/usr/bin/env python3
# lib/debug.py

from models.patron import Patron
import datetime

import ipdb

def reset_database():
    Patron.drop_table()
    Patron.create_table()

    Patron.create("Caitlin", "Clark", datetime.date(1999, 4, 21))

ipdb.set_trace()


