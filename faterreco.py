import face_recognition
import cv2

#We integrated it on Rasberry Pie

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
Rajat_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Rajat.jpeg")
Rajat_face_encoding = face_recognition.face_encodings(Rajat_image)[0]

# Load a second sample picture and learn how to recognize it.
Aditya_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Aditya.jpeg")
Aditya_face_encoding = face_recognition.face_encodings(Aditya_image)[0]

# Load a second sample picture and learn how to recognize it.
Manas_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Manas.jpeg")
Manas_face_encoding = face_recognition.face_encodings(Manas_image)[0]

# Load a second sample picture and learn how to recognize it.
Manas1_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Manas1.jpeg")
Manas1_face_encoding = face_recognition.face_encodings(Manas1_image)[0]

# Load a second sample picture and learn how to recognize it.
Manas2_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Manas2.jpeg")
Manas2_face_encoding = face_recognition.face_encodings(Manas2_image)[0]

# Load a second sample picture and learn how to recognize it.
Manas3_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Manas3.jpeg")
Manas3_face_encoding = face_recognition.face_encodings(Manas3_image)[0]

# Load a second sample picture and learn how to recognize it.
Rajat1_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Rajat1.jpeg")
Rajat1_face_encoding = face_recognition.face_encodings(Rajat1_image)[0]

# Load a second sample picture and learn how to recognize it.
Rajat2_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Rajat2.jpeg")
Rajat2_face_encoding = face_recognition.face_encodings(Rajat2_image)[0]

# Load a second sample picture and learn how to recognize it.
Rajat3_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Rajat3.jpeg")
Rajat3_face_encoding = face_recognition.face_encodings(Rajat3_image)[0]

# Load a second sample picture and learn how to recognize it.
Aditya1_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Aditya1.jpeg")
Aditya1_face_encoding = face_recognition.face_encodings(Aditya1_image)[0]

# Load a second sample picture and learn how to recognize it.
Aditya2_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/Aditya2.jpeg")
Aditya2_face_encoding = face_recognition.face_encodings(Aditya2_image)[0]

# Load a second sample picture and learn how to recognize it.
z_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/z.jpeg")
z_face_encoding = face_recognition.face_encodings(z_image)[0]

# Load a second sample picture and learn how to recognize it.
z1_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/z1.jpeg")
z1_face_encoding = face_recognition.face_encodings(z1_image)[0]

# Load a second sample picture and learn how to recognize it.
z2_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/z2.jpeg")
z2_face_encoding = face_recognition.face_encodings(z2_image)[0]

# Load a second sample picture and learn how to recognize it.
z3_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/z3.jpeg")
z3_face_encoding = face_recognition.face_encodings(z3_image)[0]

# Load a second sample picture and learn how to recognize it.
zz_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/zz.jpeg")
zz_face_encoding = face_recognition.face_encodings(zz_image)[0]

# Load a second sample picture and learn how to recognize it.
zz1_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/zz1.jpeg")
zz1_face_encoding = face_recognition.face_encodings(zz1_image)[0]

# Load a second sample picture and learn how to recognize it.
zz2_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/zz2.jpeg")
zz2_face_encoding = face_recognition.face_encodings(zz2_image)[0]

# Load a second sample picture and learn how to recognize it.
zzz_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/zzz.jpeg")
zzz_face_encoding = face_recognition.face_encodings(zzz_image)[0]

# Load a second sample picture and learn how to recognize it.
zzz1_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/zzz1.jpeg")
zzz1_face_encoding = face_recognition.face_encodings(zzz1_image)[0]

# Load a second sample picture and learn how to recognize it.
zzzz_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/zzzz.jpeg")
zzzz_face_encoding = face_recognition.face_encodings(zzzz_image)[0]

# Load a second sample picture and learn how to recognize it.
zzzz1_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/zzzz1.jpeg")
zzzz1_face_encoding = face_recognition.face_encodings(zzzz1_image)[0]

# Load a second sample picture and learn how to recognize it.
zzzz2_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/zzzz2.jpeg")
zzzz2_face_encoding = face_recognition.face_encodings(zzzz2_image)[0]

# Load a second sample picture and learn how to recognize it.
zzzz3_image = face_recognition.load_image_file("/home/rajat/Desktop/Trainimages/zzzz3.jpeg")
zzzz3_face_encoding = face_recognition.face_encodings(zzzz3_image)[0]






# Create arrays of known face encodings and their names
known_face_encodings = [
    Rajat_face_encoding,
    Aditya_face_encoding,
    Manas_face_encoding,
    Manas1_face_encoding,
    Manas2_face_encoding,
    Manas3_face_encoding,
    Rajat1_face_encoding,
    Rajat2_face_encoding,
    Rajat3_face_encoding,
    Aditya1_face_encoding,
    Aditya2_face_encoding,
    z_face_encoding,
    z1_face_encoding,
    z2_face_encoding,
    z3_face_encoding,
    zz_face_encoding,
    zz1_face_encoding,
    zz2_face_encoding,
    zzz_face_encoding,
    zzz1_face_encoding,
    zzzz_face_encoding,
    zzzz1_face_encoding,
    zzzz2_face_encoding,
    zzzz3_face_encoding

]
known_face_names = [
    "Rajat Khanna",
    "Aditya Naresh",
    "Manas Ghai",
    "Manas Ghai",
    "Manas Ghai",
    "Manas Ghai",
    "Rajat Khanna",
    "Rajat Khanna",
    "Rajat Khanna",
    "Aditya Naresh",
    "Aditya Naresh",
    "Raghunandan",
    "Raghunandan",
    "Raghunandan",
    "Raghunandan",
    "Kabir Juneja",
    "Kabir Juneja",
    "Kabir Juneja",
    "Jatin Nandal",
    "Jatin Nandal",
    "Udaram Prajapat",
    "Udaram Prajapat",
    "Udaram Prajapat",
    "Udaram Prajapat"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.42)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
