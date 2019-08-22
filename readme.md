## Install

```
redisurl="http://download.redis.io/redis-stable.tar.gz"
curl -s -o redis-stable.tar.gz $redisurl
mkdir -p /usr/local/lib/
tar -C /usr/local/lib/ -xzf redis-stable.tar.gz
rm redis-stable.tar.gz
cd /usr/local/lib/redis-stable/
make && make install
redis-cli --version
sudo mkdir -p /etc/redis/
sudo touch /etc/redis/6379.conf
sudo vim /etc/redis/6379.conf
redis-server /etc/redis/6379.conf
redis-server restart

```

To set the password, edit your redis.conf file, find this line
vim /usr/local/lib/redis-stable/redis.conf

```
requirepass YOURPASSPHRASE
redis-server restart
```

## inlcude redis-py

```
git clone git@github.com:andymccurdy/redis-py.git

or download it
https://github.com/andymccurdy/redis-py.git
```

Install Postgress (http://postgresapp.com). Once you do, add the path to Postgres to your .profile file by appending the following:

```
PATH="/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH"
```

## Instsll psycopg2

```
pip install --upgrade setuptools
pip install pyrebase
pip install psycopg2
```
