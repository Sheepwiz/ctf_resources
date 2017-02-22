#    "public": true,
#    "visibility": "full",

import urllib2
i = 200000
while i > 100000:
    try:
        url = "https://hackerone.com/reports/" + str(i) + ".json"
        response = urllib2.urlopen(url)
        html = response.read()
        if "full" in html:
            print i
        i -= 1
    except urllib2.HTTPError, e:
        i -= 1
        continue

