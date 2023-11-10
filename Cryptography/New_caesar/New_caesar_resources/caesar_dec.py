import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(enc):
    dec=""
    for c in range(0,len(enc),2):
        binary="{0:04b}".format(ALPHABET.index(enc[c])) + "{0:04b}".format(ALPHABET.index(enc[c+1]))
        dec+= chr(int(binary[:8],2))
    return dec

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

enc = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"

for key in ALPHABET:
    flag=""
    print("key=",key)
    for c in enc:
        flag+= shift(c,key)
    print("Flag =" ,b16_decode(flag))
