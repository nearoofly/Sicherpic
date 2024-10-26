# Sicherpic
Sicherpic help you get some information on all pictures you have to get information.

 **Sicherpic** :

```markdown
# Sicherpic - Recherche d'image inversée avec interface graphique

**Sicherpic** est un petit logiciel permettant d'**uploader une image** et de **lancer une recherche d'image inversée** à travers plusieurs moteurs de recherche (Google, TinEye, Yandex). Il utilise **Python** et **Tkinter** pour l'interface graphique.

## Auteur

GitHub : [nearoofly](https://github.com/nearoofly)

## Fonctionnalités

- Uploader une image depuis ton ordinateur.
- Lancer une recherche d'image inversée sur Google, TinEye, et Yandex.
- Ouvrir automatiquement le moteur de recherche sélectionné dans le navigateur par défaut.

## Prérequis

Avant de lancer le programme, assure-toi d’avoir installé les dépendances suivantes :

- Python 3.x
- Bibliothèques Python :
  ```bash
  pip install pillow requests
  ```

## Installation

1. Clone le dépôt GitHub :

   ```bash
   git clone https://github.com/nearoofly/Sicherpic.git
   cd Sicherpic
   ```

2. Installe les dépendances nécessaires (si elles ne sont pas déjà installées) :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lance le script principal :

   ```bash
   python sicherpic.py
   ```

2. Dans l'interface :
   - Clique sur "**Uploader une image**" pour sélectionner une image de ton ordinateur.
   - Une fois l'image chargée, sélectionne un moteur de recherche pour lancer une **recherche d'image inversée**.
   - Le navigateur s'ouvrira avec les résultats pour l'image uploadée.

## Aperçu du code

Le programme est composé des parties suivantes :

- **upload_image()** : Ouvre une boîte de dialogue pour choisir une image, qui sera affichée dans l’interface.
- **search_image(engine)** : Lance la recherche d’image inversée en ouvrant une URL spécifique pour le moteur sélectionné.
- **Interface Tkinter** : Interface utilisateur avec des boutons pour uploader une image et lancer les recherches.

## Limitations

Sicherpic effectue des recherches inversées de base via des URL de moteurs publics (Google, TinEye, Yandex). Actuellement, il ne prend pas en charge les recherches sur des réseaux privés (ex. : Telegram) ni les réseaux sociaux nécessitant des autorisations d'API spéciales.

## Contribuer

Les contributions sont les bienvenues ! Si tu souhaites ajouter de nouvelles fonctionnalités, améliorer le code ou corriger des bogues :

1. Fork le projet
2. Crée une branche pour ta fonctionnalité (`git checkout -b feature/NewFeature`)
3. Commit tes changements (`git commit -m 'Add NewFeature'`)
4. Push vers la branche (`git push origin feature/NewFeature`)
5. Crée une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d’informations.

## Contact

Pour toute question, n’hésite pas à me contacter via [GitHub](https://github.com/nearoofly).
```
