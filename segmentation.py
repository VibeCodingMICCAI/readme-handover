"""Simple threshold-based image segmentation."""

import numpy as np

# Default threshold used for binary segmentation.
# TODO: make this configurable from the CLI (e.g. --threshold).
DEFAULT_THRESHOLD = 0.5


def segment(image: np.ndarray, threshold: float = DEFAULT_THRESHOLD) -> np.ndarray:
    """Create a binary segmentation mask from a 2D grayscale image.

    Pixels with intensity strictly greater than ``threshold`` are marked as
    foreground (1); all others are background (0).

    Note: NaN values compare as False against the threshold, so they are
    currently treated as background.
    # TODO: improve explicit NaN handling (e.g. warn or raise) rather than
    # silently treating NaNs as background.
    """
    mask = (image > threshold).astype(np.uint8)
    return mask
