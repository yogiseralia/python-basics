# with EXPR as VAR:
#     BLOCK
#  equilant of concept of try with resources in java 7

def read_series(filename):
    with open(filename,mode='rt',encoding='utf-8') as f:
        return [int(line.strip()) for line in f]
    

