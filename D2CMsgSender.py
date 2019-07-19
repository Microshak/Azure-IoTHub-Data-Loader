import base64
import hmac
import hashlib
import time
import requests
import urllib
import urllib.parse


class IoTDataMsgSender:
    
    API_VERSION = '2016-02-03'
    TOKEN_EXPIRES = 100

    def __init__(self, connectionString=None):
        if connectionString != None:
            iotHost, deviceid, deviceKey = [sub[sub.index('=') + 1:] for sub in connectionString.split(";")]
            self.iotHost = iotHost
            self.deviceid = deviceid
            self.deviceKey = deviceKey
            
            
    def sendD2CMsg(self, message, sasToken):
        url = 'https://%s/devices/%s/messages/events?api-version=%s' % (self.iotHost, self.deviceid, self.API_VERSION)
        r = requests.post(url, headers={'Authorization': sasToken}, data=message)
        return r.text, r.status_code
    
    def buildIoTHubSasToken(self):
        TOKEN_FORMAT = 'SharedAccessSignature sig=%s&se=%s&sr=%s'
        resourceUri = '%s/devices/%s' % (self.iotHost, self.deviceid)
        targetUri = resourceUri.lower()
        expiryTime = '%d' % (time.time() + self.TOKEN_EXPIRES)
        toSign = '%s\n%s' % (targetUri, expiryTime)
        key = base64.b64decode(self.deviceKey.encode('utf-8'))
        signature = urllib.parse.quote(
            base64.b64encode(
                hmac.HMAC(key, toSign.encode('utf-8'), hashlib.sha256).digest()
            )
        ).replace('/', '%2F')
        return TOKEN_FORMAT % (signature, expiryTime, targetUri)
    