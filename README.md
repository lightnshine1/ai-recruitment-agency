[README.md](https://github.com/user-attachments/files/19777142/README.md)[Uploadin# Virtueel AI Rekruteringbureau (Open-Source Editie)

Dit project is een AI-gedreven communicatie- en rekruteringsbureau, volledig opgebouwd rond open-source taalmodellen via Hugging Face.

## ✅ Functionaliteiten
- Agents voor strategie, copywriting, campagneplanning, design, etc.
- Analyseert functies en genereert jobcampagnes
- Werkt met gratis LLM via Hugging Face
- Webinterface in Flask

---

## 🚀 Installatie (lokaal)

1. **Clone de repo of download dit project**

2. **Installeer de vereiste libraries**

```bash
pip install -r requirements.txt
```

3. **Stel je `.env` bestand in**

Maak een `.env` bestand in de hoofdmap met deze inhoud:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

Je kunt een token verkrijgen via: https://huggingface.co/settings/tokens

4. **Start de app**

```bash
python app.py
```

De app draait dan op: `http://localhost:5000`

---

## 🌐 Online zetten via Render

1. Maak een nieuwe Web Service aan op https://render.com
2. Koppel aan je GitHub repo
3. Voeg volgende environment variable toe:

| Key                     | Value                    |
|------------------------|--------------------------|
| `HUGGINGFACEHUB_API_TOKEN` | *je Hugging Face token*   |

4. Build command: *(automatisch)*
5. Start command:
```bash
python app.py
```

De app wordt automatisch gehost op een publieke link van Render.

---

## 🧠 Gebruikte tools

- `crewai` (AI agents en taakverdeling)
- `langchain-community` (Hugging Face integratie)
- `DuckDuckGoSearch` (optionele zoekopdrachten)
- `Flask` (webserver)
- `dotenv` (omgevingsvariabelen)
g README.md…]()
