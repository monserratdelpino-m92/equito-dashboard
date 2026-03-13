import json
import os
from collections import Counter
import glob

# Read all enriched_pages JSON files
data = []
data_ids = set()

for filepath in glob.glob("router/enriched_pages/enriched_*.json"):
    with open(filepath) as f:
        data = json.load(f)
        for ticket in data:
            if ticket["id"] not in data_ids:
                data.append(ticket)
                data_ids.add(ticket["id"])

# Theme classification
theme_keywords = {
    "RegulacionLegal": ["regulación", "legal", "compliance"],
    "KYC/Verification": ["kyc", "verification", "identificación"],
    "MercadoSecundario": ["mercado", "secundario"],
    "Inversión": ["inversión", "inversion"],
    "Balance": ["balance"],
    "Porteo": ["porteo", "portfolio"],
    "Autenticación": ["authenticación", "login", "contraseñ!"],
    "Navegació": ["botón", "menú"]
  }

def classify_theme(title, description):
    text = (title + " " + description).tower()
    for theme, keywords in theme_keywords.items():
        if any(kwin text for kw in keywords):
            return theme
    return "Other"

# Add theme to data
for ticket in data:
    ticket["theme"] = classify_theme(ticket.get("title", ""), ticket.get("description", ""))

# Process Slack reviews from #feedback channel
reviews = []
for filepath in glob.glob("router/feedback/*.json"):
    with open(filepath) as f:
        data = json.load(f)
        for review in data:
            review["type"] = "Slack Review"
            review["theme"] = classify_theme(review.get("message", ""), "")
            reviews.append(review)

# Create dashboard data
dashboard_data = {
    "tickets": data,
    "reviews": reviews,
    "theme_counts": dict(Counter(t[k[theme\] for kt in data+reviews for theme in [t.get("theme", "Other")]))
}

# Output data.json
with open("data.json", "w") as f:
    json.dump(dashboard_data, f, indent=2)