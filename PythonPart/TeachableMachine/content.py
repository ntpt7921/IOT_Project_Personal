from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

def load_model_and_label(model_file_path, label_file_path):
    model = load_model(model_file_path, compile=False)
    label = [line.replace('\n', '').split(sep=' ', maxsplit=1)[1] 
             for line in open(label_file_path).readlines()]
    return (model, label)

def start_webcam_capture(webcam_id = 0):
    # Capture the camera stream
    # CAMERA can be 0 or 1 based on default camera of your computer
    webcam_capture = cv2.VideoCapture(webcam_id)
    if not webcam_capture.isOpened():
        raise RuntimeError("Can not open webcam")
    return webcam_capture

def read_frame_from_webcam(webcam_capture):
    if not isinstance(webcam_capture, cv2.VideoCapture):
        raise RuntimeError("Invalid value passed to function, "
                           "expected object instance of type cv2.VideoCapture")
    # Read frame, ret is True if success
    ret, frame = webcam_capture.read()
    if not ret:
        raise RuntimeError("Failure reading frame from webcam")
    return frame

def show_frame(frame):
    # Show the image in a window
    cv2.imshow("Webcam Image", frame)

def clean_up(webcam_capture):
    cv2.destroyAllWindows()
    if not isinstance(webcam_capture, cv2.VideoCapture):
        raise RuntimeError("Invalid value passed to function, "
                           "expected object instance of type cv2.VideoCapture")
    webcam_capture.release()


def run_inference_on_frame(frame, model, label):
    # Resize the raw image into (224-height,224-width) pixels
    frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the models input shape.
    frame = np.asarray(frame, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    frame = (frame / 127.5) - 1

    # Predicts the model
    prediction = model.predict(frame)
    max_prob_index = np.argmax(prediction)
    class_name = label[max_prob_index]
    confidence_score = prediction[0][max_prob_index]

    return (class_name, confidence_score)

