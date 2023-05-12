# Ansible module to Install Basler Blaze Firmware update

# Setup

```
python3 -m venv venv  # Create a virtualenv if one does not already exist
./venv/bin/pip3 install --upgrade pip # Upgrade pip
./venv/bin/pip3 install -r python-requirements.txt # Install requirements
```

# Usage Standalone
1. Download firmware file
2. Specify location of firmware file in vars in `testmod.yml`
3. Run
```
./venv/bin/ansible-playbook testmod.yml
```

If you want to include the module in your ansible playbook
1. Install required python package on the control host from the requirements file
2. Copy `library` folder to your project
