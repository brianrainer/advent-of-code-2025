from collections import defaultdict


song = """On the First day of Christmas
My true love sent to me
A Partridge in a Pear Tree.

On the Second day of Christmas
My true love sent to me
Two Turtle Doves, and
A Partridge in a Pear Tree.

On the Third day of Christmas
My true love sent to me
Three French Hens,
Two Turtle Doves, and
A Partridge in a Pear Tree.

On the Fourth day of Christmas
My true love sent to me
Four Calling Birds,
Three French Hens,
Two Turtle Doves, and
A Partridge in a Pear Tree.

On the Fifth day of Christmas
My true love sent to me
Five Gold Rings,
Four Calling Birds,
Three French Hens,
Two Turtle Doves, and
A Partridge in a Pear Tree.

On the Sixth day of Christmas
My true love sent to me
Six Geese-a-Laying,
Five Gold Rings,
Four Calling Birds,
Three French Hens,
Two Turtle Doves, and
A Partridge in a Pear Tree.

On the Seventh day of Christmas
My true love sent to me
Seven Swans-a-Swimming,
Six Geese-a-Laying,
Five Gold Rings,
Four Calling Birds,
Three French Hens,
Two Turtle Doves, and
A Partridge in a Pear Tree.

On the Eighth day of Christmas
My true love sent to me
Eight Maids-a-Milking,
Seven Swans-a-Swimming,
Six Geese-a-Laying,
Five Gold Rings,
Four Calling Birds,
Three French Hens,
Two Turtle Doves, and
A Partridge in a Pear Tree.

On the Ninth day of Christmas
My true love sent to me
Nine Ladies Dancing,
Eight Maids-a-Milking,
Seven Swans-a-Swimming,
Six Geese-a-Laying,
Five Gold Rings,
Four Calling Birds,
Three French Hens,
Two Turtle Doves, and
A Partridge in a Pear Tree.

On the Tenth day of Christmas
My true love sent to me
Ten Lords-a-Leaping,
Nine Ladies Dancing,
Eight Maids-a-Milking,
Seven Swans-a-Swimming,
Six Geese-a-Laying,
Five Gold Rings,
Four Calling Birds,
Three French Hens,
Two Turtle Doves, and
A Partridge in a Pear Tree.

On the Eleventh day of Christmas
My true love sent to me
Eleven Pipers Piping,
Ten Lords-a-Leaping,
Nine Ladies Dancing,
Eight Maids-a-Milking,
Seven Swans-a-Swimming,
Six Geese-a-Laying,
Five Gold Rings,
Four Calling Birds,
Three French Hens,
Two Turtle Doves, and
A Partridge in a Pear Tree.

On the Twelfth day of Christmas
My true love sent to me
Twelve Drummers Drumming,
Eleven Pipers Piping,
Ten Lords-a-Leaping,
Nine Ladies Dancing,
Eight Maids-a-Milking,
Seven Swans-a-Swimming,
Six Geese-a-Laying,
Five Gold Rings,
Four Calling Birds,
Three French Hens,
Two Turtle Doves, and
A Partridge in a Pear Tree."""

paragraphs = song.split("\n")
# print(paragraphs)

word_count = 0
compressed_dict = defaultdict(int)
for sentence in paragraphs:
    words = sentence.split(" ")
    word_count += len(words)
    for word in words:
        compressed_dict[word] += 1
# print(word_count)
# print(len(compressed_dict))

sorted_list_count = sorted(compressed_dict.items(), key=lambda x: (-x[1], -len(x[0])))
# print(sorted_list_count)
sorted_list = [x[0] for x in sorted_list_count]

char_map = {}
base = "A"
offset = 0
for i in range(len(sorted_list)):
    ch = chr(ord(base) + i - offset)
    char_map[ch] = sorted_list[i]
    if i == 24:
        base = "a"
        offset = i + 1
    elif i == 49:
        base = "0"
        offset = i + 1
# print(char_map)
char_map_literal = "{"
for key, value in char_map.items():
    char_map_literal += "'%s':'%s'," % (key, value)
char_map_literal += "}"
# print(char_map_literal)

word_char_map = {}
for ch, word in char_map.items():
    word_char_map[word] = ch

encrypted_message = ""
for sentence in paragraphs:
    encrypted = ""
    for word in sentence.split(" "):
        encrypted += word_char_map[word]
    encrypted_message += encrypted + ","
# print(len(encrypted_message))
# print(encrypted_message)

decrypted_message = ""
for i in range(len(encrypted_message)):
    ch = encrypted_message[i]
    if ch == ",":
        decrypted_message += "\n"
    else:
        decrypted_message += char_map[ch]
        if encrypted_message[i + 1] != ",":
            decrypted_message += " "
# print(len(decrypted_message), len(song))
assert decrypted_message[:-1] == song


