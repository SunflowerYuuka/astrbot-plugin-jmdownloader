import unittest
from pathlib import Path

from upload_uri import upload_file_value


class UploadUriTests(unittest.TestCase):
    def test_converts_absolute_path_to_file_uri(self):
        pdf_path = Path("/tmp/astrbot_jmdownloader/job/1465788.pdf")

        self.assertEqual(
            upload_file_value(pdf_path, "file_uri"),
            pdf_path.resolve().as_uri(),
        )

    def test_preserves_legacy_path_mode(self):
        pdf_path = Path("/tmp/astrbot_jmdownloader/job/1465788.pdf")

        self.assertEqual(
            upload_file_value(pdf_path, "legacy"),
            str(pdf_path.resolve()),
        )


if __name__ == "__main__":
    unittest.main()
