# Import the required Packages
import streamlit as st
import pandas as pd
import over_the_years_dashboard
import top10_applicants_dashboard
import whole_story_dashboard


# Set Title and icon to the web page
st.set_page_config(page_title='FDA AI/ML Enabled Devices Dashboard',
                   page_icon=':bar_chart:', layout='wide')


# Read the dataset with Caching for faster implementation
@st.cache_data
def get_data_from_excel():
    # Read the excel file
    df = pd.read_excel(io='FDA(AI-ML)-Enabled Medical Devices.xlsx',
                       engine='openpyxl',
                       sheet_name='Sheet1',
                       skiprows=1,
                       usecols='A:E',
                       nrows=523)

    # Generate a column of the year
    df['year'] = df['Date of Final Decision'].dt.strftime('%Y')

    return df


# Read the data set by applying the function
df = get_data_from_excel()


############
# Side Bar #
############
editor = st.sidebar.header(
    'Editor: Omar Alkousa')
contact = st.sidebar.header('Contact: omar.ok1998@gmail.com')
st.sidebar.header('Please Filter Here:')

# Filtering by time
year = st.sidebar.multiselect(label='Select the Year',
                              options=df['year'].unique(),
                              default=df['year'].unique())

# Filtering by medical field
field = st.sidebar.multiselect(label='Select the Medical Field',
                               options=df['field'].unique(),
                               default=df['field'].unique())


# Filter the data
df_selection = df.query('year == @year & field == @field')


#############
# Main Page #
#############

# Set Title
st.title(':bar_chart: FDA AI/ML Enabled Devices Dashboard')
st.markdown('**October 5, 2022 Update**')
st.markdown("##")


# Customize the tabs
over_the_years, top_10_companies, whole_story = st.tabs(['Over The Years',
                                                         'Top 10 Applicants',
                                                         'The Whole Story'])


######################
# Over The Years Tab #
######################
# Dashboard over the years
with over_the_years:
    over_the_years_dashboard.viz(df, df_selection)

# Dashboard of the top 10 companies
with top_10_companies:
    top10_applicants_dashboard.viz(df_selection)

# Dashboard of the whole story
with whole_story:
    whole_story_dashboard.viz(df_selection)


########################
# Styling the Web page #
########################
# --- Enlarge the titles of the tabs --- #
css = '''
    <style>
    .stTabs [data-baseweb='tab-list'] button [data-testid='stMarkdownContainer'] p {
    font-size:2rem;
    }
    </style>
    '''
st.markdown(css, unsafe_allow_html=True)

# ---- HIDE STREAMLIT STYLE ---- #
hide_st_style = '''
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                '''
st.markdown(hide_st_style, unsafe_allow_html=True)