encrypted_message_literal = """"
JH4IKA,LDEFMN,PBOQGC,V,
JH0IKA,LDEFMN,TRSU,PBOQGC,V,
JH5IKA,LDEFMN,XWY,TRSU,PBOQGC,V,
JH1IKA,LDEFMN,cab,XWY,TRSU,PBOQGC,V,
JH6IKA,LDEFMN,efd,cab,XWY,TRSU,PBOQGC,V,
JH7IKA,LDEFMN,hg,efd,cab,XWY,TRSU,PBOQGC,V,
JHxIKA,LDEFMN,ji,hg,efd,cab,XWY,TRSU,PBOQGC,V,
JH2IKA,LDEFMN,lk,ji,hg,efd,cab,XWY,TRSU,PBOQGC,V,
JH8IKA,LDEFMN,onm,lk,ji,hg,efd,cab,XWY,TRSU,PBOQGC,V,
JH9IKA,LDEFMN,qp,onm,lk,ji,hg,efd,cab,XWY,TRSU,PBOQGC,V,
JHvIKA,LDEFMN,str,qp,onm,lk,ji,hg,efd,cab,XWY,TRSU,PBOQGC,V,
JHyIKA,LDEFMN,3wu,str,qp,onm,lk,ji,hg,efd,cab,XWY,TRSU,PBOQGC,
"""

D = "On the"
E = "\n"
H = ",\n"
F = "A Partridge in a Pear Tree." + E
G = "day of Christmas" + E


Z = {
    "0": "day of Christmas%sMy true love sent to me%s" % (E, E),
    "1": "%s%s%s" % (F, E, D),
    "2": "Two Turtle Doves, and" + E,
    "3": "Three French Hens" + H,
    "4": "Four Calling Birds" + H,
    "5": "Five Gold Rings" + H,
    "6": "Six Geese-a-Laying" + H,
    "7": "Seven Swans-a-Swimming" + H,
    "8": "Eight Maids-a-Milking" + H,
    "9": "Nine Ladies Dancing" + H,
    "A": "Ten Lords-a-Leaping" + H,
    "B": "Eleven Pipers Piping" + H,
    "C": "Twelve Drummers Drumming" + H,
    "D": D,
    "E": E,
    "F": F,
    "a": " First ",
    "b": " Second ",
    "c": " Third ",
    "d": " Fourth ",
    "e": " Fifth ",
    "f": " Sixth ",
    "g": " Seventh ",
    "h": " Eighth ",
    "i": " Ninth ",
    "j": " Tenth ",
    "k": " Eleventh ",
    "l": " Twelfth ",
}
nxt_char_map = Z


nxt_encrypt_message = ""
# nxt_encrypt_message += "Da01b021c0321"  # pattern continues

nxt_encrypt_message += "D"
for i in range(12):
    ch = chr(ord("a") + i)
    nxt_encrypt_message += ch + "0"
    for j in range(i + 1, 0, -1):
        if i == 11 and j == 1:
            continue
        nxt_encrypt_message += str(j) if j <= 9 else chr(ord("A") + j - 10)
nxt_encrypt_message += "F"
# print(nxt_encrypt_message)

nxt_decrypt_message = ""
for ch in nxt_encrypt_message:
    if ch == ",":
        nxt_decrypt_message += " "
    else:
        nxt_decrypt_message += nxt_char_map[ch]
# print(len(nxt_decrypt_message), len(song))

for i in range(len(nxt_decrypt_message) - 1):
    if nxt_decrypt_message[i] != song[i]:
        print(i, nxt_decrypt_message[i])
# print(nxt_decrypt_message)
assert nxt_decrypt_message[:-1] == song
# print(nxt_decrypt_message)


Y = "Da01b021c0321d04321e054321f0654321g07654321h087654321i0987654321j0A987654321k0BA987654321l0CBA98765432F"
M = "".join([Z[y] for y in Y])

Z_literal = "Z={"
for key, val in Z.items():
    if key >= "a":
        Z_literal += '"%s":"%s"' % (key, val)
        if key != "l":
            Z_literal += ","
        continue
    if "D" <= key <= "F":
        Z_literal += '"%s":%s,' % (key, key)
        continue
    if ("3" <= key <= "9") or ("A" <= key <= "C"):
        Z_literal += '"%s":"%s"+H,' % (key, val[:-2])
        continue
    if key == "2":
        Z_literal += '"%s":"%s"+E,' % (key, val[:-1])
    if key == "0":
        Z_literal += (
            '"0":"day of Christmas%' + "sMy true love sent to me%" + 's"%(E,E),'
        )
    if key == "1":
        Z_literal += '"1":"%' + "s%" + "s%" + 's"%' + "(F,E,D),"
Z_literal += "}"
# print(Z_literal)


def final_compression():
    # https://code.golf/12-days-of-christmas#python
    # 814 bytes, 814 chars
    return """D,E,H="On the","\n",",\n"
F,G,Y="A Partridge in a Pear Tree."+E,"day of Christmas"+E,"Da01b021c0321d04321e054321f0654321g07654321h087654321i0987654321j0A987654321k0BA987654321l0CBA98765432F"
Z={"0":"day of Christmas%sMy true love sent to me%s"%(E,E),"1":"%s%s%s"%(F,E,D),"2":"Two Turtle Doves, and"+E,"3":"Three French Hens"+H,"4":"Four Calling Birds"+H,"5":"Five Gold Rings"+H,"6":"Six Geese-a-Laying"+H,"7":"Seven Swans-a-Swimming"+H,"8":"Eight Maids-a-Milking"+H,"9":"Nine Ladies Dancing"+H,"A":"Ten Lords-a-Leaping"+H,"B":"Eleven Pipers Piping"+H,"C":"Twelve Drummers Drumming"+H,"D":D,"E":E,"F":F,"a":" First ","b":" Second ","c":" Third ","d":" Fourth ","e":" Fifth ","f":" Sixth ","g":" Seventh ","h":" Eighth ","i":" Ninth ","j":" Tenth ","k":" Eleventh ","l":" Twelfth "}
print("".join([Z[y] for y in Y]))"""
