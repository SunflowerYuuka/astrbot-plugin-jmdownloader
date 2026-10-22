from pathlib import Path


def upload_file_value(file_path: Path, mode: str = "file_uri") -> str:
    """Format a local path for OneBot file upload actions."""
    resolved_path = file_path.resolve()
    if mode.strip().lower() == "legacy":
        return str(resolved_path)
    return resolved_path.as_uri()
