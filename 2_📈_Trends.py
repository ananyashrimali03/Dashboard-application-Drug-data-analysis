import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv("data/overdose_data_021125.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

st.title("Trends")
st.markdown("This interactive dashboard supports the exploration of trends of the primary drugs involved in fatal accidental overdoses in Allegheny County. You can filter by the date of the overdose incident, as well as select the number of top ranked primary drugs to show.")

min_date = df.death_date_and_time.min().date()
max_date = df.death_date_and_time.max().date()
print(min_date, max_date)

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    date_range = st.slider("Range", min_date, max_date, (min_date, max_date))

with col3:
    top_n = st.number_input("How many top drugs?", min_value=1, max_value=20, value=8)

df_filtered = df[(df.death_date_and_time >= pd.to_datetime(date_range[0])) & (df.death_date_and_time <= pd.to_datetime(date_range[1]))]

df_filtered['year'] = df_filtered.death_date_and_time.dt.year
drug_counts = df_filtered.groupby(['year', 'combined_od1']).size().reset_index(name='count')

top_drugs = drug_counts.groupby('combined_od1')['count'].sum().nlargest(top_n).index
drug_counts = drug_counts[drug_counts['combined_od1'].isin(top_drugs)]

#sorted using GPT 4o
drug_counts['total_count'] = drug_counts.groupby('combined_od1')['count'].transform('sum')
drug_counts = drug_counts.sort_values(by='total_count', ascending=False)

area_chart = alt.Chart(drug_counts).mark_area().encode(
    x=alt.X('year:O', title='Fatal overdoses per year', axis=alt.Axis(values=list(range(2004, 2025)), grid=True)),
    y=alt.Y('count:Q', scale=alt.Scale(domain=[0, 400]), axis=alt.Axis(values=[0, 200, 400], grid=True)),
    color=alt.Color('combined_od1:N', legend=None),
    row=alt.Row('combined_od1:N', title='Primary Drug Involved', sort=alt.SortField('total_count', order='descending'))
).properties(
    height=50
)

st.altair_chart(area_chart, use_container_width=True)