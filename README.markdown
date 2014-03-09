# Wandering & wondering (code name Goma, production name TBD)

Have amazing experiences.

### Prerequisites
1. Install [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
2. Install [vagrant](http://www.vagrantup.com/)
3. Install [python 2.7](http://www.python.org/getit/) or use your favourite
   package manager
4. Install [pip](http://www.pip-installer.org/en/latest/installing.html)

### Setup the devbox VM using Vagrant
```sh
# Outside of VM
mkdir -p ~/.ssh/sockets
[sudo] pip install -r requirements/tools.txt
vagrant up
vagrant ssh

# Now we're inside the vm
appserver
```
Then just hit up [http://localhost:8888](http://localhost:8888)

To re-provision (if there's an ansible update) run `vagrant provision`
