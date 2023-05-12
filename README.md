# Ansible module to Install Basler Blaze Firmware update

# Setup

```
python3 -m venv venv  # Create a virtualenv if one does not already exist
./venv/bin/pip3 install --upgrade pip # Upgrade pip
./venv/bin/pip3 install -r python-requirements.txt # Install requirements
```

# Usage

1. Download firmware file
2. Specify location of firmware file in vars in `testmod.yml`
3. Run
```
./venv/bin/ansible-playbook testmod.yml
```

If you want to include the module in your ansible playbook
1. Install required python package on the control host from the requirements file
2. Copy `library` folder to your project


# Usage when run on remote host

The module is designed to be run on the Ansible controller, as the module requires `swupdateclient` to be installed on the host.
If you would like to run the firmware update on a host other than the Ansible controller the `swupdateclient` must be installed on the host.
This allows you to update Blaser Blaze cameras that are not directly to the network but directly connected to a host
`swupdateclient` can be installed using the requirements file in this repo.
It is recommended that the dependencies are installed inside a virtual environment on the host so they do not interfere with the host, please see this guide for more details: https://medium.com/@crobin/ansible-module-dependency-management-d2f5235aa75a
