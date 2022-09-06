# Postbook CTF

Flag0 -- Found
The person with username "user" has a very easy password...
It was password :D

Flag1 -- Found
Try viewing your own post and then see if you can change the ID

Flag2 -- Found
You should definitely use "Inspect Element" on the form when creating a new post
Remember to check for hidden inputs in forms.

Flag3 -- Found
189 \* 5 = the id for a hidden post.

Flag4 -- Found
You can edit your own posts, what about someone else's?

Flag5 -- Found
The cookie allows you to stay signed in. Can you figure out how they work so you can sign in to user with ID 1?
It was an MD5 hash of the user id. Used an online tool to brute force the MD5 hash.

Flag6 -- Found
Deleting a post seems to take an ID that is not a number. Can you figure out what it is?
It was the MD5 hash of the post id.
