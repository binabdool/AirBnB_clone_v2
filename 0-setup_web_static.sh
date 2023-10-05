#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

# install nginx
if ! (nginx -v)
then
    sudo apt-get update -y
    sudo apt-get install -y nginx
fi

# create the desired directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# create an html index page containing the content of the idx_cont variable
idx_cont="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$idx_cont" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# pcreate a symbolic link to current to the test directory
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# change ownership of the /data/ folder to the ubuntu user AND group
sudo chown --recursive ubuntu:ubuntu /data

# configure nginx to serve the index of /data/web_static/current when hbnb_static/ dir is queried
sedStr="\\
\tlocation /hbnb_static {\\
\t\t alias /data/web_static/current/;\\
\t}"
sudo sed -i '/server_name _;/a '"$sedStr"'' /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx restart
