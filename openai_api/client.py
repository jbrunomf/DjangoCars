import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def get_car_description(model, brand, model_year):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    input = f"Descreva o veículo {model} da marca {brand} ano do modelo {model_year} de forma resumida (em até 250 caracteres) e citando os pontos fortes em relação aos seus principais concorrentes."

    response = client.responses.create(
        model="gpt-4.1",
        input=input,
    )

    print(response.output_text)

    return "ok"
