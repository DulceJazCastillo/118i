import streamlit as st
import pandas as pd
import plotly.express as px 

def display_map(location_data):
    fig = px.scatter_mapbox(location_data, lat='Latitude', lon='Longitude', hover_name='Address')
    fig.update_layout(mapbox_style='open-street-map')
    
    return fig

#set up streamlit page to be wide as default
st.set_page_config(layout='wide')

# setup the file uploader
st.header('Upload a file')
st.write('Upload a CSV file containing housing assistance programs')

uploaded_file = st.file_uploader('Upload location data')

# check if file has been uploaded and display map
if uploaded_file:
    st.header('Housing Assistance Programs Map')
    df = pd.read_csv(uploaded_file,
                     usecols=['City', 'Phone', 'Availability', 'Bed/Bath', 'Accessibility', 'Rent', 'Deposit Info', 'Miscellaneous','Latitude', "Longitude" ])
    df.columns = ['Address', 'Phone', 'Availability', "Bed/Bath", 'Accessibility', 'Rent', 'Deposit', 'Miscellaneous', 'Latitude', 'Longitude']

    px_map = display_map(df)

    st.plotly_chart(px_map)
    