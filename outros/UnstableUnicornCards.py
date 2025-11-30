import os
import time
import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# -------- CONFIG --------
URL = "https://www.unicornsdatabase.com/"
SAVE_FOLDER = "unicorn_images"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# -------- INICIAR SELENIUM --------
chrome_options = Options()
chrome_options.add_argument("--headless=new")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

print("Carregando página...")
driver.get(URL)

# Esperar o Vue carregar
time.sleep(5)

# Selecionar todas as imagens
elements = driver.find_elements(By.CSS_SELECTOR, "#app > section > div > div a div img")
print(f"Imagens encontradas na página: {len(elements)}")

image_urls = []

for el in elements:
    src = el.get_attribute("src")
    if src and src not in image_urls:
        image_urls.append(src)

driver.quit()

print(f"URLs únicas encontradas: {len(image_urls)}")

# -------- BAIXAR E REDIMENSIONAR --------
for i, url in enumerate(image_urls, start=1):
    try:
        img_data = requests.get(url).content
        img = Image.open(BytesIO(img_data)).convert("RGB")

        # Redimensionar
        img = img.resize((250, 354), Image.LANCZOS)

        # Nome do arquivo
        filename = f"unicorn_{i}.jpg"
        path = os.path.join(SAVE_FOLDER, filename)

        img.save(path, "JPEG", quality=95)
        print(f"Salvo: {filename}")

    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")

print("\nPROCESSO CONCLUÍDO!")
