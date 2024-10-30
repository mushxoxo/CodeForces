import re

def col_to_num(coord):
    num = 0
    for char in coord:
        num = num*26 + (ord(char)-ord('A')+1)
    return num

def num_to_col(coord):
    result = []
    col_num = int(coord)
    while col_num > 0:
        col_num, rem = divmod(col_num-1, 26)
        result.append(chr(rem + ord('A')))
    return ''.join(result[::-1])

def ln_to_rxcy(cell):
    match = re.match(r"([A-Z]+)(\d+)", cell)
    if match:
        col_str,row_num = match.groups()
        col_num = col_to_num(col_str)
        return f"R{row_num}C{col_num}"
    
def rxcy_to_ln(cell):
    match = re.match(r"R(\d+)C(\d+)", cell)
    if match:
        row_num, col_num = match.groups()
        col_str = num_to_col(col_num)
        return f"{col_str}{row_num}"
    
n = int(input())

for i in range(0,n):
    coord = input()

    if re.match(r"R(\d+)C(\d+)", coord):
        print(rxcy_to_ln(coord))
    else:
        print(ln_to_rxcy(coord))

