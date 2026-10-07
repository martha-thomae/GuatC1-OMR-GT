import json
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image


INPUT_DIR = Path("original")
OUTPUT_DIR = Path("processed")


def extract_staff_image(region, output_dir, session):
    """Download an image, crop it to the region's bounding box, and save it."""
    try:
        response = session.get(region["url"])
        response.raise_for_status()

        bbox = region["bounding_box"]
        coordinates = (
            bbox["fromX"],
            bbox["fromY"],
            bbox["toX"],
            bbox["toY"],
        )

        image = Image.open(BytesIO(response.content))
        cropped = image.crop(coordinates)

        output_file = (
            output_dir
            / f"Folio{region['image_name'][:-4]}"
            f"_Region{region['region_id']}_img.jpg"
        )

        cropped = cropped.convert("RGB")
        cropped.save(output_file)

    except requests.exceptions.RequestException as e:
        print(f"Failed ot download {region['ulr']}")
        print(f"Error: {e}")


def save_encoding(region, encoding_type, output_dir):
    """Save a region's encoding to a text file."""
    seq = region[encoding_type]

    output_file = (
        output_dir
        / f"Folio{region['image_name'][:-4]}"
        f"_Region{region['region_id']}_{encoding_type[:3]}.txt"
    )
    clean_sequence = " ".join(seq.split(', '))
    output_file.write_text(clean_sequence, encoding="utf-8")


def process_file(filepath, session):
    """Process on JSON file and all of its regions."""
    with filepath.open("r", encoding="utf-8") as f:
        musicwork = json.load(f)

    output_dir = OUTPUT_DIR / filepath.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    for region in musicwork["regions"]:
        extract_staff_image(region, output_dir, session)
        save_encoding(region, "agnostic", output_dir)
        save_encoding(region, "semantic", output_dir)


def main():
    with requests.Session() as session:
        print("-- START --")
        for filepath in INPUT_DIR.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                print(f"Processing file: {filepath.name}")
                process_file(filepath, session)
                print("(complete)")
        print("-- END --")


if __name__ == "__main__":
    main()