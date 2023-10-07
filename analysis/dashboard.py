import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Smokers Dashboard")
st.markdown("The dashboard will help a researchers to get to know more about the given dataset and it's output")

st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

# Reading the dataset
data = pd.read_csv(r"C:\Users\LENOVO\Documents\Aug_PYDS_9.30\analysis\demo_data_set.csv")

chart_visual = st.sidebar.selectbox("Select the Charts/Plots", ('Line Chart', 'Bar Chart', 'Bubble Chart'))

st.sidebar.checkbox("Show Analysis by Smoking Status", True, key=1)
selected_status = st.sidebar.selectbox("Select Smoking Status", options=['formerly_smoked','Smokes','Never_Smoked','Unknown'])

fig = go.Figure()

if chart_visual == 'Line Chart':
    if selected_status == 'formerly_smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.formerly_smoked, mode="lines",name="formerly_smoked"))
    
    if selected_status == 'Smokes':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Smokes, mode="lines",name="Smokes"))

    if selected_status == 'Never_Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Never_Smoked, mode="lines",name="Never_Smoked"))


    if selected_status == 'Unknown':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Unknown, mode="lines",name="Unknown"))

elif chart_visual == 'Bar_Chart':
    if selected_status == 'formerly_smoked':
        fig.add_trace(go.Bar(x=data.Country, y=data.formerly_smoked, name="formerly_smoked"))

    if selected_status == 'Smokes':
        fig.add_trace(go.Bar(x=data.Country, y=data.Smokes, name="Smokes"))

    if selected_status == 'Never_Smoked':
        fig.add_trace(go.Bar(x=data.Country, y=data.Never_Smoked, name="Never_Smoked"))

    if selected_status == 'Unknown':
        fig.add_trace(go.Bar(x=data.Country, y=data.Unknown, name="Unknown"))

elif chart_visual == 'Bubble Chart':
    if selected_status == 'formerly_smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.formerly_smoked, mode="markers",name="formerly_smoked"))

    if selected_status == 'Smokes':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Smokes, mode="markers",name="Smokes"))

    if selected_status == 'Never_Smoked':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Never_Smoked, mode="markers",name="Never_Smoked"))

    if selected_status == 'Unknown':
        fig.add_trace(go.Scatter(x=data.Country, y=data.Unknown, mode="markers",name="Unknown"))

st.plotly_chart(fig, use_container_width=True)



