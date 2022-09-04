# Micro-CMS solution

## Flags:

### Unauthorized edit page

Using forced browsing one of the page showed forbidden instead of not found. Using the /page/edit/6 path opened the page in edit mode.

### Injection

Passing a comma alongside the id in the edit page was injected directly into the DB.

### XSS

#### Stored

When creating a new page using markdown you could use run js using html attributes seeing the script tags were sanitized. e.g. onerror="alert(1)"

#### DOM

The title of a newly created page was printed as is on the home page. So you could inject a script tag in the title when creating/editing a page and visiting the home page would trigger that code.
