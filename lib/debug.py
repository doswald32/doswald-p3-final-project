#!/usr/bin/env python3
# lib/debug.py

from seed import seed_database
import ipdb

from models.book import Book
from models.patron import Patron

seed_database()

ipdb.set_trace()


