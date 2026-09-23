#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXTENSION_DIR="$HOME/.local/share/nautilus-python/extensions"

mkdir -p "$EXTENSION_DIR"

cp "$SCRIPT_DIR/open_zed.py" "$EXTENSION_DIR/open_zed.py"

nautilus -q 2>/dev/null || true

echo "Nautilus Open Zed extension installed."
