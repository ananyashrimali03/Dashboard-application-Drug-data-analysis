import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Demographics")
st.markdown("This interactive dashboard supports the exploration of the demographics (age, gender, and race) of the people involved in fatal accidental overdoses in Allegheny County.  You can filter by the year of the overdose incident, as well as the primary drug present in the incident.")

df = pd.read_csv("data/overdose_data_021125.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

df['race'] = df['race'].str.replace('W','White')
df['race'] = df['race'].str.replace('B','Black')
df['race'] = df['race'].str.replace('H|A|I|M|O|U','Other', regex=True)
df.dropna(subset = ['race'], inplace=True)

df['sex'] = df['sex'].str.replace('M','Male')
df['sex'] = df['sex'].str.replace('F','Female')

st.subheader("Filters")

column1, column2 = st.columns(2)

with column1:
    minYear = df.death_date_and_time.dt.year.min()
    maxYear = df.death_date_and_time.dt.year.max()
    year_range = st.slider("Filter by year:", minYear, maxYear, (minYear, maxYear))

with column2:
    allDrugs = df['combined_od1'].unique().tolist()
    selectDrugs = st.multiselect("Filter by primary drug present:", allDrugs, default=[])

df_filtered = df[(df.death_date_and_time.dt.year >= year_range[0]) & (df.death_date_and_time.dt.year <= year_range[1])]
if selectDrugs:
    df_filtered = df_filtered[df_filtered['combined_od1'].isin(selectDrugs)]

st.subheader("Visualizations")

year_histogram = alt.Chart(df_filtered).mark_bar().encode(
    alt.X('year(death_date_and_time):T', title='Year'),
    alt.Y('count()', title='Count of Fatal Ovedosses')
).properties(
    title='Year'
)

st.altair_chart(year_histogram, use_container_width=True)

# Create columns for the three graphs
col1, col2, col3 = st.columns(3)

with col1:
    age_histogram = alt.Chart(df_filtered).mark_bar().encode(
        alt.Y('age:Q', bin=True, title='Age'),
        alt.X('count()', title='Count of Fatal Ovedosses')
    ).properties(
        title='Age'
    )
    st.altair_chart(age_histogram, use_container_width=True)

with col2:
    gender_bar_chart = alt.Chart(df_filtered).mark_bar().encode(
        alt.Y('sex:N', title='Gender'),
        alt.X('count()', title='Count of Fatal Ovedosses')
    ).properties(
        title='Gender'
    )
    st.altair_chart(gender_bar_chart, use_container_width=True)

with col3:
    race_bar_chart = alt.Chart(df_filtered).mark_bar().encode(
        alt.Y('race:N', title='Race'),
        alt.X('count()', title='Count of Fatal Ovedosses')
    ).properties(
        title='Race'
    )
    st.altair_chart(race_bar_chart, use_container_width=True)