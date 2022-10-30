# Encrypted Pastebin CTF

Seems like a site that stores your input as a post. The post is encrypted and they claim that the key is never stored in their database.They also claim to encrypt the data with 128-bit AES encryption.

When you make a post you get redirect to a page where you can see the post. See the URL params here:

## flag 0 - found - :expressionless: !

Hints:
What are these encrypted links?
Encodings like base64 often need to be modified for URLs. Thanks, HTTP

The second hint helped a lot because it told me the way the string had been processed. I was convinced that in order to find the first flag I needed to decode the string. So I wrote the python script to decode the param. The output is not legible.

I ended up looking for the answer online only to find you just needed to delete some characters off the param.

**Lesson:** try more things before going down any rabbit holes.

Changing the post resulted in an error which also gave details on how to decode the string:

```
Traceback (most recent call last):
  File "./main.py", line 69, in index
    post = json.loads(decryptLink(postCt).decode('utf8'))
  File "./common.py", line 46, in decryptLink
    data = b64d(data)
  File "./common.py", line 11, in <lambda>
    b64d = lambda x: base64.decodestring(x.replace('~', '=').replace('!', '/').replace('-', '+'))
  File "/usr/local/lib/python2.7/base64.py", line 328, in decodestring
    return binascii.a2b_base64(s)
Error: Incorrect padding
```

## Things learnt

Looked into Hackcat: https://hashcat.net/hashcat/ and learnt that it can be used to try and guess the value of a hash. You can see this page for an example of all types of hashes:https://hashcat.net/wiki/doku.php?id=example_hashes This is super helpful if like me you have no idea what kind of processing has happened to the string value that you have.
