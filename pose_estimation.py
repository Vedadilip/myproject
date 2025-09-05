import math

def calculate_angle(a, b, c):
    """Calculate angle at point b given points a, b, c with (x,y) coordinates."""
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    return np.degrees(angle)

# Inside your main loop, after obtaining 'keypoints':

# Map MoveNet keypoints indices for left shoulder, left elbow, left wrist
LEFT_SHOULDER = 5
LEFT_ELBOW = 7
LEFT_WRIST = 9

# Extract relevant points (x,y scaled to image size)
h, w, _ = frame.shape
left_shoulder = (keypoints[0,0,LEFT_SHOULDER,1]*w, keypoints[0,0,LEFT_SHOULDER,0]*h)
left_elbow = (keypoints[0,0,LEFT_ELBOW,1]*w, keypoints[0,0,LEFT_ELBOW,0]*h)
left_wrist = (keypoints[0,0,LEFT_WRIST,1]*w, keypoints[0,0,LEFT_WRIST,0]*h)

# Calculate elbow angle
elbow_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)

# Feedback message example
feedback = ""
if predicted_pose == "Warrior":
    if elbow_angle < 160:
        feedback = "Straighten your left arm"
    else:
        feedback = "Good pose!"

# Display feedback on frame
cv2.putText(frame, feedback, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
