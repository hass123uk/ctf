# Hacker 101 CTFs

https://ctf.hacker101.com/ctf

## Introduction

https://www.hacker101.com/playlists/newcomers

### Notes

#### Must have tools

- Burp proxy:

  - Allows you to watch all http(s) traffic and intercept/modify them.

- Firefox:

  - Allows you to set proxy settings in the browser rather then system wide.

### Web security mechanisms

#### Same origin

This is the main way you are protected on the internet. Websites can only read data they generated and can only see the DOM that belongs to them.

One new thing I learned here is that you can modify the DOM of another tab if you have a reference and you have the same origin.

##### Cross origin resource sharing

This allows us to make AJAX calls across domains.

#### Cookie rules

TODO: List the main rules around this.

### Common attacks

#### XSS

Run arbitrary code on a webpage.

If we can inject that code while another user is using the site we can steal their data.

I suppose if we can get some regex or other long running commands to run then it would also cause the site to crash for the other users acting like a DOS attack.

What other damage can this vulnerability cause?

##### Types

- Reflected
  - What you input is played directly back.
- Stored
  - Stored on the server and then retrieved.
- DOM
  - Displayed as part of the dom.

##### Cheat sheet

Try these out to check how well input is being sanitized.

```
"><h1>test</h1>
'+alert(1)+'
"onmouseover="alert(1)
http://"onmouseover="alert(1)
```

#### CSRF

What is stopping another website from using a POST to issue commands on your site. So if a user is logged in and has a cookie stored in the browser, an attacker could POST data to your site and issue commands on their behalf.

#### Auth-z attacks

Consider exploring the site with the highest level user and the replying the same actions as a user with the lowest action.

#### Directory traversal

You can use . & ../ to traverse the directory trees. If a website is reading or writing files to disk they are potentially open to this kind of attack.
If the wrong security setup is in place you could potentially read any file on the computer or write a malicious file to disk.

#### SQL Injection
