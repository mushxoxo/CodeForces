import math

data = input().split()

n = int(data[0])
m = int(data[1])
a = int(data[2])

fs_len = n/a
fs_br = m/a

if fs_len > int(fs_len):
    fs_len = int(fs_len)+1
else:
     fs_len = int(fs_len)

if fs_br > int(fs_br):
     fs_br = int(fs_br)+1
else:
     fs_br = int(fs_br)

num_fs = fs_br * fs_len


print(num_fs)
