import gradio as gr
import cv2
import torch
import numpy as np
from PIL import Image
from collections import Counter

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Function to run inference on an image
def run_inference(image):
    # Convert the image from PIL format to a format compatible with OpenCV
    image = np.array(image)

    # Run YOLOv5 inference
    results = model(image)

    # Convert the annotated image from BGR to RGB for display
    annotated_image = results.render()[0]
    annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

    return Image.fromarray(annotated_image)

# Function to generate a summary for the detected objects with counts
def generate_summary_with_counts(image):
    results = model(image)
    detected_objects = results.pandas().xyxy[0]

    # Count detected objects
    object_names = detected_objects['name'].tolist()
    object_counts = Counter(object_names)

    # Create a summary
    summary = "Detected objects:\n\n"
    for obj, count in object_counts.items():
        summary += f"- {obj}: {count}\n"

    return summary, object_counts

# Function to generate a scene description based on the detected objects
def generate_scene_description(object_counts):
    """
    Generate a possible scene description based on detected objects and their counts.
    """
    if "person" in object_counts and "dog" in object_counts:
        return "This scene seems to capture people spending time outdoors with pets, possibly in a park or recreational area."
    elif "person" in object_counts and "laptop" in object_counts:
        return "This might be a workplace or a study environment, featuring individuals using laptops for work or study."
    elif "car" in object_counts or "truck" in object_counts:
        return "This appears to be a street or traffic scene with vehicles in motion or parked."
    elif "cat" in object_counts and "sofa" in object_counts:
        return "This scene seems to capture a cozy indoor environment, likely a home with pets relaxing."
    elif "bicycle" in object_counts and "person" in object_counts:
        return "This could depict an outdoor activity, such as cycling or commuting by bike."
    elif "boat" in object_counts or "ship" in object_counts:
        return "This seems to be a water-based setting, possibly near a harbor, river, or open sea."
    elif "bird" in object_counts and "tree" in object_counts:
        return "This scene depicts a natural setting, possibly a park or forest, with birds and trees."
    elif "person" in object_counts and "microwave" in object_counts:
        return "This is likely an indoor setting, such as a kitchen, where cooking or meal preparation is taking place."
    elif "cow" in object_counts or "sheep" in object_counts:
        return "This scene appears to capture a rural or farming environment, featuring livestock in open fields or farms."
    elif "horse" in object_counts and "person" in object_counts:
        return "This might depict an equestrian scene, possibly involving horseback riding or ranch activities."
    elif "dog" in object_counts and "ball" in object_counts:
        return "This scene seems to show playful activities, possibly a game of fetch with a dog."
    elif "umbrella" in object_counts and "person" in object_counts:
        return "This might capture a rainy day or a sunny outdoor activity where umbrellas are being used."
    elif "train" in object_counts or "railway" in object_counts:
        return "This scene could involve a railway station or a train passing through a scenic route."
    elif "surfboard" in object_counts or "person" in object_counts:
        return "This is likely a beach or coastal scene featuring activities like surfing or water sports."
    elif "dining table" in object_counts and "person" in object_counts:
        return "This is likely a scene of a Person eating in a Resaturant or Food Court."
    elif "book" in object_counts and "person" in object_counts:
        return "This scene could depict a quiet reading environment, such as a library or a study room."
    elif "traffic light" in object_counts and "car" in object_counts:
        return "This seems to capture an urban street scene with traffic and signals controlling the flow."
    elif "chair" in object_counts and "dining table" in object_counts:
        return "This is likely an indoor dining area, possibly a family meal or a restaurant setting."
    elif "flower" in object_counts and "person" in object_counts:
        return "This scene could depict a garden or a floral setting, possibly involving gardening or photography."
    elif "airplane" in object_counts:
        return "This appears to capture an airport or an aerial view, featuring an airplane in flight or on the ground."
    elif "person" in object_counts and "whiteboard" in object_counts:
        return "This could be a classroom or seminar setting, with individuals engaged in a lecture or discussion."
    elif "person" in object_counts and "book" in object_counts:
        return "This scene might depict a library or a study area, where individuals are reading or preparing for exams."
    elif "person" in object_counts and "bicycle" in object_counts:
        return "This is likely a college or urban area, with students or commuters cycling to their destinations."
    elif "person" in object_counts and "water bottle" in object_counts:
        return "This could be a casual setting, such as a study group or a break during classes, with hydration in focus."
    elif "person" in object_counts and "notebook" in object_counts:
        return "This scene might depict students taking notes during a lecture or brainstorming in a group study."
    elif "person" in object_counts and "coffee cup" in object_counts:
        return "This scene could represent a casual hangout in a café, study break, or an informal meeting."
    elif "person" in object_counts and "calculator" in object_counts:
        return "This is likely an exam hall or a math-focused study session, where calculations are being performed."
    elif "laptop" in object_counts and "coffee cup" in object_counts:
        return "This might depict a college café or a workspace where students are multitasking with work and refreshments."
    elif "pen" in object_counts and "notebook" in object_counts:
        return "This scene seems to involve note-taking or journaling, possibly in a classroom or a quiet study area."
    elif "headphones" in object_counts and "person" in object_counts:
        return "This is likely a casual setting where someone is listening to music, attending an online class, or watching videos."
    
    # Other common and general scenarios
    elif "person" in object_counts and "dog" in object_counts:
        return "This scene seems to capture people spending time outdoors with pets, possibly in a park or recreational area."
    elif "person" in object_counts and "laptop" in object_counts:
        return "This might be a workplace or a study environment, featuring individuals using laptops for work or study."
    elif "car" in object_counts or "truck" in object_counts:
        return "This appears to be a street or traffic scene with vehicles in motion or parked."
    elif "cat" in object_counts and "sofa" in object_counts:
        return "This scene seems to capture a cozy indoor environment, likely a home with pets relaxing."
    elif "bicycle" in object_counts and "person" in object_counts:
        return "This could depict an outdoor activity, such as cycling or commuting by bike."
    elif "boat" in object_counts or "ship" in object_counts:
        return "This seems to be a water-based setting, possibly near a harbor, river, or open sea."
    elif "bird" in object_counts and "tree" in object_counts:
        return "This scene depicts a natural setting, possibly a park or forest, with birds and trees."
    elif "person" in object_counts and "microwave" in object_counts:
        return "This is likely an indoor setting, such as a kitchen, where cooking or meal preparation is taking place."
    elif "cow" in object_counts or "sheep" in object_counts:
        return "This scene appears to capture a rural or farming environment, featuring livestock in open fields or farms."
    elif "horse" in object_counts and "person" in object_counts:
        return "This might depict an equestrian scene, possibly involving horseback riding or ranch activities."
    elif "dog" in object_counts and "ball" in object_counts:
        return "This scene seems to show playful activities, possibly a game of fetch with a dog."
    elif "umbrella" in object_counts and "person" in object_counts:
        return "This might capture a rainy day or a sunny outdoor activity where umbrellas are being used."
    elif "train" in object_counts or "railway" in object_counts:
        return "This scene could involve a railway station or a train passing through a scenic route."
    elif "surfboard" in object_counts or "person" in object_counts:
        return "This is likely a beach or coastal scene featuring activities like surfing or water sports."
    elif "book" in object_counts and "person" in object_counts:
        return "This scene could depict a quiet reading environment, such as a library or a study room."
    elif "traffic light" in object_counts and "car" in object_counts:
        return "This seems to capture an urban street scene with traffic and signals controlling the flow."
    elif "chair" in object_counts and "dining table" in object_counts:
        return "This is likely an indoor dining area, possibly a family meal or a restaurant setting."
    elif "flower" in object_counts and "person" in object_counts:
        return "This scene could depict a garden or a floral setting, possibly involving gardening or photography."
    elif "airplane" in object_counts:
        return "This appears to capture an airport or an aerial view, featuring an airplane in flight or on the ground."
    else:
        return "This scene involves various objects, indicating a dynamic or diverse setting."
