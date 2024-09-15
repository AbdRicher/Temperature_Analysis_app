# For Country Wise

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib

data_for_col = pd.read_csv("climate_change_indicators.csv")
def column_names()->list:
    country_df = data_for_col[data_for_col["Country"] == "Algeria"]
    country_df = country_df.iloc[:, 10:]
    country_df.columns = [str(year) for year in range(1961, 2023)]
    col_names = country_df.columns
    return col_names


def helper_for_far(line_plot_temp, far):
    country_df = far[far["Country"] == line_plot_temp]
    country_df = country_df.iloc[:, 1:]
    # Ensure the columns are named correctly from 1961 to 2022
    country_df.columns = [str(year) for year in range(1961, 2023)]
    # Melt the DataFrame
    df_melted = country_df.melt(var_name='Year', value_name='Temperature')
    return df_melted

def helper_for_cel(line_plot_temp, df):
    country_df = df[df["Country"] == line_plot_temp]
    country_df = country_df.iloc[:, 10:]
    country_df.columns = [str(year) for year in range(1961, 2023)]
    # Melt the DataFrame
    df_melted = country_df.melt(var_name='Year', value_name='Temperature')
    return df_melted

def country_names(df):
    return list(df["Country"].unique())

# (°C × 9/5) + 32 = °F
def to_far(num):
    far = (num * (9/5) + 32)
    return np.round(far, decimals=2)

def far_line_plot(line_plot_temp, far):
    df_melted = helper_for_far(line_plot_temp, far)
    fig = px.line(df_melted, x='Year', y='Temperature', title='Temperature Over Years (Fahrenheit)')
    st.plotly_chart(fig)

def cel_line_plot(line_plot_temp, df):
    df_melted = helper_for_cel(line_plot_temp, df)
    fig = px.line(df_melted, x='Year', y='Temperature', title='Temperature Over Years (Celsius)')
    st.plotly_chart(fig)



def temperature_histogram_cel(line_plot_temp, df):
    df_melted = helper_for_cel(line_plot_temp, df)
    col_names = column_names()
    fig = px.histogram(df_melted, y='Temperature',x=col_names, title='Temperature Distribution Over Years')
    st.plotly_chart(fig)


def temperature_histogram_far(line_plot_temp, far):
    df_melted = helper_for_far(line_plot_temp, far)
    col_names = column_names()
    fig = px.histogram(df_melted, y='Temperature',x=col_names, title='Temperature Distribution Over Years')
    st.plotly_chart(fig)    

def temperature_box_plot_cel(line_plot_temp, df):
    df_melted = helper_for_cel(line_plot_temp, df)
    col_names = column_names()
    fig = px.box(df_melted, x='Temperature',y=col_names, title='Temperature Box Plot Over Years')
    st.plotly_chart(fig)


def temperature_box_plot_far(line_plot_temp, far):
    df_melted = helper_for_far(line_plot_temp, far)
    col_names = column_names()
    fig = px.box(df_melted, x='Temperature',y=col_names, title='Temperature Box Plot Over Years')
    st.plotly_chart(fig)

def descriptive_statistics(line_plot_temp, df):
    country_df = df[df["Country"] == line_plot_temp]
    stats = country_df.describe()
    st.write("Descriptive Statistics for {}".format(line_plot_temp))
    st.write(stats)
    
def moving_average_cel(line_plot_temp, df, window=5):
    df_melted = helper_for_cel(line_plot_temp, df)
    df_melted['Year'] = df_melted['Year'].astype(int)
    df_melted['Moving_Avg'] = df_melted['Temperature'].rolling(window=window).mean()
    fig = px.line(df_melted, x='Year', y='Moving_Avg', title='Moving Average of Temperature Over Years')
    st.plotly_chart(fig)
    
def moving_average_far(line_plot_temp, far, window=5):
    df_melted = helper_for_far(line_plot_temp, far)
    df_melted['Year'] = df_melted['Year'].astype(int)
    df_melted['Moving_Avg'] = df_melted['Temperature'].rolling(window=window).mean()
    fig = px.line(df_melted, x='Year', y='Moving_Avg', title='Moving Average of Temperature Over Years')
    st.plotly_chart(fig)




def seasonal_decomposition_cel(line_plot_temp, df):
    df_melted = helper_for_cel(line_plot_temp, df)
    df_melted['Year'] = df_melted['Year'].astype(int)
    df_melted.set_index('Year', inplace=True)
    result = seasonal_decompose(df_melted['Temperature'], model='additive', period=12)
    fig = result.plot()
    st.pyplot(fig)    

def seasonal_decomposition_far(line_plot_temp, far):
    df_melted = helper_for_far(line_plot_temp, far)
    df_melted['Year'] = df_melted['Year'].astype(int)
    df_melted.set_index('Year', inplace=True)
    result = seasonal_decompose(df_melted['Temperature'], model='additive', period=12)
    fig = result.plot()
    st.pyplot(fig)    


#     🚀 Exploring Temperature Data Analysis with Streamlit! 🌍📊

# I’m excited to share a new project where I built a data analysis app using Streamlit. This app provides interactive visualizations including line plots, histograms, boxplots, and seasonal decomposition for temperature data in Celsius and Fahrenheit across various countries.

# 🔍 Key Features:

# Interactive Line Plots: Visualize temperature trends over time.
# Detailed Histograms: Analyze the distribution of temperature data.
# Comprehensive Boxplots: Compare temperature variations across different countries.
# Seasonal Decomposition: Understand seasonal patterns in temperature data.
# Descriptive Analysis: Gain insights into temperature data with various statistical measures.
# 🎥 Watch the Video: [Link to your video]

# 📢 Thoughts and Feedback:

# What did you find most interesting about the visualizations?
# Are there additional features or improvements you would suggest?
# How do you think this app could be applied in real-world scenarios?
# I’m looking forward to your insights and feedback! Let’s discuss how we can leverage data visualization to uncover meaningful patterns and trends.

# #DataScience #Streamlit #DataAnalysis #Visualization #MachineLearning

