# This script uses DataComPy to analyze multiple datasets and produce a detailed report of the comparison between them.

import pandas as pd
import datacompy

r5 = 'C:/Users/jbaker/OneDrive - Skeo Solutions/Documents/Region5.xls'
r5_edited = 'C:/Users/jbaker/OneDrive - Skeo Solutions/Documents/Region5_edited.xls'
df1 = pd.read_excel(r5_edited)
df2 = pd.read_excel(r5)

compare = datacompy.Compare(
    df1,
    df2,
    join_columns='EPA_ID',  #You can also specify a list of columns
    abs_tol=0.0001,
    rel_tol=0,
    df1_name='edited',
    df2_name='original')

compare.report(sample_count= 102, column_count= 84, html_file= r'C:\Users\jbaker\OneDrive - Skeo Solutions\Desktop\scripts\report.html')