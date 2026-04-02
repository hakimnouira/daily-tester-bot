import random
import requests
import os
from datetime import datetime

# 👥 Team members
users = [
    "Nahed Rahmani",
    "Mohamed Bizani",
    "Hakim Nouira",
    "Wassim Hajji"
]

# 🎯 Random tester
tester = random.choice(users)

# 🌍 Slack webhook
webhook_url = os.environ["SLACK_WEBHOOK"]

# 🇫🇷 Final message
message = {
    "text": f"""
🤖 Bonjour à tous,

Je suis le bot de rotation des tests.

Chaque jour, je sélectionne aléatoirement un membre de l’équipe pour prendre en charge les tests des tickets présents dans la colonne *"Test"* sur Jira.

📌 Règles à respecter :
• Le testeur du jour doit tester tous les tickets en statut *Test*
• ❌ Il est interdit de tester ses propres tickets
• 👉 Si le testeur a lui-même des tickets dans *Test*, il doit les ignorer
• ✔️ Ces tickets seront testés par un autre membre lors d’une prochaine rotation

👨‍💻 Testeur du jour ({datetime.now().strftime('%A')}) :
👉 *{tester}*

🙏 Merci de réagir à ce message (👍) afin de confirmer que vous l’avez bien vu.

Merci pour votre collaboration et bon travail à tous 🚀
"""
}

# 📤 Send to Slack
requests.post(webhook_url, json=message)
