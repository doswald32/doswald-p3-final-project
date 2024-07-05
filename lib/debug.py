#!/usr/bin/env python3
# lib/debug.py

from seed import seed_database
from cli import patron_menu
import ipdb

from models.book import Book
from models.patron import Patron
from helpers import *

seed_database()

ipdb.set_trace()


