# Image Segmentation Tool

Small Python demo that creates a **binary segmentation mask** from a 2D grayscale image stored as a `.npy` file. Segmentation is a simple intensity threshold (no deep learning).

## Main workflow

1. Load a 2D `.npy` image
2. Threshold pixels to build a mask of `0` / `1`
3. Save the mask as another `.npy` file

## Setup

```bash
pip install -r requirements.txt
```

Dependencies: NumPy, pytest.

## Run

```bash
python main.py --input examples/sample_image.npy --output output/sample_mask.npy
```

Expected terminal output:

```text
Segmentation completed.
Output saved to: output/sample_mask.npy
```

## Inputs and outputs

| | |
|---|---|
| **Input** | 2D NumPy array in a `.npy` file (grayscale intensities) |
| **Output** | Same shape as input; values are only `0` (background) and `1` (foreground) |
| **Sample data** | `examples/sample_image.npy` (64×64, bright region in the centre) |

## Repository structure

```text
main.py              CLI entry point (--input, --output)
segmentation.py      Threshold segmentation (DEFAULT_THRESHOLD = 0.5)
utils.py             Load / save .npy helpers
examples/            Sample input image
tests/               pytest suite
```

## Verify

```bash
pytest
```

## Known limitations

- Threshold is hard-coded to `0.5` (not yet a CLI flag)
- Only 2D `.npy` images are supported; 3D volumes are rejected
- NaN pixels are currently treated as background
- Output path must differ from the input path (overwrite safeguard)
