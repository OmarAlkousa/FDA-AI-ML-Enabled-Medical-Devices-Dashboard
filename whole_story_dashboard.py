# Import the required packages
import plotly.express as px
import streamlit as st


def viz(df_selection):

    fig = px.treemap(df_selection,
                     path=['year',
                           'field',
                           'Applicant',
                           'Submission Number',
                           'Device'],
                     custom_data=['year', 'field', 'Applicant'])
    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
    fig.update_traces(hovertemplate='<b></b>%{label}\
                      <br>Year= %{customdata[0]}\
                      <br>Medical Field: %{customdata[1]}\
                      <br>Applicant: %{customdata[2]}')
    st.plotly_chart(fig, use_container_width=True)
