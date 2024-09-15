import streamlit as st
import pandas as pd
import helper
import plotly.express as px
import matplotlib
#reading the Dataset

st.title("Welcome to Cilmate Change Analysis")

far = pd.DataFrame()
df = pd.read_csv("climate_change_indicators.csv")
df = df.dropna()
df.drop_duplicates()

far['Country'] = df["Country"]
temp = ['F1961', 'F1962',
           'F1963', 'F1964', 'F1965', 'F1966', 'F1967', 'F1968', 'F1969', 'F1970',
           'F1971', 'F1972', 'F1973', 'F1974', 'F1975', 'F1976', 'F1977', 'F1978',
           'F1979', 'F1980', 'F1981', 'F1982', 'F1983', 'F1984', 'F1985', 'F1986',
           'F1987', 'F1988', 'F1989', 'F1990', 'F1991', 'F1992', 'F1993', 'F1994',
           'F1995', 'F1996', 'F1997', 'F1998', 'F1999', 'F2000', 'F2001', 'F2002',
           'F2003', 'F2004', 'F2005', 'F2006', 'F2007', 'F2008', 'F2009', 'F2010',
           'F2011', 'F2012', 'F2013', 'F2014', 'F2015', 'F2016', 'F2017', 'F2018',
           'F2019', 'F2020', 'F2021', 'F2022']

flag = 1961
for i in temp:
    far[f"In_far_{flag}"] = df[i].apply(helper.to_far)
    flag = flag+1

country_names = helper.country_names(df)

st.sidebar.title("Analysis Options")

country_wise = st.sidebar.radio("Choose an Country",["DataFrame","Country_wise_Analysis"])
if country_wise == "Country_wise_Analysis":
    line_plot_temp = st.sidebar.selectbox(label = "Choose an option",options=country_names)
    Unit = st.sidebar.radio("Choose Temperture",["Celcius","Faranheit"])
    if Unit == "Celcius":    

        plots = st.sidebar.selectbox(label = "Choose an plot",options=["Descriptive Statistics","line Plot","Histogram","Box Plot","All Plots at same",'Moving Average of Temperature Over Years',"Seasonal Decomposition"])
        st.header("{} for {}".format(plots,line_plot_temp))
        if plots == "line Plot":
            helper.cel_line_plot(line_plot_temp,df)
        elif plots =="Seasonal Decomposition":
            helper.seasonal_decomposition_cel(line_plot_temp,df)    
        elif plots == 'Moving Average of Temperature Over Years':
            helper.moving_average_cel(line_plot_temp,df)    
        elif plots == "Histogram":
            helper.temperature_histogram_cel(line_plot_temp,df)
        elif plots == "Box Plot":
            helper.temperature_box_plot_cel(line_plot_temp,df)
        elif plots == "Descriptive Statistics":
             helper.descriptive_statistics(line_plot_temp,df)
        elif plots ==  "All Plots at same":
            helper.cel_line_plot(line_plot_temp,df)
            helper.temperature_histogram_cel(line_plot_temp,df)
            helper.temperature_box_plot_cel(line_plot_temp,df)
            helper.descriptive_statistics(line_plot_temp,df)
            helper.moving_average_cel(line_plot_temp,df)
            helper.seasonal_decomposition_cel(line_plot_temp,df)
    else:
        
        plots = st.sidebar.selectbox(label = "Choose an plot",options=["Descriptive Statistics","line Plot","Histogram","Box Plot","All Plots at same",'Moving Average of Temperature Over Years',"Seasonal Decomposition"])
        st.header("{} for {}".format(plots,line_plot_temp))
        if plots == "line Plot":
            helper.far_line_plot(line_plot_temp,far)
        elif plots == 'Moving Average of Temperature Over Years':
            helper.moving_average_far(line_plot_temp,far)     
        elif plots == "Seasonal Decomposition":
             helper.seasonal_decomposition_far(line_plot_temp,far)
        elif plots == "Histogram":
            helper.temperature_histogram_far(line_plot_temp,far)
        elif plots == "Box Plot":    
            helper.temperature_box_plot_far(line_plot_temp,far)
        elif plots == "Descriptive Statistics":
             helper.descriptive_statistics(line_plot_temp,far)    
        elif plots ==  "All Plots at same":  
            helper.far_line_plot(line_plot_temp,far)
            helper.temperature_histogram_far(line_plot_temp,far)
            helper.temperature_box_plot_far(line_plot_temp,far)
            helper.descriptive_statistics(line_plot_temp,far)
            helper.moving_average_far(line_plot_temp,far)
            helper.seasonal_decomposition_far(line_plot_temp,far)
else:
    st.header("DataFrame in C Units")
    temp_df = df[["Country"]]  # Convert to DataFrame by using double brackets
    temp_df2 = df.iloc[:, 10:]
    # Concatenate along the columns (axis=1)
    data = pd.concat([temp_df, temp_df2], axis=1)
    st.dataframe(data)
    
    st.header("DataFrame in F Units")
    st.dataframe(far)        




