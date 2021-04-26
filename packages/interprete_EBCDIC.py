class ReadEBCDIC:

    def __init__(self, filepath):
        self.filepath = filepath  # reads filepath

    def read_file(self):
        ebcdic_file = open(self.filepath, "rb")  # opens filepath and reads binary (rb)
        decoded = ebcdic_file.read().decode("cp500")  # file is read and decoded assuming the encoding type is "cp500"

        return decoded  # returns decoded
