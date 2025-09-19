from vertexai import init
from vertexai.generative_models import GenerativeModel, Part

# Initialize with your GCP project + region
init(project="data-doodlers-5866", location="us-central1")
model = GenerativeModel("gemini-1.5-flash")  # Or gemini-1.5-pro
# Load image file

image = Part.from_data(
    mime_type="image/jpeg", 
    data=open("20250721_140630.jpeg", "rb").read()
)
# image = Part.from_image(open("20250721_140630.jpeg", "rb"))

# Define prompt
prompt = """
You are a health assistant. From this image:
1. Extract calories burned if present.
2. If it’s a food image, say if it is healthy/unhealthy.
3. If it’s an activity (e.g., painting, crocheting), detect and classify if it is mentally healthy.
Return the result in plain text.
"""
response = model.generate_content([prompt, image])

print(response.text)
