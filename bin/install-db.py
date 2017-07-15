#!/usr/bin/env python3

import os
import sys

# Add watchman root directory to sys path to import src modules.
sys.path.append("/".join(os.path.abspath(__file__).split("/")[:-2]))

import src

