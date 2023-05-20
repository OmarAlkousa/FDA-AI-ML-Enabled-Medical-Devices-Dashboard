# import the required packages
import streamlit as st
import pandas as pd
import plotly.express as px


def viz(df_selection):
    # --- Calculation for top 10 companies --- #
    # The names of the top 10 companies
    applicants = df_selection['Applicant'].value_counts().\
        sort_values(ascending=False).keys()[0:10]

    # Dataframe of the top 10 companies.
    top10 = df_selection[df_selection['Applicant'].isin(applicants)]

    # --- Calculate KPIs --- #
    # Total number of Devices (filter is applied)
    total_top10 = top10.shape[0]

    # The field with the highest number of devices (filter is applied)
    top_field_top10 = top10['field'].value_counts().idxmax()

    # The applicant with the higest number if devices (filter is applied)
    top_applicant_top10 = top10['Applicant'].value_counts().idxmax()

    # The number of devices for the top rated applicant (filter is applied)
    num_top_top10 = top10['Applicant'].value_counts().max()

    ########
    # KPIs #
    ########
    column1kpi, column2kpi, column3kpi = st.columns(3)
    with column1kpi:
        st.subheader(f'{total_top10}')
        st.markdown('AI/ML Devices in Total')
    with column2kpi:
        st.subheader(f'{top_field_top10}')
        st.markdown('The top among other medical fields')
    with column3kpi:
        st.subheader(f'{top_applicant_top10} ({num_top_top10} Devices)')
        st.markdown('The top among other applicants')

    st.markdown('''---''')

    ######################################
    # Bar Chart for the top 10 companies #
    ######################################
    # Cross tabulation of the applicant over the years
    top10_companies = pd.crosstab(index=top10['Applicant'],
                                  columns=top10['year'])

    # Total number of devices for each applicant
    top10_applicant_total = top10_companies.sum(axis=1).sort_values()

    # Bar chart of the total number of devices for each medical field
    fig = px.bar(x=top10_applicant_total.values,
                 y=top10_applicant_total.keys(), text_auto=True)
    # Figure Configuration
    fig.update_layout({'title': {'text': 'Top 10 Applicants',
                                 'font': {'size': 30, 'family': 'Times New Roman, bold'},
                                 'x': 0.5,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                       'xaxis': {'title': None},
                       'yaxis': {'title': None, 'showticklabels': True},
                       'margin': dict(t=150, pad=16)})
    # Sort the bars
    fig.update_yaxes(categoryorder='array',
                     categoryarray=[top10['field'].value_counts().
                                    sort_values(ascending=True).index[i] for i in range(len(top10['field'].unique()))])
    # Set the angle of the text to 0 and hide the hover inforamation
    fig.update_traces(textangle=0,
                      textfont_size=50,
                      selector=dict(type='bar'),
                      hoverinfo='skip',
                      hovertemplate=None)

    # Configure the columns on the main page
    column1, column2b, column3p, column4 = st.columns([1, 2, 2, 1])

    # Plot the bar chart
    column2b.plotly_chart(fig, use_container_width=True)

    ##########################################
    # Donut Chart for the top medical fields #
    ##########################################
    fig = px.pie(top10, names='field', hole=0.6)
    # Set the angle of the text to zero and configure the hover information
    fig.update_traces(textposition='inside', textinfo='percent+label',
                      hovertemplate='Medical Field: %{label}<br>Total Number= %{value}<br>Perecentage= %{percent}')
    # Figure Configuration
    fig.update_layout({'title': {'text': 'Medical Fields',
                                 'font': {'size': 30, 'family': 'Times New Roman, bold'},
                                 'x': 0.51,
                                 'y': 0.84,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                       'margin': dict(l=10, b=50, r=0, t=150),
                       'showlegend': False})
    # Plot the donut chart
    column3p.plotly_chart(fig, use_container_width=True)

    #######################
    # Parallel Categories #
    #######################
    # Extract the names of the top 10 companies
    top_companies = [top10['Applicant'].unique()[i]
                     for i in range(len(top10['Applicant'].unique()))]

    # set a number for each applicant
    colorscale = [i for i in range(0, len(top_companies))]

    # Set an integer value for each applicant for easier color implemenation
    top10['colorscale'] = top10['Applicant'].replace(top_companies, colorscale)

    fig = px.parallel_categories(top10, dimensions=['year', 'Applicant', 'field'],
                                 labels={
                                     'year': 'Year', 'Applicant': 'Applicant', 'field': 'Medical Field'},
                                 color='colorscale',
                                 color_continuous_scale=px.colors.sequential.Viridis)
    # Figure Configuration
    fig.update_layout({'title': {'text': 'The Top 10 Applicants over the Years',
                                 'font': {'size': 30, 'family': 'Times New Roman, bold'},
                                 'x': 0.51,
                                 'y': 0.84,
                                 'xanchor': 'center',
                                 'yanchor': 'top'},
                       'margin': dict(l=0, b=10, r=50, t=150),
                       'showlegend': False})
    # Hide the color bar
    fig.update_coloraxes(showscale=False)
    st.plotly_chart(fig, use_container_width=True)
