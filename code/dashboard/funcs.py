import pandas as pd
import numpy as np
from datetime import datetime as dt

# Function to calculate age of Haruki
def haruki_age(input_date: str) -> dict:
    """
    Calculate Haruki's age in days, weeks, months, and years as floats.
    
    Args:
    input_date (str): The date to calculate Haruki's age for, in the format 'YYYY-MM-DD'.
    
    Returns:
    dict: A dictionary with Haruki's age in days, weeks, months, and years as floats.
    """
    # Haruki's birthday
    birthday = dt(2024, 8, 29)
    
    # Parse the input date
    input_date = dt.strptime(input_date, "%Y-%m-%d")
    
    # Ensure the input date is after Haruki's birthday
    if input_date < birthday:
        return {"error": "The date is before Haruki's birth!"}
    
    # Calculate the total age difference in days
    delta = (input_date - birthday).days
    
    # Calculate age components
    days = delta
    weeks = delta / 7
    months = delta / 30.44  # Approximation of average days per month
    years = delta / 365.25  # Approximation of average days per year including leap years
    
    age = {
        "days": round(days, 2),
        "weeks": round(weeks, 2),
        "months": round(months, 2),
        "years": round(years, 2)
    }
    
    print(f"Haruki's age calculated: {age}")  # Debug print
    return age


# Function to calculate Sullivan's age 
def sullivan_age(input_date: str) -> dict:
    """
    Calculate Sullivan's age in days, weeks, months, and years as floats.
    
    Args:
    input_date (str): The date to calculate Sullivan's age for, in the format 'YYYY-MM-DD'.
    
    Returns:
    dict: A dictionary with Sullivan's age in days, weeks, months, and years as floats.
    """
    # Sullivan's birthday in datetime format
    birthday = dt(2024, 10, 7)
    
    # Parse the input date
    input_date = dt.strptime(input_date, "%Y-%m-%d")
    
    # Ensure the input date is after Sullivan's birthday
    if input_date < birthday:
        return {"error": "The date is before Sullivan's birth!"}
    
    # Calculate the total age difference in days
    delta = (input_date - birthday).days
    
    # Calculate age components
    days = delta
    weeks = delta / 7
    months = delta / 30.44  # Approximation of average days per month
    years = delta / 365.25  # Approximation of average days per year including leap years
    
    age = {
        "days": round(days, 2),
        "weeks": round(weeks, 2),
        "months": round(months, 2),
        "years": round(years, 2)
    }
    
    print(f"Sullivan's age calculated: {age}")  # Debug print
    return age


def age_in_weeks(df):
    """ 
    Desc: calculates the age of cats in weeks based on the date column

    Args: 
        df (pd.DataFrame): dataframe of cat data (cat, weight, date)
    Returns:
        pd.DataFrame: the dataframe with added "weeks" column representing the cat's age in weeks
    """

    from datetime import datetime as dt
    import pandas as pd 

    haruki_birthday = dt(2024, 8, 29)
    sullivan_birthday = dt(2024, 10, 7)

    df['date'] = pd.to_datetime(df['date']) # ensure date col is in dt form

    df.loc[df['cat'] == 'haruki', 'weeks'] = pd.to_numeric((df['date'] - haruki_birthday).dt.days / 7)
    df.loc[df['cat'] == 'sullivan', 'weeks'] = pd.to_numeric((df['date'] - sullivan_birthday).dt.days / 7)

    return df

