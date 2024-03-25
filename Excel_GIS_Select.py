# This script can be used to select values from an excel file and then select the features that share those same values in ArcGIS Pro.

import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Get spreadsheet file path
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title='Please select the spreadsheet you wish to analyze.')

# Read spreadsheet into pandas
df = pd.read_excel(file_path)

# Get column values and put into list
siteID = df['EPA ID'].tolist()

# ArcGIS analysis
field = 'EPA_ID'

for i in siteID:
    query = "{} = '{}'".format (field, i)
    arcpy.management.SelectLayerByAttribute('Region5_shapefile', 'ADD_TO_SELECTION', query)


### Potential issue is that the values for SITE_ID in boundary shapefile don't always have leading zeros, ###
### some have <null> values, and some have EPA_ID values.                                                 ###