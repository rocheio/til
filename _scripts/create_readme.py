"""Create a README table of contents for this repo."""

import os


class ReadmeWriter(object):
    """Creates a README file to and writes it to this repo."""

    def __init__(self):
        """"""
        self.readme = ""
        self.number_posts = 0
        self.repo_path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

    def create_readme(self):
        """Parse this directory and save text for a README file."""

        self._create_intro()

        # Filter repo for only non-private folders
        folders = []
        for item in sorted(os.listdir(self.repo_path)):
            if item.startswith('.') or item.startswith('_'):
                continue

            folderpath = os.path.join(self.repo_path, item)
            if os.path.isdir(folderpath):
                folders += [folderpath]

        self._create_folder_headings(folders)

        for folder in folders:
            self._create_folder_summary(folder)

        self.readme = self.readme.format(posts=self.number_posts)

    def write_readme(self):
        """Write the readme file to the local Git repo."""

        filepath = os.path.join(self.repo_path, 'README.md')
        with open(filepath, 'w') as stream:
            stream.write(self.readme)

    def _create_intro(self):
        """Return the beginning of the README.md file."""

        lines = [
            "# TIL\n\n",
            "> Today I Learned\n\n",
            "A collection of concise write-ups for something that I learn each day.",
            " Credit to [jbranchaud](https://github.com/jbranchaud/til) for the idea.\n",
            "\n**{posts} posts and counting**\n"
        ]
        self.readme += ''.join(lines)

    def _create_folder_headings(self, filepaths):
        """Return a list of all folders with Markdown links."""

        self.readme += "\n---\n"
        self.readme += "\n### Categories\n"

        for filepath in filepaths:
            folder = filepath.split(os.sep)[-1]
            title = folder.title()
            link = '#' + folder
            self.readme += "\n* [{}]({})".format(title, link)

        self.readme += "\n"

    def _create_folder_summary(self, folderpath):
        """Add contents of a folder to the table of contents."""

        folder = folderpath.split(os.sep)[-1]

        self.readme += "\n---\n"
        self.readme += "\n### {}\n".format(folder.title())

        for item in sorted(os.listdir(folderpath)):
            if item.endswith('.md'):
                self.number_posts += 1
                title = _parse_file_title(folder, item)
                link = folder + '/' + item
                self.readme += "\n* [{}]({})".format(title, link)

        self.readme += "\n"


def _parse_file_title(folder, item):
    """Parse the first-line H1 title from a Markdown file."""

    filepath = os.path.join(folder, item)
    with open(filepath, 'r') as stream:
        header = stream.readline()

    if header.startswith('# '):
        header = header[2:]

    header = ' '.join(header.split())
    return header


if __name__ == '__main__':
    WRITER = ReadmeWriter()
    WRITER.create_readme()
    WRITER.write_readme()
