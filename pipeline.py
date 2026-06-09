import os

DOCUMENTS_DIR = "documents"

# Maps filename → (title, url)
DOCUMENT_METADATA = {
    "Information about all the residential housing on-campus.txt": (
        "A Guide to Residential Life at Haverford",
        "https://www.reddit.com/r/Haverford/comments/1tj0y90/a_guide_to_residential_life_at_haverford/",
    ),
    "Social Scene at Haverford.txt": (
        "Social Scene at Haverford",
        "https://www.reddit.com/r/Haverford/comments/ti98st/social_scene_at_haverford/",
    ),
    "Reddit thread for QnA about Haverford.txt": (
        "Reddit QnA about Haverford",
        "https://www.reddit.com/r/Haverford/comments/7ngl51/anyone_who_is_applying_have_questions_about/",
    ),
    "Another advice QnA thread.txt": (
        "Another Advice/QnA Thread",
        "https://www.reddit.com/r/Haverford/comments/1bfvbeg/class_of_27_28/",
    ),
    "A freshman guide to Haverford College.txt": (
        "A Freshman Guide to Haverford College",
        "https://generalintelligences.wordpress.com/2020/05/16/a-freshman-guide-to-haverford-college/",
    ),
    "Freshman reflection on first month of Haverford College.txt": (
        "Freshmen Reflect on the First Month of College",
        "https://haverfordclerk.com/freshmen-reflect-on-the-first-month-of-college/",
    ),
    "A first-year's experience about Customs (Orientation).txt": (
        "Customs Gave Me a Community: A First-Year Perspective",
        "https://haverfordclerk.com/customs-gave-me-a-community-a-first-year-perspective/",
    ),
    "Dining Culture at Haverford according to a Transfer Student.txt": (
        "Handle With Care: Is Our Dining Center Culture Healthy?",
        "https://haverfordclerk.com/handle-with-care-is-our-dining-center-culture-healthy/",
    ),
    "Haverford vs Bryn Mawr Dining Halls.txt": (
        "Haverford vs Bryn Mawr Dining Halls",
        "https://bicollegenews.com/2019/10/05/opinion-haverford-vs-bryn-mawrs-dining-halls/",
    ),
    "Campus Life Review of Haverford.txt": (
        "Campus Life Review of Haverford",
        "https://www.niche.com/colleges/haverford-college/campus-life/",
    ),
}


def load_documents():
    documents = []
    for filename, (title, url) in DOCUMENT_METADATA.items():
        filepath = os.path.join(DOCUMENTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read().strip()
        documents.append({"title": title, "url": url, "text": text})
    return documents


def chunk_text(text, chunk_size=700, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def build_chunks(documents):
    all_chunks = []
    for doc in documents:
        text_chunks = chunk_text(doc["text"])
        for chunk in text_chunks:
            all_chunks.append({
                "title": doc["title"],
                "url": doc["url"],
                "text": chunk,
            })
    return all_chunks


if __name__ == "__main__":
    documents = load_documents()
    print(f"Loaded {len(documents)} documents\n")

    all_chunks = build_chunks(documents)
    print(f"Total chunks: {len(all_chunks)}\n")

    print("--- 5 sample chunks ---\n")
    step = max(1, len(all_chunks) // 5)
    for i in range(0, min(5 * step, len(all_chunks)), step):
        chunk = all_chunks[i]
        print(f"[Chunk {i}] Source: {chunk['title']}")
        print(f"URL: {chunk['url']}")
        print(f"Text: {chunk['text'][:300]}...")
        print()
