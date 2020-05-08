import sys

def cat():
    f = open("wasteland.txt", mode="rt", encoding="utf-8")
    for line in f:
        # print(line)    - this will add extra \n on output
        sys.stdout.write(line)
    f.close()

if __name__ =='__main__':
    cat()