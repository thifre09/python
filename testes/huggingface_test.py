from transformers import pipeline
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

MODEL_NAME = "Qwen/Qwen2.5-VL-3B-Instruct"
PROMPT = "Há lixo nessa imagem? Responda apenas com sim ou não."
image = Image.open("a.JPG")


pipe = pipeline(
    "image-text-to-text",
    model=MODEL_NAME,
    device=1
)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": image
            },
            {
                "type": "text",
                "text": PROMPT
            }
        ]
    }
]

response = pipe(
    messages,
    max_new_tokens=100
)

print(response[0]["generated_text"][-1]["content"])