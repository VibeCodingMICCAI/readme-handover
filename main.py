"""CLI entry point for the segmentation tool."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from segmentation import segment
from utils import load_image, save_mask


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Segment a 2D grayscale image using a simple threshold."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to input .npy image (2D grayscale).",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to output .npy mask.",
    )
    # TODO: add --threshold CLI argument (currently hard-coded in segmentation.py).
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    input_path = Path(args.input).resolve()
    output_path = Path(args.output).resolve()

    # Safeguard: never overwrite the input file.
    if output_path == input_path:
        print(
            f"Error: output path must differ from input path ({input_path}).",
            file=sys.stderr,
        )
        return 1

    image = load_image(input_path)
    mask = segment(image)
    save_mask(mask, output_path)

    print("Segmentation completed.")
    print(f"Output saved to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
