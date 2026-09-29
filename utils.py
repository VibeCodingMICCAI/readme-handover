"""I/O helpers for .npy image files."""

from __future__ import annotations

from pathlib import Path

import numpy as np


def load_image(path: str | Path) -> np.ndarray:
    """Load a 2D grayscale image from a .npy file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the array is not 2D.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    image = np.load(path)

    if image.ndim != 2:
        raise ValueError(
            f"Expected a 2D image, got array with shape {image.shape} "
            f"({image.ndim}D). Only 2D .npy images are currently supported; "
            "3D medical volumes have not been tested."
        )

    return image


def save_mask(mask: np.ndarray, path: str | Path) -> Path:
    """Save a segmentation mask as a .npy file.

    Creates the parent directory automatically if it does not exist.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    np.save(path, mask)
    return path
