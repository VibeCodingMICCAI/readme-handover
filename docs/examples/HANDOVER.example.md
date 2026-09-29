# Handover

Continuing-development notes for the next developer or AI agent.
Do not treat this as a user guide — see `README.md` for how to run the tool.

## 1. Current status

**Works today**

- CLI segmentation via `main.py --input` / `--output`
- Threshold mask in `segmentation.py` (`DEFAULT_THRESHOLD = 0.5`)
- `.npy` load/save with 2D validation in `utils.py`
- Auto-creates the output directory
- Refuses to overwrite the input file
- `pytest` suite in `tests/` (I/O + segmentation behaviour)

**Incomplete**

- Threshold is not configurable from the CLI
- Explicit NaN handling is still a TODO
- No support / testing for 3D medical volumes

## 2. Known issues

- NaNs become background (`0`) silently — see TODO in `segmentation.py`
- Only `.npy` is supported; other medical formats are out of scope for now
- 3D inputs raise `ValueError` by design; behaviour for real volumes is untested

## 3. Next tasks

1. Add `--threshold` to `main.py` and wire it through `segment()`
2. Improve NaN handling (warn or reject) instead of silent background
3. Decide whether 3D support is in scope; if yes, design slice/volume API

## 4. Important decisions and constraints

- Keep the tool dependency-light (NumPy + pytest only)
- Preserve binary `0`/`1` uint8-style masks
- Keep the input-overwrite safeguard in `main.py`
- Do not silently invent non-`.npy` formats without updating I/O + tests

## 5. Important files

- `main.py` — CLI, overwrite guard, success message
- `segmentation.py` — threshold constant + TODOs
- `utils.py` — 2D validation / save path creation
- `tests/test_segmentation.py`, `tests/test_io.py`

## 6. Verification

Before and after changes:

```bash
pytest
python main.py --input examples/sample_image.npy --output output/sample_mask.npy
```
