import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("data/clinic_info.json") as f:
    faq_data = json.load(f)

def answer_faq(question):
    context = " ".join([faq["answer"] for faq in faq_data])
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Answer using clinic info context: "+context},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
