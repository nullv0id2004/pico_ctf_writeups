# New caesar
## Description
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) **mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj** [new_caesar.py](https://mercury.picoctf.net/static/b82dc751249b75b2509315c59f8200c7/new_caesar.py)
## Type: Cryptography
## Solving
1) Download the python file consisiting the new caesar
2) I tried to understand the code and wrote everything below to my best understanding

```py
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]# alphabet in range a-p
# the function takes the flag and encodes it.
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))# converts ascii of letter to binary in 8 digits
		enc += ALPHABET[int(binary[:4], 2)]# takes first 4 digits of binary then converts it into int and uses it as an index for ALPHABET array and concats ALPHABET[number] to enc
		enc += ALPHABET[int(binary[4:], 2)]# does the same with last 4 binary digits
	return enc
# caesar shifting
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "bacd"
key = "b"
assert all([k in ALPHABET for k in key])# k is in range a-p so there are 16 keys only
assert len(key) == 1 #key is a single character
#encode the flag and shift it with a particular key
b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)

```
3) So I wrote a python to decode the flag from encoded string and wrote my thought process in comments
```py
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(enc):
    dec=""
    for c in range(0,len(enc),2):
        binary="{0:04b}".format(ALPHABET.index(enc[c])) + "{0:04b}".format(ALPHABET.index(enc[c+1])) # i am taking the first letter and finding its index wrt ALPHABET and converting it into 4 digit binary and repeating it for second letter and then concatting it to make 8 digit binary.
        dec+= chr(int(binary[:8],2)) # then I am converting that binary to decimal and converting it into char with corresponding ASCII value and concatting it to dec.
    return dec

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

enc = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"
# I am now brute forcing the key.
# To reverse the encode we first have to shift and then decode.
for key in ALPHABET:
    flag=""
    print("key=",key)
    for c in enc:
        flag+= shift(c,key)
    print("Flag =" ,b16_decode(flag))

```
4) I ran the code and got 16 flags.
![](/Cryptography/New_caesar/New_caesar_resources/Screenshot%20from%202023-11-11%2002-17-15.png)
5) Only one looked plausible and that was **et_tu_a2da1e18af49f649806988786deb2a6c**

**Flag: picoCTF{et_tu?_a2da1e18af49f649806988786deb2a6c}**
