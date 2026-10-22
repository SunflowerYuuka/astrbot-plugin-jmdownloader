import unittest

from filename import safe_pdf_name


class PdfFilenameTests(unittest.TestCase):
    def test_can_remove_title_for_upload_compatibility(self):
        self.assertEqual(
            safe_pdf_name("1465788", "A title", include_title=False),
            "JM1465788.pdf",
        )

    def test_keeps_sanitized_title_by_default(self):
        self.assertEqual(
            safe_pdf_name("1465788", "A:/title"),
            "JM1465788-A__title.pdf",
        )


if __name__ == "__main__":
    unittest.main()
