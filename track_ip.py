import requests, os, json, time
from time import sleep

os.system("clear")
sleep(1)
print("""
  *   )           )                   (    (  (   
` )  /(  (     ( /((        (  (      )\   )\ )\  
 ( )(_))))\(   )\())\  (    )\))(  ((((_)(((_)(_) 
(_(_())/((_)\ (_))((_) )\ )((_))\   )\ _ )\)_()_) 
|_   _(_))((_)| |_ (_)_(_/( (()(_)  (_)_\(_) || | 
  | | / -_|_-<|  _|| | ' \)) _` |    / _ \ | || | 
  |_| \___/__/ \__||_|_||_|\__, |   /_/ \_\|_||_| 
                           |___/     
	Author : GhannyXploit404
	Github : https://github.com/xxoprt
+------------------------------------------------+
""")
ip = input("IPA : ")
url = requests.get(f"http://ip-api.com/json/{ip}")

if url.status_code == 200:
	ipdate = json.loads(url.text)

	if ipdate["status"] == "success":
		for key in ipdate:
			print(f"{key.capitalize()} : {ipdate[key]}")

			if key == "lon":
				lonte = ipdate["lat"]
				murah = ipdate["lon"]
				maps = f"https://www.google.com/maps/@{lonte},{murah},9z"
				print(f"Maps : {maps}")