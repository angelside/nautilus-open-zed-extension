# Nautilus Open Zed Extension

A small Nautilus Python extension that adds **Open in Zed** to the right-click menu for directories.

It is designed for Linux systems using GNOME Nautilus and Zed.

> **Note:** The extension currently assumes Zed is installed as `/usr/bin/zeditor`. This may need to be changed for other distributions or installation methods.

## Features

- Right-click a folder → **Open in Zed**
- Right-click empty space → **Open in Zed**
- Files are ignored
- Multiple selections are ignored
- Uses the `zed` executable from your `PATH`
- No shell command execution
- No external Python dependencies

## Behaviour

| Selection | Result |
| --- | --- |
| Empty space | Opens the current directory in Zed |
| One folder | Opens the selected folder in Zed |
| One file | No menu entry |
| Multiple files | No menu entry |
| Multiple folders | No menu entry |

Files are intentionally ignored because Nautilus already provides Zed through its normal file association / **Open With** functionality.

## Requirements

- GNOME Nautilus
- `nautilus-python`
- Zed
- `zed` available in `PATH`

Check that Zed is available:

    which zed

For example:

    /usr/bin/zed

## Installation

Clone the repository:

    git clone https://github.com/angelside/nautilus-open-zed-extension.git

Enter the directory:

    cd nautilus-open-zed-extension

Run:

    ./install.sh

Restart Nautilus:

    nautilus -q

Open Nautilus again and right-click a folder or empty area.

## Quick Install

The extension can also be installed directly with:

    mkdir -p ~/.local/share/nautilus-python/extensions && \
    curl -fsSL https://raw.githubusercontent.com/angelside/nautilus-open-zed-extension/develop/open_zed.py \
      -o ~/.local/share/nautilus-python/extensions/open_zed.py && \
    nautilus -q

## Uninstallation

If installed from a cloned repository:

    ./uninstall.sh

Or remove the extension manually:

    rm ~/.local/share/nautilus-python/extensions/open_zed.py
    nautilus -q

## How It Works

Nautilus loads Python extensions implementing `Nautilus.MenuProvider`.

This extension provides two menu contexts:

- `get_file_items()` for selected items
- `get_background_items()` for empty space inside a directory

When a directory is selected, the extension passes its filesystem path directly to Zed.

For example:

    zed /home/user/projects/my-project

For empty space inside a directory:

    zed /home/user/projects

## License

MIT
