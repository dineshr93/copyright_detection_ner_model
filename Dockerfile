FROM python:3.10-bullseye

# Define environment variables
# ARG  SCAN_CODE_VERSION="v32.3.2" \
# ARG  INSTALL_DIR="/home/vscode/.local/bin/scancode-toolkit-v32.3.2" \
# ARG  TEMP_FILE="/tmp/scancode-toolkit.tar.gz"
# ARG USERNAME=vscode
# ARG USER_UID=1001
# ARG USER_GID=$USER_UID

# Create the user 
# RUN groupadd --gid $USER_GID $USERNAME \
# 	&& useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
# 	# Add Sudo support
# 	&& apt-get update \
# 	&& apt-get install -y sudo \
# 	&& echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
# 	&& chmod 0440 /etc/sudoers.d/$USERNAME
# Set working directory
WORKDIR /home/vscode

# Install necessary dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    make curl && \
    rm -rf /var/lib/apt/lists/*

# Download and extract ScanCode Toolkit
RUN curl -L --fail --silent --show-error -o "/tmp/scancode-toolkit.tar.gz" "https://github.com/aboutcode-org/scancode-toolkit/releases/download/v32.3.2/scancode-toolkit-v32.3.2_py3.10-linux.tar.gz" \
    && tar -xzf /tmp/scancode-toolkit.tar.gz -C "/home/vscode" \
    && rm -f /tmp/scancode-toolkit.tar.gz

# Set ScanCode Toolkit directory
WORKDIR /home/vscode/scancode-toolkit-v32.3.2

# Configure ScanCode Toolkit
RUN ./configure

# Add ScanCode Toolkit to PATH
ENV PATH="$PATH:/home/vscode/scancode-toolkit-v32.3.2"


WORKDIR /home/vscode/workspace

# Copy requirements.txt from two levels up
COPY ./requirements.txt ./

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip cache purge \
    && pip install -r requirements.txt || (pip cache purge && pip install -r requirements.txt)

# Default command
CMD ["/bin/bash"]
