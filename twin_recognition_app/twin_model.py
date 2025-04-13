from deepface import DeepFace
import tempfile
import os

def save_temp_image(image_pil):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        image_pil.save(tmp.name)
        return tmp.name

def compare_faces(img1_pil, img2_pil):
    path1 = save_temp_image(img1_pil)
    path2 = save_temp_image(img2_pil)

    try:
        result = DeepFace.verify(path1, path2, enforce_detection=True)
    except Exception as e:
        result = {"verified": False, "distance": None, "error": str(e)}

    os.remove(path1)
    os.remove(path2)

    return result