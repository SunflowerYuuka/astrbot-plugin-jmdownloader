from pathlib import Path

from pypdf import PdfReader, PdfWriter


def encrypt_pdf(source_path: Path, target_path: Path, password: str) -> None:
    """Write an encrypted copy of a PDF using the supplied password."""
    reader = PdfReader(str(source_path))
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password, algorithm="AES-256")
    with target_path.open("wb") as output_file:
        writer.write(output_file)
