# InstaInfo README

Gather Information about Instagram Profiles

## Usage

```python
# example script showing how to use instainfo

import instainfo

# create instainfo object
insta = instainfo.InstaInfo()

# checking if instagram.com is up
if insta.isUp():
    print("instagram.com is up and running :)")
else:
    print("instagram.com is down :(")

# checking if an username is an existing account
if insta.isValidAccount("google"):
    print("google is an existing user")
else:
    print("user not found")

# requesting info about an user
profileInfo = insta.getInfo("google")

# accessing single attributes
print(profileInfo.full_name)
print(profileInfo.biography)
print(profileInfo.profile_pic_url_hd)

# getting full dictionary with all info
infodict = profileInfo.getFullDict()

# example for printing all the info of an account
for key, value in infodict.items():
    try: # try/except to prevent decoding errors
        print("{}: {}".format(key, value))
    except:
        pass
```
