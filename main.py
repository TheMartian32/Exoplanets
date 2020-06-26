import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
A python script that uses NASA Exoplanet archive data.

"""

# * reading exoplanet csv file.
planets = pd.read_csv("Path to CSV file",
                      error_bad_lines=False, sep=',')


def auto_loc(num1=None, num2=None, num3=None, num4=None):
    """
    A quick function to automatically find and print out selected indexes
    from a dataframe.

    You can leave any of the values as nothing as the default value
    is None.

    Args:
        num1 ([int]): Start column
        num2 ([int]): End of but not including column
        num3 ([int]): Start row
        num4 ([int]): End of but not including row
    """
    try:
        print(planets.iloc[num1:num2, num3:num4])
    except:
        print('Failure to print selected indexes.')
