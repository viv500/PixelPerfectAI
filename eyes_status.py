import cv2
import dlib
from scipy.spatial import distance

# Load the pre-trained face detector and landmark predictor from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Function to compute the eye aspect ratio (EAR)
def compute_eye_aspect_ratio(eye_landmarks):
    # Compute the Euclidean distances between the vertical eye landmarks
    vertical_dist1 = distance.euclidean(eye_landmarks[1], eye_landmarks[5])
    vertical_dist2 = distance.euclidean(eye_landmarks[2], eye_landmarks[4])

    # Compute the Euclidean distance between the horizontal eye landmark
    horizontal_dist = distance.euclidean(eye_landmarks[0], eye_landmarks[3])

    # Compute the eye aspect ratio
    ear = (vertical_dist1 + vertical_dist2) / (2.0 * horizontal_dist)
    return ear

img_path = input("Enter the path to the image: ")
img = cv2.imread(img_path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray)

    for face in faces:
        # Determine the facial landmarks
        landmarks = predictor(gray, face)
        left_eye_coords = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(36, 42)]
        right_eye_coords = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(42, 48)]

        # Compute the aspect ratio for each eye
        left_eye_aspect_ratio = compute_eye_aspect_ratio(left_eye_coords)
        right_eye_aspect_ratio = compute_eye_aspect_ratio(right_eye_coords)

        # Define the threshold for closed eyes
        eye_closed_threshold = 0.173

        # Check if eyes are open or closed for each face
        if left_eye_aspect_ratio < eye_closed_threshold and right_eye_aspect_ratio < eye_closed_threshold:
            cv2.putText(img, "Eyes Closed", (face.left(), face.top() - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        else:
            cv2.putText(img, "Eyes Open", (face.left(), face.top() - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Draw rectangle around each face
        cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 2)

    cv2.imshow("Eye Status Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Invalid image path. Please try again.")
