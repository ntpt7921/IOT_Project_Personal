import tomli
from content import *

with open("../config.toml", "rb") as config_file:
    config = tomli.load(config_file)

# Load the model
# This file is expect to be run seperately, so use relative path to model
# and label file
MODEL_FILE = config["TeachableMachine"]["model_file"]
LABEL_FILE =  config["TeachableMachine"]["label_file"]
model, class_names = load_model_and_label(MODEL_FILE, LABEL_FILE)

camera_capture = start_webcam_capture()

try: 
    while True:
        frame = read_frame_from_webcam(camera_capture)
        class_name, confidence_score = run_inference_on_frame(frame, model, class_names)

        # Print prediction and confidence score
        print("Class:", class_name, str(np.round(confidence_score * 100)), "%")
finally:
    clean_up(camera_capture)
