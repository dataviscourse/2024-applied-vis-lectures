import streamlit as st

# import altair as alt
# import pandas as pd
# from vega_datasets import data

# iris_df = data.iris()
# cars_df = data.cars()

st.write("Hello, World!")

# df = data.cars()

# brush_selection = alt.selection_interval()

# base_plot = alt.Chart(df)

# scatterplot = base_plot.mark_point().encode(
#     x="Miles_per_Gallon:Q",
#     y="Weight_in_lbs:Q",
#     color=alt.condition(brush_selection, "Origin:N", alt.value("gray")),
#     opacity=alt.condition(brush_selection, alt.value(0.7), alt.value(0.3))
# ).add_params(
#     brush_selection
# )

# histogram = base_plot.mark_bar().encode(
#     y="Origin:N",
#     color="Origin:N",
#     x="count():Q",
# ).transform_filter(
#     brush_selection
# )

# st.write(scatterplot & histogram)