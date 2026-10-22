import re


INVALID_FILENAME_CHARS = re.compile(r'[\\/:*?"<>|\x00-\x1f]')


def safe_pdf_name(album_id: str, title: str, include_title: bool = True) -> str:
    """Build a QQ-compatible PDF name, optionally without the album title."""
    if not include_title:
        return f"JM{album_id}.pdf"

    cleaned = INVALID_FILENAME_CHARS.sub("_", str(title)).strip(" ._")
    cleaned = re.sub(r"\s+", " ", cleaned)[:70]
    return f"JM{album_id}-{cleaned}.pdf" if cleaned else f"JM{album_id}.pdf"
