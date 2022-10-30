import base64


#another encoded string
#p2FKIL0tta25c97Hn8qA7MP3izIdaez2M16EPZLSrU53OED2wb1jlaN5IKiwJdXB1mtElz1Eu9W9XCE7o1UO!fKPot185!yTOxbm0fk5kR9mL1fjU-KrbNskQVCPfzFBPdSm6UBRD-8NjD-!tIwhFNl1I64vbP0JEfPcJ5lDsp1ax7OyXHjzEr69jhk!GCpYEaJqPJRaM09nZghT2XXQAQ~~

encoded = '0nhEkhH5vy5NSPhdcFSiJPNuVf0I9cFEWRTVGm3hpOO9539uaghUkOEBg!MNf2l!AKKmUhZQbuh647SN1w6GscKUWUeKMg40ZG6WffFvrt3IAf!9i!rfrtYCiY5KNWZsDYRoX8S-k5!WZtS1vhUAnIohrApPid8M910j4ZypUO6uHO7fcWsd7aERkHbKxjktq0x01iFZHqbPDN7L58JqPA~~'

# The above value is base64 encoded but a format that is sutitable for web.
# Base64 chars that cause a conflict.
encoded=encoded.replace('-', '+')
encoded=encoded.replace('!', '/')
encoded=encoded.replace('~', '=')
print(encoded)
decoded = base64.b64decode(encoded)
print(decoded)