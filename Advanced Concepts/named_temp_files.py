from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+', delete=True) as temp_file:
    temp_file.write('SuperSecretAPIKey')
    temp_file.flush()
    print(temp_file.name)
    temp_file.seek(0)
    print(temp_file.read())

'''
ssh_key = settings.SSH_PRIVATE_KEY #load key from environment variable (django settings.py in this case)
        
with NamedTemporaryFile(delete=True) as temp_ssh_key:
    temp_ssh_key.write(ssh_key.encode()) #ssh requires key as a file path!
    temp_ssh_key.flush() #ssh requires key as a file path!
    subprocess.run(['chmod', '600', temp_ssh_key.name]) #ssh requires key as a file path!
    
    ssh_command = [
        'ssh', 'alex@test.org',
        '-i', temp_ssh_key.name, #ssh requires key as a file path!
        '-o', 'StrictHostKeyChecking=no',
        f'cd {settings.ANSIBLE_CWD} && echo "{settings.ANSIBLE_VAULT_PASSWORD}" | ansible-playbook update_dns.yml --vault-password-file /dev/stdin' #do something after logged in with ssh
    ]

    process = subprocess.Popen(
    ssh_command,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
    )
'''