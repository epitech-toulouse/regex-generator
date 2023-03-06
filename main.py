import re
import sys

import ghlinguist as ghl
import giig


def main():
    DEBUG = False

    print(sys.argv)

    if len(sys.argv) == 2:
        if sys.argv[1] == '--debug' or sys.argv[1] == '-d':
            DEBUG = True
            print("DEBUG MODE")

    path = ghl.Path("./repo")

    if DEBUG:
        print("Path: " + str(path))

    result = ghl.linguist(path)

    if DEBUG:
        print("Languages stats: " + str(result))

    languages = [language[0] for language in result if float(language[1]) > 5]

    if DEBUG:
        print("Languages retained: " + str(languages))

    gitignore = giig.get_gitignore(languages)

    if DEBUG:
        print("Gitignore raw: " + str(gitignore))

    gitignore = [line.strip() for line in gitignore.splitlines()]

    gitignore = [line for line in gitignore if not line.startswith('#') and line != '']

    gitignore = [line.rstrip('/') for line in gitignore]

    gitignore.append('.vscode')
    gitignore.append('.idea')
    gitignore.append('.vim')

    if DEBUG:
        print("Gitignore formatted: " + str(gitignore))

    regex = "^(?:.+/)?(" + '|'.join([re.escape(line) for line in gitignore]) + ")(?:(?P<ps_d>/).*)?$$"

    print(regex)


if __name__ == '__main__':
    main()
