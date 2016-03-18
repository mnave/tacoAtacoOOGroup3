class FileUtil():
    """ A Class representing a Taco-a-Taco file."""

    # Line of the header which as information about the period
    INDEXPeriod = 5

    def __init__(self, file_name, numLines=7):
        """Creates a FileUtil object.

        Requires: file_name is a str of the name of a Taco-a-Taco file
        organized as explained in the general specification. numLines
        is the number of lines occupied by the header in the file.
        """

        fileLines = open(file_name, 'r').readlines()
        self._header = fileLines[:numLines]
        self._content = fileLines[numLines:]

    def getContent(self):
        """The content of a FilUtil."""

        return self._content

    def getHeader(self):
        """The header of a FileUtil."""

        return self._header

    def createNewHeader(self, new_period):
        """Creates a new header, with the new period.

        Requires: new_period is a string corresponding to the next period,
        in the format HHHH (see general specifications).
        Ensures:
        a string with the header of the file named file_name,
        but in which the line corresponding to the period is
        substituted for the period in new_period.
        """

        # Changes the new_period format to the one used in the files
        new_period = new_period[0:2] + ":00 - " + new_period[2:4] + ":00"

        header = self.getHeader()

        header[FileUtil.INDEXPeriod] = new_period

        # Turns header into string, each line separated by commas. To understand the
        # use of commas, see outputStatus.writeServicesFile
        header = ','.join(header)

        # Deletes newlines
        return header.replace('\n', '')
