from skimage.metrics import structural_similarity as ssim
import cv2

def mouvement(image1, image2, seuil_ssim=0.8):
    # Charger les images en niveaux de gris
    gris1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gris2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculer la SSIM entre les deux images
    score, _ = ssim(gris1, gris2, full=True)

    # Déterminer s'il y a un changement majeur en comparant le score à un seuil
    changement_majeur = score < seuil_ssim

    return changement_majeur
