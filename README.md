# PersonalWebsite
My personal website. It is deployed here: https://robbie-howard.com/

This repo contains git submodules.
After cloning the repo please run the following command (in the repo's root directory) to pull in the submodules:
git submodule update --init --recursive

You will also need to add a secrets.py file to the PersonalWebsite directory with the following variables set:

```
KEY = '????' # django SECRET_KEY
EMAIL = '????' # Email address for sending emails in backend
PASSWORD = '????' # Password for above email
```
