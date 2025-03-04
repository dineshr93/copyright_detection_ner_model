import json
import spacy
from spacy.training.example import Example
import random

NER_TRAIN_FILE = "data/ner_training_data.json"
OUTPUT_MODEL_DIR = "model/ner_copyright_model"

def train_ner_model():
    """Train a Named Entity Recognition (NER) model for copyright detection."""
    
    nlp = spacy.blank("en")  # Start with a blank model to prevent conflicts
    ner = nlp.add_pipe("ner", last=True)

    with open(NER_TRAIN_FILE, "r", encoding="utf-8") as f:
        training_data = json.load(f)

    ner.add_label("COPYRIGHT")

    train_examples = []
    for text, annotations in training_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        train_examples.append(example)

    optimizer = nlp.begin_training()
    for epoch in range(100):  # More epochs for accuracy
        random.shuffle(train_examples)
        losses = {}
        for example in train_examples:
            nlp.update([example], losses=losses, drop=0.15)  # Lower dropout for better memorization

        print(f"Epoch {epoch+1}, Loss: {losses}")

    nlp.to_disk(OUTPUT_MODEL_DIR)
    print(f"✅ NER Model saved to {OUTPUT_MODEL_DIR}")

if __name__ == "__main__":
    train_ner_model()
