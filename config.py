import random, string, os
"".join([random.choice(string.printable) for _ in os.urandom(24) ] )

SECRET_KEY = "2lzUl{$*D6#`8uXqlU."
ABOUT = "Bienvenue sur la page à propos de Flask !" 
CONTACT = "06 24 67 98 65"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')