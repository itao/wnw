# vi: set ft=ruby :

VAGRANT_API_VERSION = '2'
Vagrant.require_version '>= 1.4.2'
Vagrant.configure(VAGRANT_API_VERSION) do |config|
  config.vm.box = 'goma'
  config.vm.box_url = 'https://s3.amazonaws.com/sesameio-vagrant/goma.box'

  config.ssh.username = 'goma'

  # devserver
  config.vm.network :forwarded_port, guest: 8888, host: 8888

  config.vm.provision :ansible do |ansible|
    ansible.playbook = 'ansible/vagrant.yml'
    ansible.inventory_path = 'ansible/development'
  end

  config.vm.provider :virtualbox do |vb|
    vb.customize ['modifyvm', :id, '--memory', '512']
    vb.customize ['modifyvm', :id, '--natdnshostresolver1', 'off']
    vb.customize ['modifyvm', :id, '--natdnsproxy1', 'off']
  end
end
