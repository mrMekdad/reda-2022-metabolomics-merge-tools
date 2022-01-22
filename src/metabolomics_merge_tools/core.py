"""Core workflow for Metabolomics Merge Tools by Red@."""

PROJECT_NAME = "Metabolomics Merge Tools"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
