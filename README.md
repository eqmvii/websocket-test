# Testing Websockets

# See it live!

Only works over http, not https, as of this commit

http://ericwstest.herokuapp.com/

# Procfile note

Note: Procfile may not be needed if a start script is provided inhstead

# Python chunk

pip install websockets

# python actually installed somehow?

python3.7 -m pip install websockets

^ worked 

then run with 

python3.7 python_socket_test.py 
hello, world

!

# python woes

sudo apt install -y python3-pip

trying to get python 3 upgraded to use websockets

let's use deadsnakes

sudo add-apt-repository ppa:deadsnakes/ppa

got

sudo apt-get install python3.7 

to work

then more pip 

sudo -H pip3 install --upgrade pip

accidentally deleted most of the OS

now have multiple python versions

pipenv looks like it makes sense

pipenv run python3.7 python_socket_test.py isn't doing much

pls send help