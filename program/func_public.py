import pandas as pd
import numpy as np
from pprint import pprint
import time

from func_utils import get_ISO_times
from constants import RESOLUTION

# get relevant time periods for ISO from and to
ISO_TIMES = get_ISO_times()
pprint(ISO_TIMES)

def construct_market_prices(client):
    pass