# Hacker 101 CTFs

https://ctf.hacker101.com/ctf

This is my notes for them newcomers playlist on hacker101.

https://www.hacker101.com/playlists/newcomers

**Must have tools**

- Burp proxy:
  - Allows you to watch all http(s) traffic and intercept/modify them.
- Firefox:
  - Allows you to set proxy settings in the browser rather then system wide.

## Web In Depth

Notes from the video web in depth. It discussed core web technologies and the security implications to think about for each of these core technologies.

### Cookies

Cookies are key value pairs that are used to store data in the browser across sessions. They are secured based on the domain they are set on and some flags that control the way the cookies behave.

#### Domain Rules

- Cookies added for .example.com can be read by any subdomain of example.com
- Cookies added for a subdomain can only be read in that subdomain and it's subdomains.
- A subdomain can set cookies for its own subdomains and parents but cannot set cookies for it's sibling domains.
  - E.g. test.example.com cannot set cookies for test2.example.com

#### Security settings

- Secure: The cookie will only be accessible to HTTPS pages.
- HTTPOnly: The cookie cannot be read by Javascript.

These flags are indicated by the server using the SET-Cookie header that passes them in the first place.

### HTML

When it comes to security the main vector of attack is how the HTML is parsed.

One problem is when a firewall parses HTML differently then how the browser parses it, which can cause a vector of attack. E.g. `<script/xss src...` may not be seen as a script tag by a bad XSS filter but Firefox HTML parser to treat the slash as whitespace.

Browsers sometimes try to be smart and clean up after authors which can be exploited. e.g.:

- \<script\> tag on its own will be automatically closed.
- a tag missing its closing angle bracket will be auto closed by the next angle bracket.

### Content Sniffing

Content sniffing is when the browser uses heuristics to determine what type of data is it currently receiving e.g. MIME type sniffing to determine the type of file, Encoding sniffing to check is the encoding ASCII or UTF-8 or something else. It then uses the determined type to base how the browser processed that data.

#### MIME Sniffing

This is no longer a real issue on new browsers. But the cause of the issue is that the browser does not only look at the content-type header and for example if the data contained enough HTML it would parse it as HTML. So an image shared with another user with enough HTML in it would get parsed as HTML and can be used for an XSS attack.

#### Encoding Sniffing

If you do not define the encoding of the page the browser will try and determine it for you. This can be used to pass UTF-7 encoded data that will pass web firewalls that are encoding HTML code but it will be parsed by older browsers as valid HTML.

### Same-Origin Policy (SOP)

This is the main way you are protected on the internet. Websites can only read data they generated and can only see the DOM that belongs to them.

One new thing I learned here is that you can modify the DOM of another tab if you have a reference and you have the same origin.

#### Origin Matching

- Protocol must match
- Port number must match
- Domains must be an exact match
  - No using of wildcards and no subdomain walking

#### SOP Loosening

Developers can loosen the grip of SOP by:

- Changing the document.domain
- Posting messages between windows
- By using CORS

All of these methods open up avenues for attack. E.g. Anyone can call postMessage into an IFrame.

#### Cross origin resource sharing

This allows us to make AJAX calls outside of your origin using special headers to signify where the request originates, what custom headers are added, if cookies should be forwarded, etc.

## Common attacks

### XSS

Run arbitrary code on a webpage.

If we can inject that code while another user is using the site we can steal their data.

I suppose if we can get some regex or other long running commands to run then it would also cause the site to crash for the other users acting like a DOS attack.

What other damage can this vulnerability cause?
If an attacker can make you execute any arbitrary code then he has access to all the data stored in that site.

#### Types

- Reflected
  - What you input is played directly back.
  - If detected then it it inherently dependent on CSRF vulnerabilities to be exploited via POSTs.
- Stored
  - Stored on the server and then retrieved.
- DOM
  - Displayed as part of the dom.

#### Recognition

For every input

- Figure out where it goes.
  - Does it get embedded anywhere e.g. a tag attribute or into a string in a script tag.
- Figure out any special handling.
  - e.g. Do URL's get turned into links?
- Figure out how special characters are handled. e.g. '<>:;"
  - If any of these get through with sanitization take a note as that can be a way to attack.

#### Cheat sheet

Try these out to check how well input is being sanitized.

```
"><h1>test</h1>
'+alert(1)+'
"onmouseover="alert(1)
http://"onmouseover="alert(1)
```

### CSRF

What is stopping another website from using a POST to issue commands on your site. So if a user is logged in and has a cookie stored in the browser, an attacker could POST data to your site and issue commands on their behalf.

### Auth-z attacks

Consider exploring the site with the highest level user and the replying the same actions as a user with the lowest action.

### Directory traversal

You can use . & ../ to traverse the directory trees. If a website is reading or writing files to disk they are potentially open to this kind of attack.
If the wrong security setup is in place you could potentially read any file on the computer or write a malicious file to disk.

#### Mitigate

- Direct mitigation
  This is easy to mitigate by not allowing path separators and/or striping ../ or ..\ from paths.
- Indirect mitigation (preferred)
  Do not allow users to control paths ever.

### Command injection

If a website is running shell commands directly based on user input they are vulnerable to command injection.

#### Testing The scenario is that the output looks very similar to the system PING command. So you try:

```
google.com;echo test
```

It silently gives back an empty page.

Backtick \` - allow you to embed a subcommand e.g.

```
$ ping `echo google.com`
results in:
$ ping google.com
```

#### Mitigation

Try and avoid this or at least sanitize the data on entry.

### SQL Injection (SQLi)

Oh. yes little bobby tables:

`Robert');DROP Table Students;--`

#### SQL refresher

```sql
SELECT some, columns, here from some_table
where some > columns and here !=0;
```

```sql
UPDATE some_table set some=1, columns=2, here=3 where id=5;
```

```sql
INSERT INTO some_table SET (some, columns, here=3) values (1,2,3);
```

#### Example

The application inserts user input directly into the SQL query string before dispatching to the DB.

```sql
SELECT age, grade, teacher from students
where (name='Robert'); DROP Table Students;--')
```

#### Mitigate

ORM's negate this attack as long as you do not misuse it. Otherwise parameterized variables can delegate the sanitation to the DB.

#### Detection

The most common SLQi is in the SELECT statements condition.
The simplest way to detect it is using:

```sql
' or 1='1 --This returns all rows
' and 0='1 --This returns no rows
```

#### Exfiltrate If the goal is to get data out of the system:

UNION is a simple way to do so, take this query:

```sql
SELECT foo, bar, baz FROM some_table
where foo='some input'
```

Knowing that we have three columns of data we could do an SQLi payload of:

```sql
SELECT foo, bar, baz FROM some_table
where foo='1'
UNION select of 1,2,3; --';
```

This will return an extra row. We can use this to select data from other tables too.

#### Truly blind SQLi

One way to see if what we are doing is working is by adding a delay to execution.

#### Which DB

Knowing which DB is being used can have an impact on the behavior and types of attacks to perform. There are a couple of tricks to figure out which DB is being used.
