"""Tests for .npy load/save helpers."""

from pathlib import Path

import numpy as np
import pytest

from utils import load_image, save_mask


def test_save_and_load_roundtrip(tmp_path: Path):
    original = np.array([[0.1, 0.5], [0.8, 0.2]], dtype=float)
    path = tmp_path / "image.npy"
    save_mask(original, path)

    loaded = load_image(path)
    np.testing.assert_array_equal(loaded, original)


def test_save_creates_parent_directory(tmp_path: Path):
    nested = tmp_path / "nested" / "out" / "mask.npy"
    mask = np.array([[0, 1], [1, 0]], dtype=np.uint8)
    saved = save_mask(mask, nested)
    assert saved.exists()
    assert saved.parent.is_dir()


def test_load_rejects_3d_array(tmp_path: Path):
    path = tmp_path / "volume.npy"
    np.save(path, np.zeros((4, 4, 4)))
    with pytest.raises(ValueError, match="Expected a 2D image"):
        load_image(path)


def test_load_rejects_1d_array(tmp_path: Path):
    path = tmp_path / "vector.npy"
    np.save(path, np.zeros(10))
    with pytest.raises(ValueError, match="Expected a 2D image"):
        load_image(path)


def test_load_missing_file(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        load_image(tmp_path / "does_not_exist.npy")
