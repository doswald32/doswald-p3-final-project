#!/usr/bin/env python3
# lib/debug.py

from models.patron import Patron
from models.book import Book
from seed import seed_database

import ipdb

seed_database()

ipdb.set_trace()


