import os
from django.conf import settings
import face_recognition

def identify(unknown_img):
    for root, dirs, files in os.walk(settings.MEDIA_ROOT):
        for file in files:
            user = file.split('.')[0]
            img_path = os.path.join(root, file)
            if compare(img_path, unknown_img):
                return user
    return "UnKnown"


def compare(known_img, unknown_img) -> bool:
    # known_image = face_recognition.load_image_file('/home/lc/workbench/Python/Face/DjangoAPI/media/my-image.png')
    # unknown_image = face_recognition.load_image_file('/home/lc/workbench/Python/Face/DjangoAPI/unknown/unknown.png')

    known_image = face_recognition.load_image_file(known_img)
    unknown_image = face_recognition.load_image_file(unknown_img)

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    if True in results:
        return True
    return False