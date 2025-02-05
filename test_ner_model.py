import spacy

MODEL_DIR = "model/ner_copyright_model"

def load_and_test_model():
    """Load the trained model and test it on a sample text."""
    nlp = spacy.load(MODEL_DIR)

    test_text = ("This software is Copyright © 2024 ABC Corp. All Rights Reserved. "
                 "and there is another author Copyright 2026 Dinesh Ravi "
                 "and there is one more copyright Copyright 2023 The Android Open Source Project.")

    doc = nlp(test_text)

    print("✅ Detected entities:")
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")

if __name__ == "__main__":
    load_and_test_model()
