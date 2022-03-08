import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.backends.backend_agg import RendererAgg

#Load df
url = https://github.com/max-lutz/national-assembly/blob/main/data/df_dep.csv
url2 = https://github.com/max-lutz/national-assembly/blob/main/data/df_polpar.csv

df_dep = pd.read_csv(url)
df_dep = pd.read_csv(url2)

df_dep