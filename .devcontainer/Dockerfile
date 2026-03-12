FROM python:3.13-slim

LABEL name="mcp-bcra-dev-container" \
      version="0.1.0" \
      maintainer="alejandro-medici"

RUN apt-get update && apt-get install -y \
    wget tar gzip git curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /workspace

CMD ["/bin/bash"]
