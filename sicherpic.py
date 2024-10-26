import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import webbrowser
import requests

# Fonction pour uploader l'image
def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")]
    )
    if file_path:
        try:
            img = Image.open(file_path)
            img.thumbnail((200, 200))
            img_display = ImageTk.PhotoImage(img)
            img_label.config(image=img_display)
            img_label.image = img_display
            global uploaded_image_path
            uploaded_image_path = file_path
            search_button.config(state="normal")
        except Exception as e:
            messagebox.showerror("Erreur", "Impossible de charger l'image.")

# Fonction pour lancer la recherche d'image inversée
def search_image(engine):
    if not uploaded_image_path:
        messagebox.showwarning("Attention", "Veuillez d'abord uploader une image.")
        return

    # Encode l'image dans l'URL pour la recherche
    with open(uploaded_image_path, "rb") as image_file:
        image_data = image_file.read()
    
    # Moteurs de recherche disponibles
    engines = {
        "Google": f"https://www.google.com/searchbyimage?image_url={uploaded_image_path}",
        "TinEye": f"https://tineye.com/search?url={uploaded_image_path}",
        "Yandex": f"https://yandex.com/images/search?rpt=imageview&url={uploaded_image_path}"
    }

    try:
        url = engines.get(engine)
        webbrowser.open(url)
    except Exception as e:
        messagebox.showerror("Erreur", "Erreur lors de l'ouverture du navigateur.")

# Configuration de l'interface graphique
root = tk.Tk()
root.title("Recherche d'image inversée")
root.geometry("400x300")

uploaded_image_path = None

# Étiquette d'instructions
instructions = tk.Label(root, text="Upload une image pour trouver sa source sur le web :")
instructions.pack(pady=10)

# Zone pour l'image
img_label = tk.Label(root)
img_label.pack(pady=10)

# Bouton pour uploader l'image
upload_button = tk.Button(root, text="Uploader une image", command=upload_image)
upload_button.pack(pady=5)

# Boutons de recherche
search_button = tk.Button(root, text="Recherche avec Google", command=lambda: search_image("Google"), state="disabled")
search_button.pack(pady=5)

tineye_button = tk.Button(root, text="Recherche avec TinEye", command=lambda: search_image("TinEye"), state="disabled")
tineye_button.pack(pady=5)

yandex_button = tk.Button(root, text="Recherche avec Yandex", command=lambda: search_image("Yandex"), state="disabled")
yandex_button.pack(pady=5)

# Lancer l'application
root.mainloop()
