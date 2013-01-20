# scrapes ALL images off of bukk.it
# future: compare vs bukkit/ to only upload those that are missing

import urllib2

pics = []
home = 'http://bukk.it'

data = urllib2.urlopen(home)
html = data.read()

for line in html.split('\n'):
    pic_href = line.split('"')
    try:
        if '.' in pic_href[7]:
            pics.append(pic_href[7])
    except:
        pass

for pic_url in pics:
    data = urllib2.urlopen(home +'/'+ pic_url)
    fh = open( 'bukkit/'+ pic_url, 'w')
    fh.write(data.read())

