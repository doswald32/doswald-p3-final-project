#!/usr/bin/env python3
# lib/debug.py

from lib.seed import seed_database
import ipdb

from lib.models.book import Book
from lib.models.patron import Patron

seed_database()

ipdb.set_trace()


