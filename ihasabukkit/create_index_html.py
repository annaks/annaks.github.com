import os

header = '<!DOCTYPE html> \
<html lang="en"> \
<meta charset="UTF-8">\
<head> \
    <script type="text/javascript" src="static/js/lazyload.min.js"></script>\
    <title>ihasabukk.it</title> \
    <link href="static/css/bootstrap.css" rel="stylesheet"> \
    <link href="http://fonts.googleapis.com/css?family=PT+Sans" rel="stylesheet" type="text/css"> \
    <link href="http://fonts.googleapis.com/css?family=PT+Mono" rel="stylesheet" type="text/css"> \
</head> \
\
<body> \
<div id="content"> \
\
<div class="science_title"> \
<h1>ihasabukk.it</h1> \
</div> \
\
<div class="images">'

footer = '</div> \
\
<div class="projects"> \
    <p>started january 2013<span class="title"</p> \
</div> \
\
</div> \
</body> \
</html>'

header += '<ul class="bukkits">'
img_html_beg = '<li class="container" data-name="' #name of image
img_html_mid1 = '"> <a class="image" href="' #put bitly here
img_html_mid2 = '"> <img src="blank.gif" data-src="' #image location
img_html_end = '" onload=lzld(this) onerror=lzld(this) /> </a> </li>'

bukkit_dir = 'bukkit/'
img_files = os.listdir(bukkit_dir)

final_html = header
bukkit_dir_host = "http://bukk.it/"

for pic_name in img_files[:100]:
#    img_html = img_html_beg + bukkit_dir + pic_name + img_html_mid + pic_name.split('.')[0] + img_html_end
#    bitly_loc = bukkit_dir + pic_name
    bitly_loc = bukkit_dir_host + pic_name
    img_html = img_html_beg + pic_name.split('.')[0] + img_html_mid1 + bitly_loc + \
                img_html_mid2 + bukkit_dir_host + pic_name + img_html_end
    
    final_html += img_html

final_html += '</ul>'    
final_html += footer

fh = open('index.html','w')
fh.write(final_html)
fh.close()
