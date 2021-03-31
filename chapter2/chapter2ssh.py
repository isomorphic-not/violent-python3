import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    conn_str = f"ssh {user}@{host}"
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('Unable to connect')
        return
    else:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if ret == 0:
            print('Unable to connect')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    user = 'root'
    host = 'localhost'
    password = 'password'
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')

if __name__ == '__main__':
    main()