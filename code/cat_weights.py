# .py file for cat weight calculator
# Author: Andrew Richard
#fdsa Date: 2025-02-01
# Version: 1.0
# Description: This program plots the weight of my cats over time, and calculates their age based on their birthdates.

# Importing necessary libraries
import plotly.express as px
import pandas as pd 
import numpy as np
from datetime import datetime as dt
from dash import Dash, dcc, html, Input, Output

# some colors I want to use
yellow_color = '#FFD96E'
blue_color = '#3F4C5D'

# Haruki Script 
haruki_dict = {
    '2024-11-4':2,
    '2024-11-13':2.6875,
    '2024-11-17':2.875,
    '2024-11-24':3.1875,
    '2024-11-29':3.3125,
    '2024-12-13':3.875,
    '2024-12-27':4.85,
    '2025-01-03':5,
    '2025-01-07':5.0625,
    '2025-01-11':5.1875,
    '2025-01-13':5.25,
    '2025-01-17':5.625,
    '2025-01-20':5.75,
    '2025-01-24':5.8125,
    '2025-01-28':5.9375,
    '2025-02-01':6.1875
    }
date_haruki = pd.to_datetime(
    list(
        haruki_dict.keys()
        )
        )
weight_haruki = list(haruki_dict.values())
Haruki = pd.DataFrame({'Date':date_haruki, 'Weight (lbs)':weight_haruki})
Haruki['Date']=Haruki['Date'].dt.date
Haruki
fig = px.line(Haruki,
           x=date_haruki,
           y=weight_haruki,
           hover_data=["Date", "Weight (lbs)"],
           labels={'x':'Date Weighed', 'y':'Weight (lbs)'},
           title = "Haruki's Weight Tracker",
           markers='o'
)
fig.show()

# Sullivan Script
sullivan_dict = {
    '2024-12-02':3.125,
    '2024-12-07':3.0625,
    '2024-12-13':3.5625,
    '2024-12-17':3.75,
    '2024-12-27': 3.09,
    '2025-01-03':3.3125,
    '2025-01-07':3.8125,
    '2025-01-11':3.8125,
    '2025-01-13':4.1875,
    '2025-01-17':4.3125,
    '2025-01-20':4.5625,
    '2025-01-24':4.75,
    '2025-01-28':4.9375,
    '2025-02-01':5.25
    }
date_sullivan = pd.to_datetime(list(sullivan_dict.keys()))
weight_sullivan = list(sullivan_dict.values())
Sullivan = pd.DataFrame({'Date':date_sullivan, 'Weight (lbs)':weight_sullivan})
Sullivan['Date']=Sullivan['Date'].dt.date
Sullivan
fig = px.line(Sullivan,
           x=date_sullivan,
           y=weight_sullivan,
           hover_data=["Date", "Weight (lbs)"],
           labels={'x':'Date Weighed', 'y':'Weight (lbs)'},
           title = "Sullivan's Weight Tracker",
           markers='o'
)
fig.add_vrect(x0='2024-12-18', x1='2024-12-27', 
              annotation_text="Sullivan was sick", annotation_position="top left",
              annotation=dict(font_color=blue_color),fillcolor=yellow_color, opacity=0.35, line_width=0)
fig.show()


# Function to calculate age of Haruki
def haruki_age(input_date: 'str') -> dict:
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
    
    return {
        "days": round(days, 2),
        "weeks": round(weeks, 2),
        "months": round(months, 2),
        "years": round(years, 2)
    }


# Function to calculate Sullivan's age 
def sullivan_age(input_date:str) -> dict:
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
    
    return {
        "days": round(days, 2),
        "weeks": round(weeks, 2),
        "months": round(months, 2),
        "years": round(years, 2)
    }


# Create a plotly line plot with both cats weights plotted in 
# terms of age, rather than discrete time
# Cat birthdays
haruki_birthday = dt(2024, 8, 29)
sullivan_birthday = dt(2024, 10, 7)

# Combine the weights into a DataFrame aligned by age in weeks
data = []

# Process Haruki's data
for date, weight in haruki_dict.items():
    date_obj = dt.strptime(date, "%Y-%m-%d")
    weeks_since_birth = (date_obj - haruki_birthday).days / 7
    data.append({
        "Age in Weeks": weeks_since_birth,
        "Weight (lbs)": weight,
        "Cat": "Haruki"
    })

# Process Sullivan's data
for date, weight in sullivan_dict.items():
    date_obj = dt.strptime(date, "%Y-%m-%d")
    weeks_since_birth = (date_obj - sullivan_birthday).days / 7
    data.append({
        "Age in Weeks": weeks_since_birth,
        "Weight (lbs)": weight,
        "Cat": "Sullivan"
    })

# Create a DataFrame
df = pd.DataFrame(data)

# Create the line plot
fig = px.line(
    df, 
    x="Age in Weeks", 
    y="Weight (lbs)", 
    color="Cat", 
    title=f"Weight of Haruki and Sullivan by Age in Weeks<br><sup>Last Rendered: {dt.today().strftime('%Y-%m-%d')}, -- Haruki's Age: {haruki_age(dt.today().strftime('%Y-%m-%d'))} || Sullivan's Age: {sullivan_age(dt.today().strftime('%Y-%m-%d'))}</sup>",
    markers=True,
    labels={"Weight (lbs)": "Weight (lbs)", "Age in Weeks": "Age in Weeks"}
)

fig.show()

# fig.write_image("../assets/both_cats_weigths.png")
# fig.write_html("../assets/both_cats_weights.html")

