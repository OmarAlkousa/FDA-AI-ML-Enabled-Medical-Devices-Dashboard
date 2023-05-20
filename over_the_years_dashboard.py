# Import the required packages
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def viz(df, df_selection):
    # --- Calculate KPIs --- #
    # Total number of Devices (filter is applied)
    total = df_selection.shape[0]

    # The field with the highest number of devices (filter is applied)
    top_field = df_selection['field'].value_counts().idxmax()

    # The Applicant with the higest number of devices (filter is applied)
    top_applicant = df_selection.loc[df['field'] ==
                                     top_field]['Applicant'].value_counts().idxmax()

    # The number of devices for the top rated Applicant (filter is applied)
    num_top = df_selection.loc[df['field'] ==
                               top_field]['Applicant'].value_counts().max()

    ########
    # KPIs #
    ########
    column1, column2, column3 = st.columns(3)
    with column1:
        st.subheader(f'{total}')
        st.markdown('AI/ML Devices in Total')
    with column2:
        st.subheader(f'{top_field}')
        st.markdown('The top among other medical fields')
    with column3:
        st.subheader(f'{top_applicant} ({num_top} Devices)')
        st.markdown('The top among other companies')

    st.markdown('''---''')

    ############################
    # Line plot over the years #
    ############################
    # Filtering is not applied
    each_year = df['year'].value_counts().sort_index(ascending=True)

    # Line Plot
    fig = px.line(x=each_year.keys(), y=each_year.values, markers=True)
    # Figure Configuration
    fig.update_layout({'title': {'text': 'Number of AI/ML-Enabled Medical Devices Over the Years (1995 is the start)',
                                 'font': {'size': 20, 'family': 'Times New Roman, bold'},
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                       'xaxis': {'title': 'Year', 'tickvals': df['year'].unique()},
                       'yaxis': {'title': 'Number of Devices'},
                       'hovermode': 'x unified'})

    # Configure the hover information
    fig.update_traces(hovertemplate='Count= %{y}')
    st.plotly_chart(fig, use_container_width=True)

    #########################
    # Heatmap and Bar chart #
    #########################
    # Cross tabulation of Medical fields vs Time
    df_field = pd.crosstab(index=df_selection['field'],
                           columns=df_selection['year'])

    # Total number of devices for each field
    field_total = df_field.sum(axis=1)

    # Set the columns
    column1, column2 = st.columns([3, 1])

    # Heatmap Plot
    fig = go.Figure(data=go.Heatmap(z=df_field.values,
                                    x=df_field.columns,
                                    y=df_field.index,
                                    text=df_field.values,
                                    texttemplate='%{text}',
                                    colorscale='Blues'))
    # Figure Configuration
    fig.update_layout({'title': {'text': 'Number of Devices for Each Medical Field Over the Years',
                                 'font': {'size': 20, 'family': 'Times New Roman, bold'},
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                       'xaxis': {'title': 'Year', 'tickvals': df['year'].unique()},
                       'yaxis': {'title': 'Medical Field'}})

    # Sort the bars
    fig.update_yaxes(categoryorder='array',
                     categoryarray=[df_selection['field'].value_counts().sort_values(ascending=True).
                                    index[i] for i in range(len(df_selection['field'].unique()))])
    # Hide the colorbar and configure the hover information
    fig.update_traces(showscale=False,
                      hovertemplate='Year= %{x}<br>Field: %{y}<br>Count= %{z}<extra></extra>')
    column1.plotly_chart(fig, use_container_width=True)

    # Bar chart of the total number of devices for each medical field
    fig = px.bar(x=field_total.values, y=field_total.keys(), text_auto=True)
    # Figure Configuration
    fig.update_layout({'title': {'text': 'Total',
                                 'font': {'size': 18, 'family': 'Times New Roman, bold'},
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                       'xaxis': {'title': 'Number of Devices', 'title_standoff': 28},
                       'yaxis': {'title': None, 'showticklabels': False},
                       'hovermode': 'y unified',
                       'margin': dict(t=100, pad=16)})

    # Sort the categories
    fig.update_yaxes(categoryorder='array',
                     categoryarray=[df_selection['field'].value_counts().sort_values(ascending=True).
                                    index[i] for i in range(len(df_selection['field'].unique()))])

    # Set the angle of the text to 0 and configure the hover information
    fig.update_traces(textangle=0,
                      textfont_size=50,
                      selector=dict(type='bar'),
                      hovertemplate='Count= %{x}')
    column2.plotly_chart(fig, use_container_width=True)
