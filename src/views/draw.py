import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Sketchbook")
st.markdown("Draw something!")
st.sidebar.header("Configuration")

b_width = st.sidebar.slider("Brush width: ", 1, 100, 10)
b_color = st.sidebar.beta_color_picker("Enter brush color hex: ")
bg_color = st.sidebar.beta_color_picker("Enter background color hex: ", "#eee")
drawing_mode = st.sidebar.checkbox("Drawing mode ?", True)

# Create a canvas component
image_data = st_canvas(
    b_width, b_color, bg_color, height=150, drawing_mode=drawing_mode, key="canvas"
)

# Do something interesting with the image data
if image_data is not None:
    st.image(image_data)