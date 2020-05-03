#Download libraries
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import geopandas as gpd
from datetime import datetime,timedelta
from datetime import date as dt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import io
import json
import matplotlib.gridspec as gridspec
import math

#Download files
url="https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7"
s=requests.get(url).content
df_hosp=pd.read_csv(io.StringIO(s.decode("utf-8")),sep=';')
df_hosp.jour=pd.to_datetime(df_hosp.jour)
df_hosp.head()
