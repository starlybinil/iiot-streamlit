import streamlit as st
import pandas as pd
import numpy as np
from data import retrieve
import plotly.express as px
import streamviz
import time

st.set_page_config(page_title="IIoT Dash Query", page_icon="📊", layout="wide")

st.markdown("# IIoT Dash Demo")
st.sidebar.header("IIoT Dash Query")

df = retrieve.getData()
print("asfsdfsdfsdfsfd", df.shape[0])
machines = st.multiselect(
    "Choose Machine", list(df.loc[:,'id'].unique()), ["100"]
)

st.divider()

# creating a single-element container
placeholder = st.empty()
tempList = df['Temperature'].tolist()
pressList= df['Pressure'].tolist()
humidList= df['Humidity'].tolist()

for idx in range (200):
    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # creating KPIs
        atemp = np.mean(df["Temperature"])
        apressure = np.mean(df["Temperature"])
        ahumidity = np.mean(df["Humidity"])

        temp=tempList[idx]
        pressure=pressList[idx]
        humidity=humidList[idx]

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="Temp ⏳",
            value=int(temp),
            delta=round(temp) - 10,
        )

        kpi2.metric(
            label="Pressure 💍",
            value=int(pressure),
            delta=-1 + pressure,
        )

        kpi3.metric(
            label="Humidity %",
            value=int(humidity),
        )

        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = st.line_chart(
                data=df, x="Timestamp", y="Temperature"
            )
            #st.write(fig)
            
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = st.line_chart(
                data=df, x="Timestamp", y="Pressure"
            )
            #st.write(fig2)

        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
