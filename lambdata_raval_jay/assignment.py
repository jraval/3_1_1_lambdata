""" Coding Conventions - PEP 8 - State Abbreviations Function """
import pandas
import numpy
from pandas import DataFrame

# TODO: helper function from Assignment
# State abbreviation --> Full Name and vice versa
# FL --> Florida, etc.


def add_state_names_column(my_df):
    """
    Add a column of corresponding state names to a dataframe
    
    Params (my_df) a DataFrame with a column called "abbrev" that has state abbreviations.
    Return a copy of the original dataframe, but with an extra column.
    """
    new_df = my_df.copy()

    names_map = {"CA": "Cali", "CO": "Colorado", "CT": "Connecticut", "NJ": "New Jersey"}

    new_df = df["name"] = new_df["abbrev"].map(names_map)

    return my_df


if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    mapped_df = add_state_names_column(df)

    print(mapped_df.head())




