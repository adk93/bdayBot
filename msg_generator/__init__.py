# Standard library imports
import os

# Third party  imports
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# prompt = """
# Act as a happiness manager in a company that uses company's slack_client to wish each employee a happy birthday.\n
# Write a happy birthday text in Polish. Text should be cheerful, short, max 3 sentences. Text should include
# '@jan.kowalski' who is the birthday wishes recipient.
#
# Use this examples below to create new wishes for @jan.kowalski
#
# 1. 'Wszystkiego najwspanialszego w dniu Twojego święta @jan.kowalski! :royal-birthday-celebration:'
# 2. 'Samych pomyślności i samospełnienia @jan.kowalski! :birthday:
# 3. '@jan.kowalski, sto lat dziś dla Ciebie! :birthday:'
# 4. 'Dziś sto lat śpiewamy @jan.kowalski! :birthday:'
# 5. 'Samych radości i dużo słońca w dniu Twojego święta @jan.kowalski! :birthday_party_parrot:'
# """

with open(os.path.join('msg_generator', "prompt.txt")) as text:
    PROMPT = text.read()


def get_bday_wishes() -> str:
    response = openai.Completion.create(
        model="gpt-3.5-turbo-1106",
        prompt=PROMPT,
        temperature=0.8,
        max_tokens=128,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response.get('choices')[0].get('text')
