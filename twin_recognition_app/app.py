import streamlit as st
from PIL import Image
from twin_model import compare_faces

st.title("👯 Twin Recognition App (DeepFace)")

st.write("Upload two face images to check if they look like twins.")

img1 = st.file_uploader("Upload first image", type=["jpg", "jpeg", "png"])
img2 = st.file_uploader("Upload second image", type=["jpg", "jpeg", "png"])

if img1 and img2:
    image1 = Image.open(img1).convert("RGB")
    image2 = Image.open(img2).convert("RGB")

    st.image([image1, image2], caption=["Image 1", "Image 2"], width=300)

    with st.spinner("Analyzing faces..."):
        result = compare_faces(image1, image2)

    if "error" in result:
        st.error(f"Error: {result['error']}")
    elif result["verified"]:
        st.success(f"✅ They look like twins! (distance: {result['distance']:.2f})")
    else:
        st.warning(f"❌ They don't look alike. (distance: {result['distance']:.2f})")