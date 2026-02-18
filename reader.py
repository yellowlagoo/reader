import argparse

parser =  argparse.ArgumentParser()
parser.add_argument("file", help="txt file to parse")
args = parser.parse_args()


def parse_file(filename, keyword):
    f = open(filename, encoding="utf-8")
    
    for line in f:
        if keyword in line:
            print(line, end='')
    f.close()

parse_file(args.file, "apple")