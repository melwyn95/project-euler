import re

common_english = re.compile("[a-zA-Z0-9\.,\"/+()\[\];':]|\s")

f = open("./inputs/_059", "r")

codes = list(map(int, f.read().split(",")))

len_codes = len(codes)
bucket1 = list(map(lambda x: codes[x], range(0, len_codes, 3)))
bucket2 = list(map(lambda x: codes[x], range(1, len_codes, 3)))
bucket3 = list(map(lambda x: codes[x], range(2, len_codes, 3)))

def find_key(bucket):
    key_start = 97
    key_end = 122
    for k in range(key_start, key_end + 1):
        found = True
        for c in bucket:
            if common_english.match(chr(c ^ k)) == None:
                found = False
                break
        if found: 
            return chr(k)

key1 = find_key(bucket1)
key2 = find_key(bucket2)
key3 = find_key(bucket3)

key_final = key1 + key2 + key3 

pwd = key_final * 485
msg = ""
ans = 0
for i in range(len(codes)): 
    msg += chr(ord(pwd[i]) ^ codes[i])
    ans += ord(pwd[i]) ^ codes[i]
print(msg)
print(ans)

