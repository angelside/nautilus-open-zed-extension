import subprocess

from gi.repository import GObject, Nautilus


class OpenZed(GObject.GObject, Nautilus.MenuProvider):

    def open_zed(self, menu, directory):
        try:
            subprocess.Popen(
                [
                    "/usr/bin/zeditor",
                    directory,
                ],
                start_new_session=True,
            )
        except Exception as e:
            print(f"OpenZed: failed to launch Zed: {e}")

    def make_menu_item(self, directory, name):
        item = Nautilus.MenuItem(
            name=name,
            label="Open in Zed",
            tip=f"Open {directory} in Zed",
        )

        item.connect("activate", self.open_zed, directory)

        return item

    def get_file_items(self, files):
        if len(files) != 1:
            return []

        file = files[0]

        if not file.is_directory():
            return []

        directory = file.get_location().get_path()

        if not directory:
            return []

        return [
            self.make_menu_item(
                directory,
                "OpenZed::OpenFolder",
            )
        ]

    def get_background_items(self, current_folder):
        if not current_folder:
            return []

        directory = current_folder.get_location().get_path()

        if not directory:
            return []

        return [
            self.make_menu_item(
                directory,
                "OpenZed::OpenBackground",
            )
        ]
