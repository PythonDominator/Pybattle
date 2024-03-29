from pathlib import Path
from shutil import rmtree


def remove_cache(directory: Path) -> dict[Path, Path | dict[Path, Path | dict]]:
    """Get all the .py files and folders in a directory."""
    dct = {}
    for path in directory.glob("*"):
        if path.is_dir():
            if path.name == "__pycache__":
                rmtree(path)
            remove_cache(path)
    return dct


if __name__ == "__main__":
    remove_cache(
        Path(r"C:\Users\jacob\Downloads\Programming\Python\Pybattle\Github\pybattle")
    )
