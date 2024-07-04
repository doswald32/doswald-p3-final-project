#!/usr/bin/env python3
# lib/debug.py

from seed import seed_database

import ipdb

seed_database()

ipdb.set_trace()


