from hashlib import sha1
import hmac
from conf import ptv_devid, ptv_key

def getUrl(request):
    devId = ptv_devid
    key = bytes(ptv_key,'UTF-8')
    
    request = request + ('&' if ('?' in request) else '?')
    raw = bytes(request+'devid={0}'.format(devId),'UTF-8')
    
    hashed = hmac.new(key, raw, sha1)
    signature = hashed.hexdigest()
    raw = str(raw,'UTF-8')
    return 'http://timetableapi.ptv.vic.gov.au/'+raw+'&signature={1}'.format(devId, signature),'UTF-8'
    
# request_url = '/v3/routes'
# print(getUrl(request_url))