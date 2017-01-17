#!/usr/bin/python3
import csv
import pandas as pd

example = "example.csv"

locations = pd.read_csv(example, names=['Type', 'EID', 'Name', 'ID'])


eidList = locations.groupby('Type')['EID'].apply(list)
