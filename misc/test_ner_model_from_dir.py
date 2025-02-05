import os
import glob
import spacy

# Function to read text from any file format
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# Function to test the model on all files in a directory
def load_and_test_model(directory):
    # Load the trained model
    nlp = spacy.load("ner_copyright_model")  # Load your trained model

    # Traverse the directory to get all files
    all_files = glob.glob(os.path.join(directory, "**"), recursive=True)
    
    for file_path in all_files:
        # Check if the file is a regular file (skip directories)
        if os.path.isfile(file_path):
            print(f"Processing file: {file_path}")
            # Read file content
            text = read_file(file_path)

            if text:
                # Pass the text through the model to detect copyrights
                doc = nlp(text)

                print(f"\n✅ Detected entities in {file_path}:")
                for ent in doc.ents:
                    if ent.label_ == "COPYRIGHT":
                        print(f"{ent.text} ({ent.label_})")

# Example Usage: Pass the directory where you want to test the model
directory_to_test = "lib/material-android-1.7.6-sources.jar-extract"  # Replace with your directory path
load_and_test_model(directory_to_test)
