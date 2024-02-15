simport streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import base64

st.set_page_config("Marine Route Optimization")
st.header("Marine Route Optimization")

st.selectbox(label = " Select Route", options = ['Lesbon_Rio_de_Janerio','Mumbai_Dubai'])
submit=st.button("Generate Optimized Marine Route")



def Lesbon_Rio_de_Janerio():


    st.write("Preprocessed Data: ")
    # load the merged and preprocessed data
    data = pd.read_csv("G:\AIMLDS\Projectss\Marine Route optimization\github\preprocessed_data.csv")
    st.write(data)

    st.write("AIS and CMEMS data for the model on: January, April, July, October 2020")

    st.header("Area of interest-Lisbon: 38.716666°N 9.1667°W: Rio de Janeiro: 22.908333°S 43.196389°W")


    st.write("Important features based on normalization of data:")
    norma =Image.open( "G:\AIMLDS\Projectss\Marine Route optimization\github\cop_marine-master\cop_marine-master\imgs\output_9_0.png")
    st.image(norma)

    st.write("Shipping route map")
    route = Image.open("G:\AIMLDS\Projectss\Marine Route optimization\github\cop_marine-master\cop_marine-master\imgs\_area.png")
    st.image(route, use_column_width=True) 

    st.write("Land area in the map")
    land = Image.open("G:\AIMLDS\Projectss\Marine Route optimization\github\cop_marine-master\cop_marine-master\imgs\output_28_0.png")
    st.image(land, use_column_width=True) 


    wave_height = Image.open("G:\AIMLDS\Projectss\Marine Route optimization\github\cop_marine-master\cop_marine-master\imgs\wave_height.png")
    st.image(wave_height, use_column_width=True) 


    st.write("Marine route based on weights calculation using Linear Regression")
    linear_regr = Image.open("G:\AIMLDS\Projectss\Marine Route optimization\github\cop_marine-master\cop_marine-master\imgs\output_35_0.png")
    st.image(linear_regr, use_column_width=True) 


    st.write("Marine route based on weights calculation using Random Forest")
    rand_for = Image.open("G:\AIMLDS\Projectss\Marine Route optimization\github\cop_marine-master\cop_marine-master\imgs\oneday_rf.png")
    st.image(rand_for, use_column_width=True) 


    st.header("Advanced solution: Calculate optimal route based on multiple variables and multiple days")
    multi_rf = Image.open("G:\AIMLDS\Projectss\Marine Route optimization\github\cop_marine-master\cop_marine-master\imgs\output_58_0.png")
    st.image(multi_rf, use_column_width=True) 


    st.header("Fastest Route")
    final = Image.open("G:\AIMLDS\Projectss\Marine Route optimization\github\cop_marine-master\cop_marine-master\imgs\mean.png")
    st.image(final, use_column_width=True)

    st.header("Splitting the route yeilds 5% faster than single day route")

    st.header("Total costs compared to Simple Solution: One day Simple solution:  1.0") 
    st.header("All days mean:  1.0646950242380102")
    st.header("All days splitted:  0.9486024897459013")

if submit:
    response=Lesbon_Rio_de_Janerio()