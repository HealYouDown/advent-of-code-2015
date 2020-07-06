from hashlib import md5

key = "iwrupvqb"

i = 0
while True:
    md5_hash = md5(f"{key}{i}".encode()).hexdigest()
    if md5_hash.startswith("000000"):
        print(i)
        break
    i += 1