# Create the Gradio interface with enhanced UI
with gr.Blocks(css="""
    body {
        font-family: 'Poppins', sans-serif;
        margin: 0;
        background: linear-gradient(135deg, #3D52A0, #7091E6, #8697C4, #ADBBDA, #EDE8F5);
        background-size: 400% 400%;
        animation: gradient-animation 15s ease infinite;
        color: #FFFFFF;
    }
    @keyframes gradient-animation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    h1 {
        text-align: center;
        color: #FFFFFF;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 0.5em;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    }
    footer {
        text-align: center;
        margin-top: 20px;
        padding: 10px;
        font-size: 1em;
        color: #FFFFFF;
        background: rgba(61, 82, 160, 0.8);
        border-radius: 8px;
    }
    .gr-button {
        font-size: 1em;
        padding: 12px 24px;
        background: linear-gradient(90deg, #7091E6, #8697C4);
        color: #FFFFFF;
        border: none;
        border-radius: 5px;
        transition: all 0.3s ease-in-out;
    }
    .gr-button:hover {
        background: linear-gradient(90deg, #8697C4, #7091E6);
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    .gr-box {
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        color: #FFFFFF;
    }
""") as demo:
    with gr.Row():
        gr.Markdown("<h1>✨ InsightVision: Detect, Analyze, Summarize ✨</h1>")

    with gr.Row():
        with gr.Column(scale=2):
            image_input = gr.Image(label="Upload Image", type="pil", elem_classes="gr-box")
            detect_button = gr.Button("Run Detection", elem_classes="gr-button")
        with gr.Column(scale=3):
            annotated_image_output = gr.Image(label="Detected Image", type="pil", elem_classes="gr-box")
            summary_output = gr.Textbox(label="Detection Summary with Object Counts", lines=10, interactive=False, elem_classes="gr-box")
            scene_description_output = gr.Textbox(label="Scene Description", lines=5, interactive=False, elem_classes="gr-box")
    
    # Actions for buttons
    def detect_and_process(image):
        annotated_image = run_inference(image)
        summary, object_counts = generate_summary_with_counts(np.array(image))
        scene_description = generate_scene_description(object_counts)
        return annotated_image, summary, scene_description
    
    detect_button.click(
        fn=detect_and_process,
        inputs=[image_input],
        outputs=[annotated_image_output, summary_output, scene_description_output]
    )

    gr.Markdown("<footer>Made with ❤️ using Gradio and YOLOv5 | © 2024 InsightVision</footer>")

# Launch the interface
demo.launch()
