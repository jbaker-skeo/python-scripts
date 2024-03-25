# This script analyzes an excel file exported from ArcGIS to extract only the exact columns needed from regrid's parcel data.
import arcpy
import pandas as pd
file = arcpy.GetParameterAsText(0)
folder = arcpy.GetParameterAsText(1)
# Read spreadsheet into pandas
df = pd.read_excel(file)
# Extracted columns
newColumns = df[['szip','parcelnumb', 'address', 'owner', 'saleprice', 'saledate', 'zoning' 'usedesc', 'gisacre', 'lat', 'lon']]
# Export to excel
newColumns.to_csv(folder + "/Refined_Regrid_Data.csv")