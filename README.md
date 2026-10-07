# GuatC1-OMR-GT

This repository contains the ground-truth Optical Music Recognition (OMR) data for **GuatC 1**, a polyphonic choirbook in mensural notation, containing 27 music works. For a full digital edition of _GuatC 1_, please consult the [GitHub Repo ***GuatC 1***](https://github.com/martha-thomae/GuatC1). The present repository, however, is for the OMR ground truth data generated while processing this manuscript. It contains the equivalent of 384 pages of annotated data (folios 1v to 193r).

The OMR ground truth data consists of:

- **Images of the staff regions** found on the manuscript pages.
- **Encodings of the sequences of music symbols** in each staff region, provided in two formats, following the output formats of the *Music Recognition Encoding and Transcription (MuRET)* OMR framework:
  - **Agnostic encoding**
  - **Semantic encoding**

## Repository structure

The repository contains two main folders:

- [`processed`](./processed): contains the ready-to-use ground-truth files. The folder is divided into 27 sub-folders (corresponding to the 27 pieces of the manuscript). These subfolders contain the staff-region images and their corresponding agnostic and semantic encodings.
- contains the ready-to-use ground-truth files. The directory is divided into 27 folders, each corresponding to one of the 27 pieces of the manuscript. Each of these folders contains the staff-region images and their corresponding agnostic and semantic encodings.
- [`original`](./original): contains the original output produced by MuRET. It consists of 27 JSON files, one for each piece. Each JSON file contains the information needed to identify and extract the individual staff regions and their corresponding encodings.

### Processed files

The files in the `processed` folder are organized by piece and contain the individual staff-region images together with their corresponding encodings. These files can be used directly as ground-truth data for OMR experiments.

### Original MuRET output

Each JSON file in the `original` folder corresponds to one piece in the manuscript and contains information about all the staff regions belonging to that piece.

For each region, the following information is provided:

| Field | Description |
|---|---|
| `image_name` | Name of the manuscript page image containing the region. |
| `image_id` | Identifier of the manuscript page image within MuRET. |
| `region_id` | Identifier of the staff region within MuRET. |
| `url` | URL of the manuscript page image. |
| `bounding_box` | Coordinates defining the staff region within the page image. These coordinates, together with the `url`, were used to extract the corresponding staff-region image (as found in the `processed` sub-folders). |
| `semantic` | Semantic encoding of the sequence of music symbols in the region. |
| `agnostic` | Agnostic encoding of the sequence of music symbols in the region. |

#### Example
For example, for the first region of the [first piece, *Asperges me*](https://github.com/OmniOMR/mensomr_data/blob/e1dff105ddf86c8a8edb70bbcee2fa388cbe2535/muret_guatemala/original/01_Asperges-me.json#L3-L16), is represented as follows:

```json
{
    "regions": [
        {
            "image_name": "1v.jpg",
            "semantic": "*clefG2\n*met(C)\n[sdd\nsee]\nsff#\nsgg\nsee\ns.dd\nMcc\nsb\nscc\n[sdd\nsg]\n[sa\nsb]\nsr_3\nsee\nsdd\nscc\n*custosb\n",
            "bounding_box": {
                "fromX": 240,
                "toX": 1105,
                "fromY": 123,
                "toY": 267
            },
            "region_id": 25073,
            "agnostic": "clef.G:L2, metersign.Ct:L3, lnote.rect_up_left:L4, lnote.rect:S4, accidental.sharp:S3, note.whole:L5, note.whole:S5, note.whole:S4, note.whole:L4, dot:S3, note.half_down:S3, note.whole:L3, note.whole:S3, lnote.rect_up_left:L4, lnote.rect:L2, ligature_separator:L1, lnote.rect_up_left:S2, lnote.rect:L3, rest.whole:L3, note.whole:S4, note.whole:L4, note.whole:S3, custos:L3",
            "image_id": 2728,
            "url": "https://muret.dlsi.ua.es/images/iiif/2/6%3A208:masters:1v.jpg/full/full/0/default.jpg"
        },
        ...
    ]
}
```

The `bounding_box` coordinates identify the staff region within the page image specified by `url`. The `semantic` and `agnostic` fields contain the two corresponding representations of the musical symbols in that region.

## Dataset
The dataset contains **27 pieces** from the GuatC 1 manuscript. Each piece is represented by one JSON file in the `original` folder and by one sub-folder that contains its corresponding staff-region images and encodings in the `processed` folder.

### Provenance
The `original` JSON files were obtained from MuRET, the OMR framework used to process this full manuscript book. The JSON files were extracted by MuRET's developer, David Rizo.

## References
Thomae, M.E. (2026) ‘Semi‑Automatic Pipeline for the Transcription of Mensural Polyphony into Symbolic Interpreted Scores’, Transactions of the International Society for Music Information Retrieval, 9(1), p. 293–308. Available at: https://doi.org/10.5334/tismir.292.
