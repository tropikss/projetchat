#from skimage.metrics import structural_similarity as ssim
import cv2

def mouvement(image1, image2, seuil_ssim=0.8):
    image1 = cv2.imread(image1)
    image2 = cv2.imread(image2)
    # Charger les images en niveaux de gris
    gris1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gris2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculer la SSIM entre les deux images
    score, _ = ssim(gris1, gris2, full=True)

    # Déterminer s'il y a un changement majeur en comparant le score à un seuil
    changement_majeur = score < seuil_ssim

    return changement_majeur

def visage(image_path):
    # Charger la cascade de Haar pour les visages
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Lire l'image depuis le chemin spécifié
    img = cv2.imread(image_path)

    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Détecter les visages dans l'image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Si un visage est détecté, renvoyer True
    return (len(faces) > 0)

# Utilisation de la fonction detect_face_in_image
image_path = 'photo/download.jpg'
if visage(image_path):
    print("Visage détecté dans l'image !")
else:
    print("Aucun visage détecté dans l'image.")

import cv2

def detect_face():
    # Charger la cascade de Haar pour les visages
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Initialiser la capture vidéo depuis la caméra (index 0 pour la caméra par défaut)
    cap = cv2.VideoCapture(0)

    while True:
        # Lire une image depuis la caméra
        ret, frame = cap.read()

        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Détecter les visages dans l'image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        # Si un visage est détecté, renvoyer True et quitter la boucle
        if len(faces) > 0:
            cap.release()
            cv2.destroyAllWindows()
            return True

        # Attendre la touche 'q' pour quitter la boucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer la capture vidéo et fermer la fenêtre
    cap.release()
    cv2.destroyAllWindows()

    # Si aucun visage n'est détecté, renvoyer False
    return False
