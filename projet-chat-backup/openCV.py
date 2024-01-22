#from skimage.metrics import structural_similarity as ssim
import cv2
import os

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
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

    # Lire l'image depuis le chemin spécifié
    img = cv2.imread(image_path)

    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Détecter les visages dans l'image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3, minSize=(30, 30))

    # Si un visage est détecté, renvoyer True
    return (len(faces) > 0)

def test(repertoire):
    # Vérifier si le chemin fourni est un répertoire
    if not os.path.isdir(repertoire):
        print(f"{repertoire} n'est pas un répertoire valide.")
        return

    # Liste tous les fichiers du répertoire
    fichiers = [f for f in os.listdir(repertoire) if os.path.isfile(os.path.join(repertoire, f))]

    # Exécuter la fonction visage() pour chaque fichier
    for fichier in fichiers:
        chemin_fichier = os.path.join(repertoire, fichier)
        print(str(fichier)+" : "+str(visage(chemin_fichier)))

# Utilisation de la fonction detect_face_in_image
test("phototest")