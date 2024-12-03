import streamlit as st
from PIL import Image
import rembg as bg
from io import BytesIO

# Set up Streamlit app
st.set_page_config(page_title="Background Remover")
st.title("Let's Remove Backgrounds")

# Upload the image
img = st.file_uploader("Upload your image file here", type=["png", "jpg", "jpeg"])

if img:
    # Save the uploaded image locally
    with open(img.name, "wb") as f:
        f.write(img.getbuffer())

    # Display the uploaded image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Open and process the image
    img_input = Image.open(img.name)
    extracted_img = bg.remove(img_input)

    # Display the processed image
    st.image(extracted_img, caption="Background Removed", use_column_width=True)

    # Prepare the image for download
    img_buffer = BytesIO()
    extracted_img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    # Download button for the processed image
    st.download_button(
        label="Download Image with Background Removed",
        data=img_buffer,
        file_name="background_removed.png",
        mime="image/png",
    )
