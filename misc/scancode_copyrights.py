import json
import subprocess

# Path to the software package (e.g., a folder containing source code)
SOFTWARE_PACKAGE_PATH = "test_input"

# Output file for storing results
OUTPUT_JSON = "copyright_results.json"

def scan_for_copyrights():
    """Runs ScanCode Toolkit to detect copyrights in a software package."""
    command = [
        "scancode",
        "--copyright",  # Detect copyrights
        "--ignore=*test*",  # ignore test files 
        "--processes=5",  # use 5 processes
        "--json-pp", OUTPUT_JSON,  # Output results in JSON
        SOFTWARE_PACKAGE_PATH
    ]
    
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

if __name__ == "__main__":
    print("Scanning for copyrights...")
    scan_for_copyrights()
    
    print("Parsing results...")
    detected_copyrights = parse_results()

    # Print detected copyright statements
    for entry in detected_copyrights:
        print(f"File: {entry['file']}")
        print(f"Copyright: {entry['statement']}")
        print("-" * 50)

    print(f"Detection complete. Results saved in {OUTPUT_JSON}.")
