# instainfo v0.1 by aaronlyy

import requests

class InstaInfo:
    def __init__(self):
        self.apiUrl = "https://instagram.com/{}/?__a=1"

    def __repr__(self):
        return 'Object: InstaInfo ({})'.format(self.apiUrl)

    def isUp(self):
        '''
        checks if instagram.com is up
        returns (true/false)
        '''
        if requests.get("https://instagram.com").status_code == 200:
            return True
        else:
            return False

    def isValidAccount(self, username):
        '''
        checks if given username is a valid account
        returns true/false
        '''
        if requests.get(self.apiUrl.format(username)).status_code == 200:
            return True
        else:
            return False

    def getInfo(self, username):
        '''
        returns object of ProfileInfoContainer containing the info
        '''
        response = requests.get(self.apiUrl.format(username))
        profileInfo = response.json()["graphql"]["user"]
        return ProfileInfoContainer(profileInfo)


class ProfileInfoContainer:
    '''
    contains info about user
    '''

# attributes of ProfileInfoContainer:
#   .biography
#   .blocked_by_viewer
#   .country_block
#   .external_url
#   .external_url_linkshimmed
#   .edge_followed_by
#   .edge_followed_by["count"] (== follower counter)
#   .followed_by_viewer
#   .edge_follow
#   .edge_follow[count] (== follows counter)
#   .follows_viewer
#   .full_name
#   .has_channel
#   .has_blocked_viewer
#   .highlight_reel_count (== higlight counter)
#   .has_requested_viewer
#   .id
#   .is_business_account
#   .is_joined_recently
#   .business_category_name
#   .is_private
#   .is_verified
#   .edge_mutual_followed_by
#   .edge_mutual_followed_by["count"] (== mutual counter)
#   .profile_pic_url
#   .profile_pic_url_hd
#   .requested_by_viewer
#   .username
#   .connected_fb_page
#   .edge_felix_video_timeline (??)
#   .edge_saved_media (??)
#   .edge_media_collections (??)

    def __init__(self, infodict):
        self.infodict = infodict

    def __getattr__(self, attr):
        if attr in self.infodict:
            return self.infodict[attr]
        else:
            return "n/a"
    
    def getFullDict(self):
        '''
        returns full dictionary
        '''
        return self.infodict