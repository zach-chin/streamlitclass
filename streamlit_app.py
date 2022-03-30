
##### This app is just an extremely simple example.
##### See the Streamlit documentation for how to create more complex apps.

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset
baseball = pd.read_csv("player-batting-stats-1988-2016.csv")
# constants for the position and team
pos = "P"
team = "BOS"
# constant for batting statistic (RBI)
batstat = "RBI"

##### Title and intro

st.title( 'Creating a Histogram From baseball Team and batting stat' )


##### Inputs

st.header( 'Choose team and stat' )
team = st.selectbox("Choose a team", baseball.Tm.unique())
batstat = st.selectbox("Choose a batting stat", baseball.columns)


##### Output
baseball_filtered = baseball[baseball.Tm == team]
baseball_sorted = baseball_filtered.sort_values(batstat, ascending=False)
baseball_final = baseball_sorted.head(20)


plt.hist(baseball_filtered[batstat], color="red")
plt.ylabel("Frequency")
plt.xlabel("Number of " + batstat)
plt.title("Histogram for " + batstat + " for " + team)

st.pyplot(plt.gcf())
