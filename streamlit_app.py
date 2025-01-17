

from vega_datasets import data
import matplotlib.pyplot as plt
import altair as alt
from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.transform import factor_cmap, factor_mark
import streamlit as st


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
choice = st.sidebar.radio("Choose one:", ["Matplotlib", "Altair", "Bokeh"])

if choice == 'Matplotlib':

    st.subheader("Matplotlib")

    plt.figure(figsize=(12,8))
    plt.scatter(source['Horsepower'], source['Miles_per_Gallon'])
    plt.scatter(x=source['Horsepower'], y=source['Miles_per_Gallon'])
    plt.xlabel("Horsepower")
    plt.ylabel("Miles_per_Gallon")


    st.pyplot(plt)

##ALTAIR
elif choice == 'Altair':
    st.subheader("Altair")
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


else:

    #BOKEH
    st.subheader("BOKEH")


    hover = HoverTool(
        tooltips = [('Label', '@Origin')], mode='mouse'
    )


    p = figure(title = "CARS PERFORMANCE",
               background_fill_color="#fafafa",
              tools=[hover, "pan", "crosshair","wheel_zoom", "box_zoom", "reset", "box_select"])

    p.xaxis.axis_label = 'Horsepower'
    p.yaxis.axis_label = 'Miles_per_Gallon'

    #p.circle(source['Horsepower'], source['Miles_per_Gallon'])
    p.scatter("Horsepower",
              "Miles_per_Gallon",
              source=source,
              legend_group="Origin",
              fill_alpha=0.4,
              size=12,
              #marker=factor_mark('species', MARKERS, SPECIES),
              #color=factor_cmap('species', 'Category10_3', SPECIES)
              )

    p.legend.location = "top_left"
    p.legend.title = "Origin"

    st.bokeh_chart(p)