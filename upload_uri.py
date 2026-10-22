import base64
from pathlib import Path


def upload_file_value(file_path: Path, mode: str = "file_uri") -> str:
    """Format a local path for OneBot file upload actions."""
    resolved_path = file_path.resolve()
    normalized_mode = mode.strip().lower()
    if normalized_mode == "base64":
        encoded = base64.b64encode(resolved_path.read_bytes()).decode("ascii")
        return f"base64://{encoded}"
    if normalized_mode == "legacy":
        return str(resolved_path)
    return resolved_path.as_uri()
