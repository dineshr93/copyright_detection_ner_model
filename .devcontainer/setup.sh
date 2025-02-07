#!/bin/bash

# Define variables
SCAN_CODE_VERSION="v32.3.2"
SCAN_CODE_URL="https://github.com/aboutcode-org/scancode-toolkit/releases/download/$SCAN_CODE_VERSION/scancode-toolkit-${SCAN_CODE_VERSION}_py3.10-linux.tar.gz"
INSTALL_DIR="/home/vscode/.local/bin/scancode-toolkit-${SCAN_CODE_VERSION}"
TEMP_FILE="/tmp/scancode-toolkit.tar.gz"

# Download the tarball
echo "Downloading ScanCode Toolkit..."
curl -L --fail --silent --show-error -o "$TEMP_FILE" "$SCAN_CODE_URL"

# Verify the download
if [ $? -ne 0 ]; then
    echo "Error: Failed to download ScanCode Toolkit."
    exit 1
fi

# Check if the downloaded file is valid
if ! file "$TEMP_FILE" | grep -q "gzip compressed data"; then
    echo "Error: The downloaded file is not a valid .tar.gz archive."
    rm -f "$TEMP_FILE"
    exit 1
fi

# Create installation directory
mkdir -p "$INSTALL_DIR"


# Extract the tarball
echo "Extracting ScanCode Toolkit..."
tar -xzf "$TEMP_FILE" -C "/home/vscode/.local/bin/"

# Ensure we are in the correct directory
cd "$INSTALL_DIR" || exit 1

./configure

# Add ScanCode to PATH
echo "export PATH=\$PATH:$INSTALL_DIR" >> /home/vscode/.bashrc

# Cleanup
rm -f "$TEMP_FILE"

echo "ScanCode Toolkit installed successfully!"

pip install --upgrade pip setuptools wheel && pip cache purge && pip install -r requirements.txt || pip cache purge && pip install -r requirements.txt

# echo "PATH=\"$PATH:$INSTALL_DIR\"" | sudo tee -a /etc/environment
