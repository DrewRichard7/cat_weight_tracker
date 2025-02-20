"""
Cat weights app created in streamlit 
Andrew Richard
2025-02-19
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime as dt
import time
from funcs import age_in_weeks, haruki_age, sullivan_age

# App title
st.title("change in kitten weights over time")

# path to dataset
path = 'weights.csv'

@st.cache_data
def load_weights(path):
    weights = pd.read_csv(path, index_col=False)
    weights = age_in_weeks(weights)
    return weights

# load weights in as weight
weights = load_weights(path)
# add checkbox to optionally toggle raw data display
if st.checkbox('show raw data'):
    st.subheader('raw data')
    st.write(weights)


# create line chart for cat weights by age in weeks
st.subheader("weight change by age in weeks")
st.line_chart(weights, x='weeks', y='weight', color='cat', x_label="age (wks)", y_label="weight (lbs)")

# create line chart for cat weights by date
st.subheader("weight change by date")
st.line_chart(weights, x='date', y='weight', color='cat', x_label="date", y_label="weight (lbs)")


# add cat ages
today_date_str = dt.today().strftime('%Y-%m-%d')
sully_age = sullivan_age(today_date_str)
ruki_age = haruki_age(today_date_str)

# sullivan age 
st.write(f"Sullivan's age: {sully_age['years']} years, {sully_age['months']} months, {sully_age['weeks']} weeks, {sully_age['days']} days")

# haruki age 
st.write(f"Haruki's age: {ruki_age['years']} years, {ruki_age['months']} months, {ruki_age['weeks']} weeks, {ruki_age['days']} days")

