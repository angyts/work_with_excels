import pandas as pd

def dataframe_difference(df1, df2, outpath, which=None):
    """Find rows which are different between two DataFrames."""
    comparison_df = df1.merge(df2,
                              indicator=True,
                              how='outer')
    if which is None:
        diff_df = comparison_df[comparison_df['_merge'] != 'both']
    else:
        diff_df = comparison_df[comparison_df['_merge'] == which]
    diff_df = diff_df[diff_df.columns[:-1]]
    _, filetype = outpath.split('.')
    if filetype == 'csv':
        diff_df.to_csv(outpath)
    else: 
        diff_df.to_excel(outpath)
    return diff_df




#################################################################################################
# TO DO:
# reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
# change input file paths
# change output file paths
# if input file type is csv, uncomment pd.read_csv(.) instead
#################################################################################################

## change input file paths
df1 = pd.read_excel(io='ComparisonData.xlsx',sheet_name='Sheet1')
df2 = pd.read_excel(io='ComparisonData.xlsx',sheet_name='Sheet2')
# df1 = pd.read_csv('df1.csv')
# df2 = pd.read_csv('df2.csv')


## change output file paths (supports csv, xls, xlsx, xlsm, xlsb, odf)
dataframe_difference(df1,df2,'both.xlsx',which='both')
dataframe_difference(df1,df2,'df1_only.xlsx',which='left_only')
dataframe_difference(df1,df2,'df2_only.xlsx',which='right_only')