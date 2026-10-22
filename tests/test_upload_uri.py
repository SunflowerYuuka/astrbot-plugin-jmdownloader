import unittest
import ast
from pathlib import Path

from upload_uri import upload_file_value


class UploadUriTests(unittest.TestCase):
    def test_plugin_uses_package_relative_helper_import(self):
        main_path = Path(__file__).parents[1] / "main.py"
        tree = ast.parse(main_path.read_text(encoding="utf-8"))

        self.assertTrue(
            any(
                isinstance(node, ast.ImportFrom)
                and node.module == "upload_uri"
                and node.level == 1
                for node in ast.walk(tree)
            ),
        )

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
