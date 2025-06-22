from streamlit_drawable_canvas import st_canvas
import streamlit as st

st.title("Sketchbook")
st.markdown("Draw something!")
st.sidebar.header("Configuration")

b_width = st.sidebar.slider("Brush width: ", 1, 100, 10)
b_color = st.sidebar.color_picker("Enter brush color hex: ", "#000000")
bg_color = st.sidebar.color_picker("Enter background color hex: ", "#eeeeee")
drawing_mode = "freedraw" if st.sidebar.checkbox("Drawing mode?", True) else "transform"

# Create a canvas component
canvas_result = st_canvas(
    stroke_width=b_width,
    stroke_color=b_color,
    background_color=bg_color,
    height=400,
    width=600,
    drawing_mode=drawing_mode,
    key="canvas"
)