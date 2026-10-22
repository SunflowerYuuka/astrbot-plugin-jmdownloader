import tempfile
import unittest
from pathlib import Path

from pypdf import PdfReader, PdfWriter

from pdf_security import encrypt_pdf


class PdfSecurityTests(unittest.TestCase):
    def test_encrypts_pdf_with_numeric_album_id(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source.pdf"
            target = Path(temp_dir) / "protected.pdf"
            writer = PdfWriter()
            writer.add_blank_page(width=100, height=100)
            with source.open("wb") as source_file:
                writer.write(source_file)

            encrypt_pdf(source, target, "1465788")

            reader = PdfReader(str(target))
            self.assertTrue(reader.is_encrypted)
            self.assertEqual(reader.decrypt("1465788"), 2)


if __name__ == "__main__":
    unittest.main()
