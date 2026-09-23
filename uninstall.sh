#!/bin/bash

set -e

EXTENSION="$HOME/.local/share/nautilus-python/extensions/open_zed.py"

if [ -f "$EXTENSION" ]; then
    rm "$EXTENSION"
fi

nautilus -q 2>/dev/null || true

echo "Nautilus Open Zed extension removed."
