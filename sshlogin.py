import pexpect

PROMPT = ['#', '>>>' , '>', '\$ ']

def connect(user,host,password):
    ssh_newkey = 'Are you sure you want to connect'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey])
    if ret == 0:
        print("[-] Error connecting")
        return 
    elif ret == 1:
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT, ['Password']])
        if ret == 0:
            print('[-] Error connecting')   
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child
    

def main():
    user = "hackerjedi"
    password = "hackerjedi"
    host = "192.168.64.10"
    child = connect(user,host,password)
    send_command(child, 'cat /etc/shadow | grep root;ps')
    
main()
