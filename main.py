#!/bin/env python3

################################ Fetch and preprocess ###########################################

import numpy as np
import pandas as pd
import ucimlrepo as uci

# fetch data
df = uci.fetch_ucirepo(id=360).data.features  # entire dataset

# merge date and time columns into a single one
df["Datetime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"], errors="coerce", dayfirst=True
)
df.drop("Date", axis=1, inplace=True)
df.drop("Time", axis=1, inplace=True)

# set missing values to NaN
df.replace(-200.0, np.nan, inplace=True)

# check how many missing values we have per column
missing_summary = df.isna().sum().sort_values(ascending=False)
missing_summary  # TODO: visualize

# NMHC(GT) column has too many missing values (~90%)
# so we discard it
df.drop("NMHC(GT)", axis=1, inplace=True)

# fill remaining missing values with mean
df = df.fillna(df.mean())

#################################################################################################
