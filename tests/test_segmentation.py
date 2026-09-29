"""Tests for threshold segmentation."""

import numpy as np

from segmentation import DEFAULT_THRESHOLD, segment


def test_output_is_binary():
    image = np.array([[0.1, 0.9], [0.4, 0.6]], dtype=float)
    mask = segment(image)
    assert set(np.unique(mask)).issubset({0, 1})


def test_output_shape_matches_input():
    image = np.random.rand(32, 48)
    mask = segment(image)
    assert mask.shape == image.shape


def test_threshold_behaviour():
    image = np.array(
        [
            [0.0, DEFAULT_THRESHOLD, DEFAULT_THRESHOLD + 0.01],
            [0.2, 0.8, 1.0],
        ],
        dtype=float,
    )
    mask = segment(image, threshold=DEFAULT_THRESHOLD)
    expected = np.array([[0, 0, 1], [0, 1, 1]], dtype=np.uint8)
    np.testing.assert_array_equal(mask, expected)


def test_nan_treated_as_background():
    """Known limitation: NaN values become background (0)."""
    image = np.array([[np.nan, 0.9], [0.1, np.nan]], dtype=float)
    mask = segment(image)
    expected = np.array([[0, 1], [0, 0]], dtype=np.uint8)
    np.testing.assert_array_equal(mask, expected)
