import json
import subprocess

# https://stackoverflow.com/a/77673054/2018343
# Path to the software package (e.g., a folder containing source code)
SOFTWARE_PACKAGE_PATH = "input"

# Output file for storing results
OUTPUT_JSON = "data/copyright_results.json"

TRAINING_DATA_FILE = "data/training_data.json"

print("Tip: extractcode --shallow --replace-originals input/your_archive")

def scan_for_copyrights():
    """Runs ScanCode Toolkit to detect copyrights in a software package."""
    command = [
        "scancode",
        "--copyright",  # Detect copyrights
        "--ignore=*test*",  # ignore test files 
        "--processes=9",  # use 9 processes
        "--json-pp", OUTPUT_JSON,  # Output results in JSON
        SOFTWARE_PACKAGE_PATH
    ]

    print(command)
    
    # Execute the ScanCode command
    subprocess.run(command, check=True)

def parse_results():
    """Parses the JSON output to extract relevant copyright data."""
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        results = json.load(f)

    copyrights = []
    for file_data in results.get("files", []):
        if "copyrights" in file_data:
            for entry in file_data["copyrights"]:
                copyrights.append({
                    "file": file_data["path"],
                    "statement": entry["copyright"]
                })
    
    return copyrights

def extract_copyright_statements():
    """Parses ScanCode output and saves copyright statements."""
    with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
        results = json.load(f)

    training_data = []
    for file_data in results.get("files", []):
        if "copyrights" in file_data:
            for entry in file_data["copyrights"]:
                training_data.append(entry["copyright"])

    with open(TRAINING_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(training_data, f, indent=4)

if __name__ == "__main__":
    print("Scanning for copyrights...")
    scan_for_copyrights()
    extract_copyright_statements()
    print(f"Training data saved to {TRAINING_DATA_FILE}")
