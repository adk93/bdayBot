# Standard library imports
import os

# Third party  imports
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": PROMPT
            }
        ]
    )

    return response.choices[0].message.content
