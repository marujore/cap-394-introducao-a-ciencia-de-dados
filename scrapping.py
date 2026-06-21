import json
import re
import requests
from bs4 import BeautifulSoup

URL = "http://mtc-m16c.sid.inpe.br/col/sid.inpe.br/mtc-m18@80/2008/03.17.15.17.24/doc/mirrorget.cgi?metadatarepository=sid.inpe.br/mtc-m16c/2025/05.29.18.05.45&choice=full&languagebutton=en"

response = requests.get(URL, timeout=30)
response.raise_for_status()

response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

def get_field(name):
    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) != 2:
            continue
        key = cells[0].get_text(" ", strip=True)
        if key == name:
            return cells[1].get_text(" ", strip=True)
    return None


title = get_field("Title")
abstract = get_field("Abstract")
article_type = get_field("Tertiary Type")
language = get_field("Language")
conference_name = get_field("Conference Name")
author = get_field("Author")
affiliations = get_field("Affiliation")

edition = None
if conference_name:
    m = re.search(r",\s*(\d+)\s*\(", conference_name)
    if m:
        edition = int(m.group(1))

metadata = {
    "title": title,
    "abstract": abstract,
    "article_type": article_type,
    "language": language,
    "event_edition": edition,
    "author": author,
    "affiliation": affiliations
}

print(metadata)

if metadata["article_type"] == "Full paper":
    metadata["article_type"] = "full"
if metadata["article_type"] == "Short paper":
    metadata["article_type"] = "short"
if metadata["language"] == "en":
    metadata["language"] = "english"
if metadata["language"] == "pt":
    metadata["language"] = "portuguese"

# Authors extraction and formatting
raw_authors = re.findall(r'\d+\s+(.*?)(?=\s+\d+\s+|$)', metadata["author"])
raw_authors = [name.strip() for name in raw_authors]
# Convert "Last, First" to "First Last"
formatted_authors = [
    f"{first_name.strip()} {last_name.strip()}" 
    if ',' in author 
    else author
    for author in raw_authors
    for last_name, first_name in [author.split(',', 1)] if ',' in author
]
metadata["author"] = formatted_authors

raw_affiliations = re.findall(r'\d+\s+(.*?)(?=\s+\d+\s+|$)', metadata["affiliation"])
raw_affiliations = [aff.strip() for aff in raw_affiliations]
# Clean up encoding issues (replace \ufffd with –)
formatted_affiliations = [
    aff.replace('\ufffd', '–').replace('�', '–') 
    for aff in raw_affiliations
]

metadata["affiliation"] = formatted_affiliations

print(json.dumps(metadata, indent=4))
