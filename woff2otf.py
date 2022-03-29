# import brotli !

from fontTools.ttLib import woff2
import os
import sys

def convert(infilename, outfilename):
    with open(infilename , mode='rb') as infile:
        with open(outfilename, mode='wb') as outfile:
            woff2.decompress(infile, outfile)

    return 0

def batchconvert(source_dir, target_dir):
    for file in os.listdir(source_dir):
        if file.endswith('.woff2') or file.endswith('.woff'):
            convert(source_dir + '/' + file, target_dir + '/' + file.rsplit('.', 1)[0] + '.otf')
    
    return 0


def main(argv):
    if len(argv) == 1 or len(argv) > 3:
        print("""usage:

    python woff2otf.py [filename.woff/.woff2] [export filename:optional]

or, for batch conversion:

    python woff2otf.py [import directory path] [export directory path:optional]""")
        return

    if argv[1].endswith('.woff') or argv[1].endswith('.woff2'):
        if len(argv) == 3:
            target_file_name = argv[2]
        else:
            target_file_name = argv[1].rsplit('.', 1)[0] + '.otf'
        convert(argv[1], target_file_name)
    else:
        if len(argv) == 3:
            target_dir_name = argv[2]
        else:
            target_dir_name = argv[1] + '_otf'
        if not os.path.exists(target_dir_name):
            os.makedirs(target_dir_name)
        batchconvert(argv[1], target_dir_name)
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
