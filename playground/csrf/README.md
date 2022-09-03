# Cross Site Request Forgery (CSRF)

This shows that using a csrf attack, if auth is via cookies an attacker can impersonating that user.

## Instructions

### Run app server

```
npm i
node app.js
```

### Set the cookie

Visit localhost:3000 which should set a cookie in your browser.

### Run a static file server

```
python3 -m http.server
```

### Get hacked

Visit localhost:8000/attack.html.

You should see that a post was made to app.js and it contained the cookies.
