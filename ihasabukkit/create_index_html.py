import os
import random

header = '<!DOCTYPE html> \n\
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
<div class="graph_title">\
<ul>\
'
navigation = ''
navigation_folders = ['#','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for letter in navigation_folders:
    letter_nav = '<li class="nav"><a href="'+ letter +'"> '+ letter +' </a></li>'
    if letter == '#':
        letter_nav = '<li class="nav"><a href="num"> '+ letter +' </a></li>'
    navigation += letter_nav
header += navigation

header += '</ul>\
</h2>\
</div>\
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

random.seed()
random_bukkit = [ random.randint(0,len(img_files)-1) for i in range(10)]
for rand in random_bukkit:
    pic_name = img_files[rand]
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

# create html for navigation pages

# bash to create directories: `for i in {}
for letter in navigation_folders:
    if letter == '#':
        letter = 'num'
    os.system('if [ ! -d '+ letter +' ]; then mkdir -p '+ letter +'; fi')

    final_html = header.replace('static','../static')
    final_html = final_html.replace('<li class="nav"><a href="', '<li class="nav"><a href="../')
    # create html for each 
    for pic_name in img_files:
        if letter == 'num' and \
            pic_name[0].isdigit():
            
            bitly_loc = bukkit_dir_host + pic_name
            img_html = img_html_beg + pic_name.split('.')[0] + img_html_mid1 + bitly_loc + \
                        img_html_mid2 + bukkit_dir_host + pic_name + img_html_end

            final_html += img_html

        if pic_name.lower().startswith(letter):

            bitly_loc = bukkit_dir_host + pic_name
            img_html = img_html_beg + pic_name.split('.')[0] + img_html_mid1 + bitly_loc + \
                        img_html_mid2 + bukkit_dir_host + pic_name + img_html_end

            final_html += img_html

    final_html += '</ul>'
    final_html += footer
    
    fh = open( letter +'/index.html','w')
    fh.write(final_html)
    fh.close()    

