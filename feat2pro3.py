import csv 
import streamlit as st
import folium 
from streamlit_folium import st_folium

datafile = 'Affordable_Housing_info.csv'

@st.cache_data 
def read_data():
    def parse_lat_lon(point):
        return point.split("(")[-1].split(")")[0].split()
    
    data = []
    with open(datafile, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        print("reading...")
        for row in reader: 
            longitude, latitude = parse_lat_lon(row['New Georeferenced Column'])
            data.append({
                'name': row['City'],
                'latitude': float(latitude),
                'longitude': float(longitude)
            })
        return data

data = read_data()

STARTING_POINT = (37.36125, -121.90595)
map = folium.Map(location = STARTING_POINT, zoom_start=9)

for city in data:
    location = city['latitude'], city['longitude']
    folium.Marker(location, popup=city['name']).add_to(map)


st.header("Affordable Housing Locations in the Bay Area")

st_folium(map, width=700)
