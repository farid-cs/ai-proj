#!/bin/env python3

import pandas

data = pandas.read_csv('dataset/AirQualityUCI.csv', sep=';')
print(data.head())
