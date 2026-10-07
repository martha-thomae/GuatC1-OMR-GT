# GuatC1-OMR-GT
This repository contains the ground truth OMR files for the manuscript GuatC 1, these consist of:
- images of each of the staff regions in the pages of the manuscript
- and the encoding of the sequence of music symbols in said regions, which are provided in two formats (as done by the _Music Recognition Encoding and Transcription (MuRET)_ OMR framework):
  - agnostic encoding
  - semantic encoding

The ready-to-use files are in the [processed folder](./processed), where the staff region images and the two encodings are found for each of the 27 pieces included in the manuscript. These files were extracted from MuRET's original output, which can be found in the [original folder](./original), with 27 _JSON files_ that include the information needed to extract the individual staff images and encodings. Each JSON file corresponds to one piece in the manuscript, and it contains information about all the regions in said piece. The information for each region includes:
- `image_name`: name of the image that contains the region
- `image_id`: ID of the image
- `region_id`: ID of the region
- `url`: URL of the image
- `bounding_box`: Coordinates for the region (which are used together with the URL to extract the staff region image found in the [processed](./processed) folder)
- `semantic`: semantic encoding for the sequence of symbols in the region
- `agnostic`: agnostic encoding for the sequence of symbols in the region

For example, for the first region of the [first piece (Asperges me)](https://github.com/OmniOMR/mensomr_data/blob/e1dff105ddf86c8a8edb70bbcee2fa388cbe2535/muret_guatemala/original/01_Asperges-me.json#L3-L16), we have the following data:

```JSON
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
