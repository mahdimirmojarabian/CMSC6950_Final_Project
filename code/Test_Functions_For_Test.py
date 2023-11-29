import pandas as pd
import numpy as np
import pytest

from Functions_For_Test import *

# -------------------------------------------------------------------------
@pytest.mark.parametrize("df, columns, scale, mode, expected_df, expected_outliers", [
    # Test case for mode="replace", scale=1.5
    (pd.DataFrame({'A': [1, 2, 3, 4, 5, 100], 'B': [1, -100, 3, 4, 5, 6]}), ['A', 'B'], 1.5, "replace",
     pd.DataFrame({'A': [1.0, 2.0, 3.0, 4.0, 5.0, 8.5], 'B': [1.000, -3.375, 3.000, 4.000, 5.000, 6.000]}),
     pd.DataFrame({'A': [100.0, np.nan], 'B': [np.nan, -100.0]})),
     
    # Test case for mode="remove", scale=1.5
    (pd.DataFrame({'A': [1, 2, 3, 4, 5, 100], 'B': [1, -100, 3, 4, 5, 6]}), ['A', 'B'], 1.5, "remove",
     pd.DataFrame({'A': [1.0, 2.0, 3.0, 4.0, 5.0, np.nan], 'B': [1.0, np.nan, 3.0, 4.0, 5.0, 6.0]}),
     pd.DataFrame({'A': [100.0, np.nan], 'B': [np.nan, -100.0]})),
     
    # Test case for mode="replace", scale=2
    (pd.DataFrame({'A': [1, 2, 3, 4, 5, 100], 'B': [1, -100, 3, 4, 5, 6]}), ['A', 'B'], 2, "replace",
     pd.DataFrame({'A': [1.00, 2.00, 3.00, 4.00, 5.00, 9.75], 'B': [1.0, -5.0, 3.0, 4.0, 5.0, 6.0]}),
     pd.DataFrame({'A': [100.0, np.nan], 'B': [np.nan, -100.0]})),
     
    # Test case for mode="remove", scale=2
    (pd.DataFrame({'A': [1, 2, 3, 4, 5, 100], 'B': [1, -100, 3, 4, 5, 6]}), ['A', 'B'], 2, "remove",
     pd.DataFrame({'A': [1.0, 2.0, 3.0, 4.0, 5.0, np.nan], 'B': [1.0, np.nan, 3.0, 4.0, 5.0, 6.0]}),
     pd.DataFrame({'A': [100.0, np.nan], 'B': [np.nan, -100.0]})),
     
    # Test case for mode not mentioned (default to "replace"), scale not mentioned (default to 1.5)
    (pd.DataFrame({'A': [1, 2, 3, 4, 5, 100], 'B': [1, -100, 3, 4, 5, 6]}), ['A', 'B'], None, None,
     pd.DataFrame({'A': [1.0, 2.0, 3.0, 4.0, 5.0, 8.5], 'B': [1.000, -3.375, 3.000, 4.000, 5.000, 6.000]}),
     pd.DataFrame({'A': [100.0, np.nan], 'B': [np.nan, -100.0]})),
])
def test_remove_outliers_IQR(df, columns, scale, mode, expected_df, expected_outliers):
    if scale is None and mode is None:
        result_df, result_outliers = remove_outliers_IQR(df, columns)
    else:
        result_df, result_outliers = remove_outliers_IQR(df, columns, scale, mode)

    result_df.reset_index(drop=True, inplace=True)
    result_outliers.reset_index(drop=True, inplace=True)

    pd.testing.assert_frame_equal(result_df, expected_df)
    pd.testing.assert_frame_equal(result_outliers, expected_outliers)

# -------------------------------------------------------------------------
@pytest.mark.parametrize("date, expected", [
    # Spring
    (pd.Timestamp('2004-03-21'), 'spring'),
    (pd.Timestamp('2004-04-15'), 'spring'),
    (pd.Timestamp('2004-06-20'), 'spring'),
    # Summer
    (pd.Timestamp('2004-06-21'), 'summer'),
    (pd.Timestamp('2004-07-15'), 'summer'),
    (pd.Timestamp('2004-09-22'), 'summer'),
    # Autumn
    (pd.Timestamp('2004-09-23'), 'autumn'),
    (pd.Timestamp('2004-10-15'), 'autumn'),
    (pd.Timestamp('2004-12-20'), 'autumn'),
    # Winter
    (pd.Timestamp('2004-12-21'), 'winter'),
    (pd.Timestamp('2005-01-15'), 'winter'),
    (pd.Timestamp('2005-02-28'), 'winter'),
])
def test_season(date, expected):
    assert season(date) == expected
# -------------------------------------------------------------------------