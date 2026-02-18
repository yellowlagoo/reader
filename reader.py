
def parse_file(filename, keyword):
    f = open(filename, encoding="utf-8")
    
    for line in f:
        if keyword in line:
            print(line, end='')
    f.close()

parse_file('test1.txt', 'fox')