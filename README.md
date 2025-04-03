# timbuktu
 Travel Journal App ![Version](https://img.shields.io/badge/version-1.0.0-blue.svg) (4 April 2025)

## Author details
<pre>
Name:                  Salvatore Reito (Salvo)
Student ID:            1155720
PA username:           ......
PA URL:                https://www.pythonanywhere.com/user/....
GitHub username:       sreitouni
GitHub repository:     https://github.com/sreitouni/timbuktu
Teacher:               lincolnmac
</pre>

## Background
This web app is an 


## System Access
A login system allows users to register, log in, and view pages specific to their user role, providing different levels of access.
There are three user roles in this system:
- **traveller**
- **editor**
- **admin**
<br> Each user has access to a different set of features.

Anyone who registers via the app will be a **traveller**. 
Administrators **admin** can upgrade **traveller** to **editor** or **Admin** roles.

## Getting the Timbuktu App Running

To run the app yourself, you'll need to:

1. Open the project in Visual Studio Code.
2. Create yourself a virtual environment.
3. Install all of the packages listed in requirements.txt
4. Use the [Database Creation .... to create your own.
5. Use the [Database Population Script](.... to populate
   the ***users*** ***journeys*** ***events*** tables with the values provided.
6. Modify [connect.py](timbuktu/connect.py) with the connection details for
   your local database server.
7. Run [The Python/Flask application](run.py). Use Command line python3 run.py or python run.py


Travellers can register for a **traveller** account by creating their own account details. 
Users can also log in using **traveller**, **editor**, or **admin** accounts as listed in the database popuate script 



## Database Scripts
- [MySQL script
- .....

???- [Python script to create password hashes](password_hash_generator.py) ?????

## Passwords
The login system does not store users' passwords in the database.
1. When the user first gives us a password during registration, the system pass it
   through a cryptographic "hash" function: a one-way mathematical operation
   that transforms the original password into its corresponding "hash value"
   or "hash". The same password always results in the same hash.
   
2. The system throws away the original password, and just keep the hashed version.
   ////////////////////////UP TO HERE////////////////////////////
3. The hash value is useless to an attacker: because the hash-function is
   one-way, anyone who steals our database of user accounts can't work out
   what the users' passwords are. Well, okay, there are clever ways around
   that. Look up "rainbow tables" if you're interested. Read Cory Doctorow's
   "Knights of the Rainbow Table" if you're *really* interested. But it takes
   a whole lot more time and computing power for an attacker to get a user's
   password back from its hash than it does to just read the plain password
   straight out of your database.

4. When a user tries to log in, we take the password they supplied us, run it
   through the exact same hash function, and then compare the hash to the one
   we have on file. Because the same password will always produce the same
   hash, if the two hashes match then the passwords must match! Again, kinda.
   It's possible, though very unlikely, that two passwords may produce the
   same hash value. In that case, you'd be able to log in using either
   password. These kinds of "hash collisions" are extremely rare, though. Rare
   enough that we won't worry about that here.

So, in short:
1. The user gives us a password.
2. We put that password though a one-way hashing algorithm to get its "hash".
3. We store the hash, **not** the password.
4. During login, we put the supplied password through the same algorithm.
5. If the hash of the supplied password matches the hash of the user's original
   password that we stored in step 3, then we know the user has supplied the
   correct password... without having to know their password at all.

Cool, huh?

### Salting Passwords

Remember how we mentioned that it's technically possible for an attacker to
work out a user's original password from its hash, just expensive? Well, it's
actually not expensive at all if you just pre-calculate one of those "rainbow
tables": essentially a giant table mapping hash values back to passwords. It
takes time to generate something like that, and the tables are absolutely huge,
but storage is pretty cheap these days and you only have to generate the table
once per hash algorithm. Once someone has a rainbow table for a particular
algorithm, translating hashes back to passwords is just a simple lookup.

The contemporary solution to this is to add a "salt" to each password before
you hash it. The salt is just some random string. It doesn't have to be secret,
necessarily, just specific to your app (which we used to do in older versions
of this example project) or, ideally, specific to each password (which we do in
this current version). Adding a salt to your passwords totally breaks the whole
"rainbow table" approach: an attacker can't just use an off-the-shelf table
any more. With our old approach, one salt for the whole app, an attacker needs
to generate a rainbow table specific to *our application's salt*. When you're
using per-password salts, like we are here, an attacker would have to generate
one of those giant tables to break *each individual password* in our database.

Quantum computing will probably break all this, in the not-too-distant future,
but for now this approach provides a reasonable means of protecting users'
passwords from disclosure if an attacker gains access to our database.

### How exactly do we do all this?

With the [Flask-Bcrypt library](https://flask-bcrypt.readthedocs.io/en/1.0.1/)
(which is really just a Flask-specific wrapper for the bcrypt library) and a
couple lines of code.

If you take a look at the [database creation script](create_database.sql),
you'll see that instead of a "password" field to store the password, we have a
"password_hash" field that stores a binary string of 60 characters.

Flask-Bcrypt uses the [bcrypt algorithm](https://en.wikipedia.org/wiki/Bcrypt)
(as you may have guessed from the name). Bcrypt password hashes bundle together
a bcrypt version number, the password hash itself, and the salt value used to
generate it. Together, depending on which version of the algorithm you're
using, this is a string of either 59 or 60 bytes (always 60 bytes in the
current version).

The string of bytes making up a bcrypt hash are all in the "printable
character" range, so can be displayed a text string. In a MySQL database you
could either store them as a `BINARY(60)` or `CHAR(60) BINARY` column: we use
the latter format in this example because it makes it easier for us to see and
edit the hashes in MySQL Workbench. Technically, because of the way our app
is written, we could use plain old `CHAR(60)`. However, we explicitly use
`CHAR(60) BINARY` because this tells MySQL to treat our string as binary data:
where, for example, "ABC" is meaningfully different to "ABc" or "aBC".

If this sounds terrifyingly complicated, don't worry. Take a look at the
[Hash generator Python script](password_hash_generator.py) for an example of
how to create the hashes (literally one line of code) and check a password
against a hash (again, one line of code).

If we were using the bcrypt library directly, or another option such as
[Flask-Hashing](https://flask-hashing.readthedocs.io/en/latest/) (used in older
versions of this example) then we'd need to handle the "salting" process
ourselves. However, the Flask-Bcrypt library does this for us. We only have to
call the `generate_password_hash(password)` function to generate a hash for a
new `password` (e.g. when a user signs up or changes their password). That
function generates a new salt value then uses it to hash the password in a
single step.

Once we've generated a password hash and stored it in our database, we can then
call the `check_password_hash(pw_hash, password)` function to check a whether a
`password` supplied during login matches the `pw_hash` stored in our database
for that particular user account.

## Documentation
PEP 257 and PEP 8 conventions for writing Docstrings """ """ and Single-Line Comments (#) are followed.
### https://peps.python.org/pep-0257/
### https://peps.python.org/pep-0008/#comments
