import streamlit as st
import pandas as pd
import plotly.express as px

st.title('CHONJO TECHNOLOGIES LTD.')
st.write('we offer quality data analysis dashboard you can rely on.')
def load_data():
    df = pd.read_csv("vgsales.csv")
    return df

data = load_data()

# Title and introduction
st.subheader("Video Game Sales Dashboard")
st.write("Explore video game sales, ratings, and platforms using this interactive dashboard.")

# Display raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(data)

# Filter data by platform
platforms = data['Platform'].unique()
platform_filter = st.multiselect("Select platforms:", platforms, default=platforms)
filtered_data = data[data['Platform'].isin(platform_filter)]

# Bar chart for the top N games by global sales
st.subheader("Top N Games by Global Sales")
top_n = st.number_input("Select the top N games:", min_value=5, max_value=100, value=10, step=1)
top_games = filtered_data.nlargest(top_n, "Global_Sales")
fig = px.bar(top_games, x="Name", y="Global_Sales", color="Platform", hover_name="Name", text="Global_Sales")
st.plotly_chart(fig)

# Pie chart for platform market share
st.subheader("Platform Market Share")
platform_share = filtered_data.groupby("Platform")["Global_Sales"].sum().reset_index()
fig2 = px.pie(platform_share, names="Platform", values="Global_Sales", title="Platform Market Share")
st.plotly_chart(fig2)

# Scatter plot for Year vs. Global Sales
st.subheader("Year vs. Global Sales")
fig3 = px.scatter(filtered_data, x="Year", y="Global_Sales", color="Platform", hover_name="Name", opacity=0.6)
st.plotly_chart(fig3)


st.sidebar.title('PROFILE')
st.sidebar.subheader('CHONJO TECHONOLOGIES LTD.')
st.sidebar.text_input('OUR EMAIL ADDRESS:')
st.sidebar.text_input('OUR PHONE NUMBER:')
st.sidebar.write('THANK YOU FOR CHOOSING US.')

st.title('EXAMPLE TWO')

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt




########## upload the dataset using uploader ###############
# uploaded_file = st.file_uploader("Upload your dataset (CSV file):")

# if uploaded_file:
#     column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
#     data = pd.read_csv(uploaded_file, header=None, names=column_names)
#     st.write("### Raw Data")
#     st.dataframe(data)



def load_iris_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    data = pd.read_csv(url, header=None, names=column_names)
    return data

data = load_iris_data()

st.title("Iris Dataset Explorer")
st.write("Explore the Iris dataset by answering the following questions:")

# Display the raw data
if st.checkbox("DISPLAY RAW DATA"):
    st.subheader("Raw Data Displayed")
    st.dataframe(data)

# Question 1: Show the average sepal length for each species
if st.checkbox("Show the average sepal length for each species"):
    st.subheader("Average Sepal Length per Species")
    avg_sepal_length = data.groupby("species")["sepal_length"].mean()
    st.write(avg_sepal_length)

# Question 2: Display a scatter plot comparing two features
st.subheader("Compare two features using a scatter plot")
feature_1 = st.selectbox("Select the first feature:", data.columns[:-1])
feature_2 = st.selectbox("Select the second feature:", data.columns[:-1])

scatter_plot = px.scatter(data, x=feature_1, y=feature_2, color="species", hover_name="species")
st.plotly_chart(scatter_plot)

# Question 3: Filter data based on species
st.subheader("Filter data based on species")
selected_species = st.multiselect("Select species to display:", data["species"].unique())

if selected_species:
    filtered_data = data[data["species"].isin(selected_species)]
    st.dataframe(filtered_data)
else:
    st.write("No species selected.")

# Question 4: Display a pairplot for the selected species
if st.checkbox("Show pairplot for the selected species"):
    st.subheader("Pairplot for the Selected Species")

    if selected_species:
        sns.pairplot(filtered_data, hue="species")
    else:
        sns.pairplot(data, hue="species")
        
    st.pyplot()

# Question 5: Show the distribution of a selected feature
st.subheader("Distribution of a Selected Feature")
selected_feature = st.selectbox("Select a feature to display its distribution:", data.columns[:-1])

hist_plot = px.histogram(data, x=selected_feature, color="species", nbins=30, marginal="box", hover_data=data.columns)
st.plotly_chart(hist_plot)