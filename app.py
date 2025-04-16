# app.py — AI Recruitment Bureau Prototype

from flask import Flask, render_template, request
import os
import openai
from crewai import Crew, Agent, Task
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.llms import OpenAI
from PIL import Image
import requests
import io
from dotenv import load_dotenv

# Laad omgevingsvariabelen vanuit .env bestand
load_dotenv()

# Setup Flask
app = Flask(__name__)

# Zorg dat je OpenAI API key ingesteld is
openai.api_key = os.getenv("OPENAI_API_KEY")

# Stel een paar basistools en LLM in
llm = OpenAI(temperature=0)
search_tool = DuckDuckGoSearchRun()

# Functie om afbeelding te genereren met DALL·E
def generate_visual(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    image_url = None
    if request.method == 'POST':
        functie = request.form['functie']
        locatie = request.form['locatie']

        jobomschrijving = f"{functie} in {locatie}"

        # AI-agenten
        strategic_director = Agent(
            role="Strategisch Directeur",
            goal="Bepaal de algemene rekruteringsstrategie en stuur de AI-teams aan",
            backstory="Je leidt creatieve en effectieve rekruteringscampagnes.",
            verbose=True,
            llm=llm
        )

        recruiter = Agent(
            role="Rekruteringsspecialist",
            goal="Ontwikkel wervende vacatureteksten op basis van klantbehoeftes",
            backstory="Je vertaalt de jobnoden van klanten in aantrekkelijke teksten.",
            verbose=True,
            llm=llm
        )

        copywriter = Agent(
            role="Copywriter",
            goal="Schrijf wervende content voor jobposts en social media",
            backstory="Je gebruikt je flair voor taal om jobs aantrekkelijk te maken.",
            verbose=True,
            llm=llm
        )

        campaign_manager = Agent(
            role="Campagnebeheerder",
            goal="Plan en optimaliseer jobcampagnes online",
            backstory="Je zorgt dat elke jobpost de juiste doelgroep bereikt.",
            verbose=True,
            llm=llm
        )

        graphic_designer = Agent(
            role="Grafisch Ontwerper",
            goal="Genereer visuele content bij de vacature",
            backstory="Je bent een AI-ontwerper die visuals maakt met AI tools.",
            verbose=True,
            llm=llm
        )

        # Taken
        job_analysis = Task(
            description=f"Analyseer het profiel van '{jobomschrijving}' en geef aanbevelingen voor targeting.",
            agent=recruiter,
            expected_output="Doelgroepanalyse en wervingsadvies."
        )

        write_job_post = Task(
            description=f"Schrijf een krachtige vacaturetekst voor een {jobomschrijving}.",
            agent=copywriter,
            expected_output="Een volledige vacaturetekst die klaar is voor publicatie."
        )

        plan_campaign = Task(
            description=f"Maak een plan om de vacature '{jobomschrijving}' te verspreiden via social media, jobboards, enz.",
            agent=campaign_manager,
            expected_output="Een concreet en bruikbaar campagneplan."
        )

        generate_visual_task = Task(
            description=f"Genereer een visuele representatie van een {jobomschrijving}. Denk aan kantooromgeving, professionele sfeer, en wervende uitstraling.",
            agent=graphic_designer,
            expected_output="Een visuele prompt of gegenereerde afbeelding."
        )

        overview_task = Task(
            description=f"Overzicht van de campagne en optimalisatievoorstellen voor het team.",
            agent=strategic_director,
            expected_output="Samenvatting van de samenwerking en optimalisatie-ideeën."
        )

        # Combineer alles in een crew
        crew = Crew(
            agents=[strategic_director, recruiter, copywriter, campaign_manager, graphic_designer],
            tasks=[job_analysis, write_job_post, plan_campaign, generate_visual_task, overview_task],
            verbose=True
        )

        result = crew.kickoff()
        image_prompt = f"Professional and modern visual for a {functie} job in {locatie}. Office setting, dynamic and engaging."
        image_url = generate_visual(image_prompt)

    return render_template('index.html', result=result, image_url=image_url)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
