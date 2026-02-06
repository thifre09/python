import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import re

BASE = "https://vsbattles.fandom.com"
START_URL = BASE + "/wiki/Category:Characters"
headers = {"User-Agent": "Mozilla/5.0"}


# ============================================================
# → GET PAGE (tolerante a erros)
# ============================================================
def get_page(url):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(f"[ERRO GET] {url} -> {e}")
        return None


# ============================================================
# → EXTRATOR DE TIERS + CATEGORIAS
# ============================================================
def extract_tiers_and_categories(soup):
    tiers = []
    categories = []

    container = soup.select_one("div.page-header__categories")
    if not container:
        return tiers, categories

    links = container.select("a")

    for a in links:
        text = a.text.strip()

        if text == "Characters":
            continue

        if text.startswith("Tier"):
            tiers.append(text)
        else:
            categories.append(text)

    return tiers, categories


# ============================================================
# → EXTRATOR DE HABILIDADES DA ABA ATIVA
# ============================================================
def extract_abilities(soup):
    tab = soup.select_one("div.wds-tab__content.wds-is-current")
    if not tab:
        return []

    habilidades = []

    for ul in tab.select("ul"):
        for li in ul.select("li"):
            texto = li.get_text(" ", strip=True)
            if texto:
                habilidades.append(texto)

    return habilidades


# ============================================================
# → SALVAR LINKS EM ARQUIVO
# ============================================================
def save_links(links):
    with open("links_personagens.json", "w", encoding="utf-8") as f:
        json.dump(links, f, indent=2, ensure_ascii=False)
    print(f"\n✔ Salvo links em links_personagens.json ({len(links)} links)\n")


# ============================================================
# → CARREGAR LINKS SE EXISTIREM
# ============================================================
def load_links_if_exist():
    if os.path.exists("links_personagens.json"):
        try:
            with open("links_personagens.json", "r", encoding="utf-8") as f:
                links = json.load(f)
                print(f"\n✔ links_personagens.json encontrado ({len(links)} links)")
                print("⏩ Pulando coleta de links!")
                return links
        except:
            pass
    return None


# ============================================================
# → COLETAR TODOS OS LINKS
# ============================================================
def collect_all_links():
    characters = set()
    current_url = START_URL
    page_count = 0

    while current_url:
        page_count += 1
        print(f"\n=== Página {page_count} ===")
        print(f"URL: {current_url}")

        html = get_page(current_url)
        if not html:
            break

        soup = BeautifulSoup(html, "html.parser")

        for a in soup.select("#mw-content-text .category-page__members ul li a"):
            href = a.get("href")
            if not href or "Category:" in href:
                continue

            full_url = BASE + href
            name = a.text.strip()

            if name:
                characters.add(full_url)
                print("Coletado link:", name)

        next_button = soup.select_one("a.category-page__pagination-next")
        if next_button:
            href = next_button.get("href")
            current_url = href if href.startswith("http") else BASE + href
        else:
            current_url = None

    links = list(characters)
    save_links(links)
    return links


# ============================================================
# → EXTRAÇÃO DE 1 PERSONAGEM
# ============================================================
def extract_info(url):
    try:
        html = get_page(url)
        if not html:
            return None

        soup = BeautifulSoup(html, "html.parser")

        name_tag = soup.select_one("h1")
        name = name_tag.text.strip() if name_tag else "??"

        summary = None
        h2 = soup.find(id="Summary")
        if h2:
            p = h2.find_next("p")
            if p:
                summary = p.text.strip()

        tiers, categories = extract_tiers_and_categories(soup)

        info = {
            "name": name,
            "url": url,
            "tiers": tiers,
            "categories": categories,
            "summary": summary,
            "abilities": extract_abilities(soup)
        }

        print("Processado:", name)
        return info

    except Exception as e:
        print(f"[ERRO extract] {url} -> {e}")
        return None


# ============================================================
# → SALVAR JSONL DURANTE O PROCESSO
# ============================================================
def save_jsonl(data, filename="personagens_temp.jsonl"):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
    except Exception as e:
        print("[ERRO salvar JSONL]", e)


# ============================================================
# → PROCESSAMENTO PARALELO
# ============================================================
def process_all(links, threads=40):
    print("\nIniciando scraping paralelo...\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(extract_info, url) for url in links]

        for f in as_completed(futures):
            data = f.result()
            if data:
                save_jsonl(data)


# ============================================================
# → JSON FINAL LEGÍVEL
# ============================================================
def create_final_json():
    print("\nGerando JSON final...")

    all_items = []

    if os.path.exists("personagens_temp.jsonl"):
        with open("personagens_temp.jsonl", "r", encoding="utf-8") as f:
            for line in f:
                try:
                    all_items.append(json.loads(line))
                except:
                    pass

    all_items.sort(key=lambda x: x["name"])

    with open("personagens_vsbattles.json", "w", encoding="utf-8") as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)

    print("✔ Criado: personagens_vsbattles.json")


# ============================================================
# → MAIN
# ============================================================
if __name__ == "__main__":
    links = load_links_if_exist()
    if links is None:
        links = collect_all_links()

    process_all(links)
    create_final_json()

    print("\nFINALIZADO COM SUCESSO!\n")
