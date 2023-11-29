import pandas as pd
import numpy as np

# -------------------------------------------------------------------------
def remove_outliers_IQR(df, columns, scale=1.5, mode="replace"):
    outliers = pd.DataFrame()
    outlier_ratios = {}
    for c in columns:
        q1=df[c].quantile(0.25)
        q3=df[c].quantile(0.75)
        iqr = q3-q1
        low_lim = q1 - scale*iqr
        high_lim = q3 + scale*iqr
        # To show what percentage of each column are outliers
        Outs = df[c][(df[c] >= high_lim) | (df[c] <= low_lim)]
        Out_Ratio = 100*(len(Outs)/len(df[c]))
        outlier_ratios[c] = Out_Ratio
        
        # Store outliers in a separate DataFrame
        outliers = pd.concat([outliers, Outs.to_frame()], axis=1)
        
        if mode == "remove":
            indexes = df[c][(df[c] > high_lim) | (df[c] < low_lim)].index
            df.loc[indexes, c] = np.nan # replace outliers with nan
            
        else:
            df[c] = np.where(df[c] >= high_lim, high_lim, np.where(df[c] <= low_lim, low_lim, df[c])) # replace

    return df, outliers

# -------------------------------------------------------------------------
def season(date):
    year = str(date.year)
    seasons = {'spring': pd.date_range(start=year+'/03/21', end=year+'/06/20'),
               'summer': pd.date_range(start=year+'/06/21', end=year+'/09/22'),
               'autumn': pd.date_range(start=year+'/09/23', end=year+'/12/20')}
    if date in seasons['spring']:
        return 'spring'
    if date in seasons['summer']:
        return 'summer'
    if date in seasons['autumn']:
        return 'autumn'
    else:
        return 'winter'
# -------------------------------------------------------------------------