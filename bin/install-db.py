#!/usr/bin/env python3

import os
import sys
import json
import logging

logging.basicConfig(level=logging.DEBUG)

# Add watchman root directory to sys path to import src modules.
ROOT_DIR="/".join(os.path.abspath(__file__).split("/")[:-2])
sys.path.append(ROOT_DIR)

from src.common import dbhandler

# Create db for file_integ_watch
CONF=json.loads(open(ROOT_DIR+"/conf/file_integ_watch.conf").read())
dbname=CONF["dbname"]
dbpath=CONF["dbpath"]
dbhandler.createdb_file_integ_check(dbpath+"/"+dbname)
