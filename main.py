from packages import misc, interprete_EBCDIC

path = 'EBCDIC_files' # pathname
filename = 'sample-customer-data' # filename
suffix = 'ebcdic' # format

if __name__ == '__main__':
    file_path = misc.load_rel_path(
        directory=path,
        filename=filename,
        suffix=suffix
    )
    test = interprete_EBCDIC.ReadEBCDIC(
        filepath=file_path
    ).read_file()
    print(test)
