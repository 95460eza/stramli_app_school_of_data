
import streamlit as st
import altair as alt
from vega_datasets import data
import matplotlib.pyplot as plt
from bokeh.plotting import figure


source = data.cars()



st.title("Data Visualization web application")
st.header("Part 1: Data Exploration")
st.write("In this section, we will explore the Altair cars dataset.")
st.markdown("*Further resources [here](https://altair-viz.github.io/gallery/selection_histogram.html)*")

slider = st.slider("Slider title", 0, 100, 50)
if slider > 50:
    st.write("GREAT")
check = st.checkbox("Checkbox title", ["Add a constant", "Add beta 1", "Add beta 2"])
radio = st.radio("Radio title", ["Yes", "No"])
txt = st.text_input("Type here")
if txt == 'coucou':
    st.write(f"You wrote {txt}")
txt_area = st.text_area("Type here")
button = st.button("Button name")


if st.button("Click to launch"):
    st.execute_code




st.header("Visualization")

st.subheader("Matplotlib")

plt.figure(figsize=(12,8))
plt.scatter(source['Horsepower'], source['Miles_per_Gallon'])
st.pyplot(plt)


brush = alt.selection(type='interval')

points = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
).add_selection(
    brush
)

bars = alt.Chart(source).mark_bar().encode(
    y='Origin:N',
    color='Origin:N',
    x='count(Origin):Q'
).transform_filter(
    brush
)

st.altair_chart(points & bars)




p = figure()
p.circle(source['Horsepower'], source['Miles_per_Gallon'])
st.bokeh_chart(p)