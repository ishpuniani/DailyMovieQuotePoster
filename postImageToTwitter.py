#To post image to twitter account

from TwitterAPI import TwitterAPI
import ConfigParser

def authenticateCredentials():
    """
    parse credentials from credentials.txt and authenticate with Twitter.
    """
    config = ConfigParser.ConfigParser()
    config.read('credentials.txt')
    consumer_key = config.get('TWITTER-CREDS', 'consumer_key')
    consumer_secret = config.get('TWITTER-CREDS', 'consumer_secret')
    access_token_key = config.get('TWITTER-CREDS', 'access_token_key')
    access_token_secret = config.get('TWITTER-CREDS', 'access_token_secret')

    api = TwitterAPI(consumer_key,
                      consumer_secret,
                      access_token_key,
                      access_token_secret)

    return api

def postImageToTwitter(imagePath):

	api = authenticateCredentials();
	# STEP 1 - upload image
	file = open(imagePath, 'rb')
	data = file.read()
	r = api.request('media/upload', None, {'media': data})
	print('UPLOAD MEDIA SUCCESS' if r.status_code == 200 else 'UPLOAD MEDIA FAILURE')

	# STEP 2 - post tweet with reference to uploaded image
	if r.status_code == 200:
	        media_id = r.json()['media_id']
	        r = api.request('statuses/update', {'status':'Daily Movie Quote!', 'media_ids':media_id})
	        print('UPDATE STATUS SUCCESS' if r.status_code == 200 else 'UPDATE STATUS FAILURE')

#postImageToTwitter()