import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Map")
st.markdown("This interactive dashboard supports the exploration of trends of the locations involved in fatal accidental overdoses in Allegheny County. You can filter by the date of the overdose incident, as well as filter locations by the number of incidents.")

df = pd.read_csv("./data/overdose_data_021125.csv")
df['death_date_and_time'] = pd.to_datetime(df['death_date_and_time'])
df['incident_zip'] = pd.to_numeric(df['incident_zip'], errors='coerce')

latlon_zip = pd.read_csv("./data/zipcodes_latlon.csv")
allegheny_zip = pd.read_csv("./data/zipcodes_AlleghenyCounty.csv")

allegheny_zip.columns = allegheny_zip.columns.str.lower()
latlon_zip.columns = latlon_zip.columns.str.lower()
df.columns = df.columns.str.lower()

df = df[df['incident_zip'].isin(allegheny_zip['zipcode'])]

df = df.merge(
latlon_zip, left_on='incident_zip', right_on='zip', how='left')

column1, spacer, column2 = st.columns([2, 1, 2])

with column1:
    min_date = df['death_date_and_time'].min().date()
    max_date = df['death_date_and_time'].max().date()
    start_date, end_date = st.slider("Range", min_value=min_date, max_value=max_date, value=(min_date, max_date))
    df = df[(df['death_date_and_time'] >= pd.to_datetime(start_date)) & (df['death_date_and_time'] <= pd.to_datetime(end_date))]

incident_counts = df.groupby(['incident_zip', 'lat', 'lng']).size().reset_index(name='counts') #Counts number of incidents per zip code

with column2:
    min_incidents, max_incidents = st.slider("How many cases", min_value=int(incident_counts['counts'].min()), max_value=int(incident_counts['counts'].max()), value=(int(incident_counts['counts'].min()), int(incident_counts['counts'].max())))

filtered_data = incident_counts[(incident_counts['counts'] >= min_incidents) & (incident_counts['counts'] <= max_incidents)] #filters data

st.map(filtered_data.rename(columns={'lng': 'lon'})[['lat', 'lon']]) #plots the map with filtered data