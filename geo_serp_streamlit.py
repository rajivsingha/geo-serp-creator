import streamlit as st
import pandas as pd
import uule_grabber

st.title("GeoLocation Based SERP")

query = st.text_input("enter your search query here", "how to be awesome")
#query = user_input.encode()
#query = "how to choose a football boot"


try:
    @st.cache
    def get_Locations():
        df = pd.read_csv("GeoLocations_o.csv")
        return df.set_index("Location")
except:
    st.write("Error in loading CSV")


df = get_Locations()
geo_location = st.selectbox(
    "Choose countries", list(df.index)
)
num_results = st.slider('Select number of results to display:', 10, 100,10,10)

if not geo_location:
    st.error("Please select at least one location.")
else:
    city = geo_location
    uule_parameter = uule_grabber.uule(city)
    serp_link = "https://www.google.com/search?q="+query+"&oq="+query+"&uule="+uule_parameter+"&hl=en&gl=us"+"&num="+str(num_results)



st.subheader("Click the link below for GEO BASED SERP")

html_string = "<a href='"+serp_link+"' target='_blank'>Link to SERP</a>"
st.markdown(html_string,unsafe_allow_html=True)


