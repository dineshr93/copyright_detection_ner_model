import json
import re

TRAINING_DATA_FILE = "data/training_data.json"
NER_TRAIN_FILE = "data/ner_training_data.json"

def prepare_ner_data():
    """Prepare training data for Named Entity Recognition (NER) ensuring full copyright phrases are captured."""
    with open(TRAINING_DATA_FILE, "r", encoding="utf-8") as f:
        copyright_texts = json.load(f)

    ner_training_data = []

    for text in copyright_texts:
        # Improved regex to extract full copyright statements
        matches = re.finditer(r"(Copyright(?:\s©)?\s\d{4}[^.!?\n]*)", text)

        entities = [(m.start(), m.end(), "COPYRIGHT") for m in matches]

        if entities:
            ner_training_data.append((text, {"entities": entities}))

    # Save to file
    with open(NER_TRAIN_FILE, "w", encoding="utf-8") as f:
        json.dump(ner_training_data, f, indent=4)

    print(f"✅ NER data prepared and saved to {NER_TRAIN_FILE}")

if __name__ == "__main__":
    prepare_ner_data()
