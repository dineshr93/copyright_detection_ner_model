# copyright_detection_ner_model
## Basic pipeline to generate a copyright texts detection model from SPACY NER

An atempt to create a model exclusively to detect the literal copyright texts present in each source code.

## Installation

copyright_detection_ner_model requires [python](https://www.python.org/downloads/) v3.10+ , [scancode](https://github.com/aboutcode-org/scancode-toolkit/releases/tag/v32.3.2) v32.3.2 to run.

download multiple packages into the input folder and use extractcode to unpack the archive files
```sh
extractcode --shallow --replace-originals input/your_archive
```
```sh
python -m venv venv && source venv/bin/activate
git clone git@github.com:dineshr93/copyright_detection_ner_model.git && cd copyright_detection_ner_model && \
pip install -r requirements.txt
make b #starts the pipeline
```


## License
Copyright (c) 2025 Dinesh Ravi

[AGPL-3.0+](https://www.gnu.org/licenses/agpl-3.0.de.html)
