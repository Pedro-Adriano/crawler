import unicodedata

def load_mockup(mockup_name, encoding="utf-8"):
    with  open(f"testes/mockup/{mockup_name}", encoding=encoding, mode="r") as f:
        return f.read()

def normalize_text(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")