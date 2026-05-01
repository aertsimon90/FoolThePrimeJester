import requests
import socket
import random
from fake_useragent import UserAgent
import threading
import whois
import time
import dns.resolver
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
import ssl
import json

domain_ip = {}
port_scanning = {}
usings_of_ports = {
  "20": "FTP (File Transfer Protocol) - Used for transferring files between a client and server (data transfer).",
  "21": "FTP (File Transfer Protocol) - Used for control commands and communication between client and server.",
  "22": "SSH (Secure Shell) - Provides a secure channel over an unsecured network for remote login and command execution.",
  "23": "Telnet - A protocol for bidirectional text-oriented communication, typically used for remote terminal access (unencrypted).",
  "25": "SMTP (Simple Mail Transfer Protocol) - Used for sending emails between servers.",
  "53": "DNS (Domain Name System) - Translates domain names into IP addresses.",
  "80": "HTTP (HyperText Transfer Protocol) - The foundation of data communication on the World Wide Web.",
  "110": "POP3 (Post Office Protocol 3) - Used by email clients to retrieve emails from a server.",
  "143": "IMAP (Internet Message Access Protocol) - Used by email clients to access emails on a remote mail server.",
  "443": "HTTPS (HTTP Secure) - A secure version of HTTP that uses SSL/TLS encryption for web traffic.",
  "445": "SMB (Server Message Block) - Used for sharing files, printers, and serial ports between nodes on a network.",
  "465": "SMTPS (SMTP Secure) - SMTP over SSL/TLS for secure email transmission.",
  "587": "SMTP (Mail Submission) - Used for email submission with authentication, often with TLS.",
  "993": "IMAPS (IMAP Secure) - Secure version of IMAP using SSL/TLS encryption.",
  "995": "POP3S (POP3 Secure) - Secure version of POP3 using SSL/TLS encryption.",
  "1433": "Microsoft SQL Server - Default port for Microsoft SQL Server database connections.",
  "1521": "Oracle Database - Default port for Oracle database listener.",
  "1723": "PPTP (Point-to-Point Tunneling Protocol) - Used for VPN connections.",
  "3306": "MySQL - Default port for MySQL database server.",
  "3389": "RDP (Remote Desktop Protocol) - Used by Microsoft’s Remote Desktop services for remote access.",
  "5432": "PostgreSQL - Default port for PostgreSQL database server.",
  "5900": "VNC (Virtual Network Computing) - Used for remote desktop sharing.",
  "8080": "HTTP Alternate - Commonly used as an alternative port for HTTP traffic (e.g., web proxies or testing).",
  "8443": "HTTPS Alternate - Commonly used as an alternative port for HTTPS traffic.",
  "27017": "MongoDB - Default port for MongoDB database server.",
  "49152": "Dynamic/Private Port - Start of the range for dynamic or private ports, often used by applications temporarily.",
  "49153": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49154": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49155": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49156": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49157": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49158": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49159": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49160": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49161": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49162": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49163": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49164": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49165": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49166": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49167": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49168": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49169": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49170": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49171": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49172": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49173": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49174": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system.",
  "49175": "Dynamic/Private Port - Part of the dynamic port range assigned by the operating system."
}
lock = threading.Lock()
bot = requests.Session()
virustotal_api = open("virustotalapi.txt","r").read()

def scan_port(host, port):
	global port_scanning
	if host not in port_scanning:
		with lock:
			port_scanning[host] = []
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.4)
	try:
		s.connect((host, port))
		print(f"Open Port: {host}:{port}")
		with lock:
			port_scanning[host].append(port)
	except:
		pass
	s.close()

def scan_ports(host, ports):
	global port_scanning
	if host not in port_scanning:
		with lock:
			port_scanning[host] = []
	ts = []
	for p in ports:
		t = threading.Thread(target=scan_port, args=(host, p))
		t.start()
		ts.append(t)
		time.sleep(1/1024)
	for t in ts:
		t.join()
		time.sleep(0)
	ports = port_scanning[host]
	with lock:
		del port_scanning[host]
	return ports

def scan_all_ports(host):
	n = 0
	opens = []
	while True:
		maxn = n+1024
		ports = list(range(n, maxn+1))
		print(f"Scanning Ports: {n}-{maxn} for {host}")
		n += 1024
		if n >= 65536:
			break
		opens += scan_ports(host, ports)
	print("Finished Port Scanning. Open Ports:", opens)
	return opens
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

def scan_usings_for_ports(ports):
	global usings_of_ports
	info = []
	for p in ports:
		if str(p) in usings_of_ports:
			info.append(usings_of_ports[str(p)])
	return " ".join(info)

def virustotal_check(host):
	global virustotal_api
	url = f"https://www.virustotal.com/api/v3/ip_addresses/{host}"
	headers = {"x-apikey": virustotal_api}
	try:
		return premius_request("GET", url, headers=headers).json()
	except Exception as e:
		return str(e)

def dns_resolve(host):
	records = {}
	for record_type in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', "CNAME", "PTR", "SRV", "CAA", "DNSKEY", "DS", "HINFO", "RP", "LOC", "PREM", "CERT"]:
		try:
			answers = dns.resolver.resolve(host, record_type)
			records[record_type] = [str(rdata) for rdata in answers]
		except Exception as e:
			records[record_type] = str(e)
	return records
	
def get_ssl_certificate(host):
	try:
		context = ssl.create_default_context()
		with socket.create_connection((host, 443)) as sock:
			with context.wrap_socket(sock, server_hostname=host) as ssock:
				cert = ssock.getpeercert()
		return cert
	except Exception as e:
		return str(e)

def get_methods(host):
	methods = {}
	for method in ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH", "TRACE", "CONNECT", "LINK", "UNLINK", "PURGE", "COPY", "MOVE", "LOCK", "UNLOCK", "PROPFIND", "PROPPATCH", "MKCOL", "REPORT", "CHECKOUT", "CHECKIN", "MKACTIVITY", "MERGE", "NOTIFY", "SUBSCRIBE", "UNSUBSCRIBE", "SEARCH", "BIND", "REBIND", "UNBIND", "ACL", "BASELINE-CONTROL", "VERSION-CONTROL", "DEL", "LIST", "MKWORKSPACE", "ORDERPATCH", "LABEL", "UPDATE", "TRACE-LEGACY", "SYNC", "CHUNK", "TEACH", "DESCRIBE", "DIFF", "ANNOUNCE", "M-SEARCH", "AVAIL", "PING"]:
		print("Scanning:", method)
		methods[method] = {}
		try:
			c = premius_request(method, "http://"+host)
			methods[method]["http"] = {"headers": c.headers, "content": c.content, "status": c.status_code}
		except Exception as e:
			methods[method]["http"] = str(e)
		try:
			c = premius_request(method, "https://"+host)
			methods[method]["https"] = {"headers": c.headers, "content": c.content, "status": c.status_code}
		except Exception as e:
			methods[method]["https"] = str(e)
	return methods

def get_dnsdumpster(host):
	try:
		res = DNSDumpsterAPI().search(host)
		return res
	except Exception as e:
		return str(e)

def host_lookup(host):
	global domain_ip
	if host not in domain_ip:
		try:
			ip = socket.gethostbyname(host)
		except:
			ip = host
		with lock:
			domain_ip[host] = ip
	else:
		ip = domain_ip[host]
	if ip == host:
		hosts = [host]
	else:
		hosts = [host, ip]
	lookup_data = {"started_time": time.time(), "hosts": {}}
	for host in hosts:
		data = {"started_time": time.time()}
		try:
			host2 = socket.gethostbyaddr(host)
		except Exception as e:
			host2 = str(e)
		data["host"] = host
		data["hostname_alias_ips"] = host2
		print(f"Loading Internet Address Informations For: "+host)
		results = {}
		locations = []
		orgs = []
		url = f"https://ipapi.co/{host}/json"
		try:
			info = premius_request("GET", url).json()
			locations.append([info["latitude"], info["longitude"]])
			orgs.append(info["org"])
		except Exception as e:
			info = str(e)
		results[url] = info
		url = f"https://ipinfo.io/{host}/json"
		try:
			info = premius_request("GET", url).json()
			loc = info["loc"].split(",")
			locations.append([float(loc[0]), float(loc[1])])
			orgs.append(info["org"])
		except Exception as e:
			info = str(e)
		results[url] = info
		url = f"http://ip-api.com/json/{host}?fields=66846719"
		try:
			info = premius_request("GET", url).json()
			orgs.append(info["org"])
			orgs.append(info["isp"])
			locations.append([info["lat"], info["lon"]])
		except Exception as e:
			info = str(e)
		results[url] = info
		url = f"http://ipwho.is/{host}?fields=ip,success,message,type,continent,continent_code,country,country_code,region,region_code,city,latitude,longitude,is_eu,postal,calling_code,capital,borders,flag.img,flag.emoji,flag.emoji_unicode,connection.asn,connection.org,connection.isp,connection.domain,timezone.id,timezone.abbr,timezone.is_dst,timezone.offset,timezone.utc,timezone.current_time,currency.name,currency.code,currency.symbol,currency.plural,currency.exchange_rate,security.anonymous,security.proxy,security.vpn,security.tor,security.hosting"
		try:
			info = premius_request("GET", url).json()
			orgs.append(info["connection"]["isp"])
			orgs.append(info["connection"]["org"])
			locations.append([info["latitude"], info["longitude"]])
		except Exception as e:
			info = str(e)
		results[url] = info
		url = f"https://ip.zxq.co/{host}"
		try:
			info = premius_request("GET", url).json()
			loc = info["loc"].split(",")
			locations.append([float(loc[0]), float(loc[1])])
		except Exception as e:
			info = str(e)
		results[url] = info
		url = f"https://api.ipbase.com/v1/json/{host}"
		try:
			info = premius_request("GET", url).json()
			locations.append([info["latitude"], info["longitude"]])
		except Exception as e:
			info = str(e)
		results[url] = info
		print("Loading WHOIS For: "+host)
		try:
			results["whois"] = dict(whois.whois(host))
		except Exception as e:
			results["whois"] = str(e)
		data["results"] = results
		print("Creating Locations...")
		r1 = None
		r2 = None
		r3 = None
		r4 = None
		newlocations = []
		for lat, lon in locations:
			if r1 == None:
				r1 = lat
			if r2 == None:
				r2 = lon
			r1 = (lat+r1)/2
			r2 = (lon+r2)/2
			newlocations.append([lat, lon])
			lat = float(str(lat)+"50000000000000000")
			lon = float(str(lon)+"50000000000000000")
			if r3 == None:
				r3 = lat
			if r4 == None:
				r4 = lon
			r3 = (lat+r3)/2
			r4 = (lon+r4)/2
			newlocations.append([lat, lon])
		if r1 == None:
			r1 = 0
		if r2 == None:
			r2 = 0
		if r3 == None:
			r3 = 0
		if r4 == None:
			r4 = 0
		locations = newlocations+[[r1, r2], [r3, r4], [(r1+r3)/2, (r2+r4)/2]]
		print("Locations:", locations)
		data["locations"] = locations
		data["orgs"] = orgs
		data["orgs_string"] = " ".join(orgs).strip()
		location_address = []
		location_nominatim = {}
		print("Nominatim Geolocation Loading...")
		for loc in locations:
			lat = loc[0];lon = loc[1]
			url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
			print(url)
			try:
				info = premius_request("GET", url).json()
				if "address" in info:
					addr = info["address"]
					addr = ', '.join([v for k, v in addr.items()])
					print(addr)
					location_address.append(addr)
			except Exception as e:
				info = str(e)
			location_nominatim[url] = info
		data["location_nominatim"] = location_nominatim
		data["location_address"] = location_address
		print("Scanning TCP All Open Ports For:", host)
		open_ports = scan_all_ports(host)
		print("Loading Open Ports to Using Information...")
		data["open_ports"] = open_ports
		usings = scan_usings_for_ports(open_ports)
		print(f"Usings of Ports:", usings)
		data["usings_of_open_ports"] = usings
		print("Loading VirusTotal...")
		data["virustotal"] = virustotal_check(host)
		print("Loading DNS Resolve...")
		data["dns_resolve"] = dns_resolve(host)
		print("Loading SSL Certificate...")
		data["ssl_certificate"] = get_ssl_certificate(host)
		print("Loading HTTP Methods and Responses...")
		data["http_methods_to_response"] = get_methods(host)
		print("Loading DNS Dumpster...")
		data["dnsdumpster"] = get_dnsdumpster(host)
		data["end_time"] = time.time()
		lookup_data["hosts"][host] = data
	lookup_data["end_time"] = time.time()
	return lookup_data

def duckduckgo_search(query):
	url = f"https://api.duckduckgo.com/"
	params = {"q": query, "format": "json", "no_html": 1}
	try:
		response = premius_request("GET", url, params=params)
		response.raise_for_status()
		data = response.json()
		if "Abstract" in data:
			big = {"title": data.get("Abstract", ""), "source": data.get("AbstractSource", ""), "text": data.get("AbstractText", ""), "url": data.get("AbstractURL", "")}
		else:
			big = {"title": "", "source": "", "text": "", "url": ""}
		results = []
		if "RelatedTopics" in data:
			for h in data["RelatedTopics"]:
				if "FirstURL" in h:
					url = h["FirstURL"]
					text = h["Text"]
					title = text[:text.find(" - ")][:32]
					source = url[url.find("://")+3:]
					source = source[:source.find("/")].replace("-", " ").replace("_", " ").replace(".", " ").strip().upper()
					results.append({"title": title, "source": source, "text": text, "url": url})
		return {"top": big, "results": results}
	except Exception as e:
		return str(e)

import json
import os
from datetime import datetime
from colorama import init, Fore, Style
import cmd
import re

# Initialize colorama for colored CLI output
init()

def print_banner():
    banner = f"""
{Fore.CYAN}============================================================
        PremiusTool v1.0
        Advanced Reconnaissance and Identity Profiling Utility
        Created by aertsimon90
============================================================{Style.RESET_ALL}
    """
    print(banner)

def validate_domain(domain):
    """Validate domain or IP address format."""
    domain_regex = r'^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    ip_regex = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(domain_regex, domain) or re.match(ip_regex, domain)

def save_to_file(data, output_dir, filename_prefix):
    """Save data to a JSON file with a timestamped filename."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/{filename_prefix}_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"{Fore.GREEN}[+] Saved to {filename}{Style.RESET_ALL}")
    return filename

def load_from_file(filename):
    """Load JSON data from a file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"{Fore.RED}[-] Error loading file {filename}: {str(e)}{Style.RESET_ALL}")
        return None

def display_results(data, verbose=False):
    """Display scan results in a formatted, colorful way."""
    for host, info in data["hosts"].items():
        print(f"\n{Fore.YELLOW}[*] Host: {host}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  Started: {datetime.fromtimestamp(info['started_time']).strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  Ended: {datetime.fromtimestamp(info['end_time']).strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
        
        print(f"\n{Fore.BLUE}[+] Hostname/Alias IPs: {info['hostname_alias_ips']}{Style.RESET_ALL}")
        print(f"\n{Fore.BLUE}[+] Geolocation Data{Style.RESET_ALL}")
        for loc, addr in zip(info['locations'], info['location_address']):
            print(f"  - Lat: {loc[0]}, Lon: {loc[1]} -> {addr}")
        
        print(f"\n{Fore.BLUE}[+] Organizations: {info['orgs_string']}{Style.RESET_ALL}")
        print(f"\n{Fore.BLUE}[+] Open Ports: {info['open_ports']}{Style.RESET_ALL}")
        if info['usings_of_open_ports']:
            print(f"  Uses: {info['usings_of_open_ports']}")
        
        print(f"\n{Fore.BLUE}[+] VirusTotal Check{Style.RESET_ALL}")
        if isinstance(info['virustotal'], dict):
            vt_data = info['virustotal'].get('data', {})
            if vt_data.get('attributes'):
                last_analysis = vt_data['attributes'].get('last_analysis_stats', {})
                print(f"  Malicious: {last_analysis.get('malicious', 0)}")
                print(f"  Suspicious: {last_analysis.get('suspicious', 0)}")
                print(f"  Harmless: {last_analysis.get('harmless', 0)}")
        else:
            print(f"  {info['virustotal']}")
        
        print(f"\n{Fore.BLUE}[+] DNS Records{Style.RESET_ALL}")
        for record_type, records in info['dns_resolve'].items():
            print(f"  {record_type}: {records}")
        
        print(f"\n{Fore.BLUE}[+] SSL Certificate{Style.RESET_ALL}")
        if isinstance(info['ssl_certificate'], dict):
            cert = info['ssl_certificate']
            print(f"  Subject: {cert.get('subject', {}).get('CN', 'N/A')}")
            print(f"  Issuer: {cert.get('issuer', {}).get('CN', 'N/A')}")
            print(f"  Valid From: {cert.get('notBefore', 'N/A')}")
            print(f"  Valid Until: {cert.get('notAfter', 'N/A')}")
        else:
            print(f"  {info['ssl_certificate']}")
        
        if verbose:
            print(f"\n{Fore.BLUE}[+] HTTP Methods{Style.RESET_ALL}")
            for method, protocols in info['http_methods_to_response'].items():
                for proto, resp in protocols.items():
                    if isinstance(resp, dict):
                        print(f"  {method} ({proto}): Status {resp['status']}")
                    else:
                        print(f"  {method} ({proto}): {resp}")
        
        print(f"\n{Fore.BLUE}[+] DNS Dumpster{Style.RESET_ALL}")
        if isinstance(info['dnsdumpster'], dict):
            for key, value in info['dnsdumpster'].items():
                print(f"  {key}: {value}")
        else:
            print(f"  {info['dnsdumpster']}")

class PremiusToolMenu(cmd.Cmd):
    intro = f"{Fore.CYAN}Welcome to PremiusTool Interactive Menu. Type 'help' or '?' for commands.{Style.RESET_ALL}"
    prompt = f"{Fore.GREEN}(PremiusTool)> {Style.RESET_ALL}"

    def __init__(self):
        super().__init__()
        self.output_dir = "output"
        self.verbose = False
        self.profiles = {}  # In-memory storage for profiles
        self.current_profile = None

    def do_scan(self, arg):
        """Perform a full host lookup scan. Usage: scan <target> [verbose]"""
        args = arg.split()
        if not args:
            print(f"{Fore.RED}[-] Target is required. Usage: scan <target> [verbose]{Style.RESET_ALL}")
            return
        target = args[0]
        verbose = args[1].lower() == "true" if len(args) > 1 else self.verbose

        if not validate_domain(target):
            print(f"{Fore.RED}[-] Invalid domain or IP address: {target}{Style.RESET_ALL}")
            return

        print(f"{Fore.YELLOW}[*] Starting scan for {target}{Style.RESET_ALL}")
        try:
            scan_data = host_lookup(target)
            display_results(scan_data, verbose)
            filename = save_to_file(scan_data, self.output_dir, f"scan_{target}")
            if self.current_profile:
                self.profiles[self.current_profile]["scans"].append({"target": target, "file": filename, "data": scan_data})
                print(f"{Fore.GREEN}[+] Scan added to profile '{self.current_profile}'{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] Error during scan: {str(e)}{Style.RESET_ALL}")

    def do_search(self, arg):
        """Perform a DuckDuckGo search. Usage: search <query>"""
        if not arg:
            print(f"{Fore.RED}[-] Query is required. Usage: search <query>{Style.RESET_ALL}")
            return
        query = arg
        print(f"{Fore.YELLOW}[*] Performing DuckDuckGo search for: {query}{Style.RESET_ALL}")
        try:
            search_results = duckduckgo_search(query)
            if isinstance(search_results, dict):
                print(f"\n{Fore.BLUE}[+] Search Results{Style.RESET_ALL}")
                top = search_results.get("top", {})
                print(f"  Top Result: {top.get('title', 'N/A')}")
                print(f"  Source: {top.get('source', 'N/A')}")
                print(f"  Text: {top.get('text', 'N/A')}")
                print(f"  URL: {top.get('url', 'N/A')}")
                for result in search_results.get("results", []):
                    print(f"\n  Title: {result['title']}")
                    print(f"  Source: {result['source']}")
                    print(f"  Text: {result['text']}")
                    print(f"  URL: {result['url']}")
                filename = save_to_file(search_results, self.output_dir, f"search_{query.replace(' ', '_')}")
                if self.current_profile:
                    self.profiles[self.current_profile]["searches"].append({"query": query, "file": filename, "data": search_results})
                    print(f"{Fore.GREEN}[+] Search added to profile '{self.current_profile}'{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[-] Search error: {search_results}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[-] Search error: {str(e)}{Style.RESET_ALL}")

    def do_create_profile(self, arg):
        """Create a new profile. Usage: create_profile <profile_name>"""
        if not arg:
            print(f"{Fore.RED}[-] Profile name is required. Usage: create_profile <profile_name>{Style.RESET_ALL}")
            return
        profile_name = arg
        if profile_name in self.profiles:
            print(f"{Fore.RED}[-] Profile '{profile_name}' already exists{Style.RESET_ALL}")
            return
        self.profiles[profile_name] = {
            "name": profile_name,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "scans": [],
            "searches": [],
            "entities": []
        }
        filename = save_to_file(self.profiles[profile_name], self.output_dir, f"profile_{profile_name}")
        self.profiles[profile_name]["file"] = filename
        print(f"{Fore.GREEN}[+] Profile '{profile_name}' created and saved to {filename}{Style.RESET_ALL}")

    def do_load_profile(self, arg):
        """Load an existing profile. Usage: load_profile <profile_name>"""
        if not arg:
            print(f"{Fore.RED}[-] Profile name is required. Usage: load_profile <profile_name>{Style.RESET_ALL}")
            return
        profile_name = arg
        profile_file = None
        for file in os.listdir(self.output_dir):
            if file.startswith(f"profile_{profile_name}_") and file.endswith(".json"):
                profile_file = os.path.join(self.output_dir, file)
                break
        if not profile_file:
            print(f"{Fore.RED}[-] Profile '{profile_name}' not found{Style.RESET_ALL}")
            return
        profile_data = load_from_file(profile_file)
        if profile_data:
            self.profiles[profile_name] = profile_data
            self.profiles[profile_name]["file"] = profile_file
            self.current_profile = profile_name
            print(f"{Fore.GREEN}[+] Profile '{profile_name}' loaded and set as current{Style.RESET_ALL}")

    def do_set_profile(self, arg):
        """Set the current profile. Usage: set_profile <profile_name>"""
        if not arg:
            print(f"{Fore.RED}[-] Profile name is required. Usage: set_profile <profile_name>{Style.RESET_ALL}")
            return
        profile_name = arg
        if profile_name not in self.profiles:
            print(f"{Fore.RED}[-] Profile '{profile_name}' does not exist. Create or load it first.{Style.RESET_ALL}")
            return
        self.current_profile = profile_name
        print(f"{Fore.GREEN}[+] Current profile set to '{profile_name}'{Style.RESET_ALL}")

    def do_list_profiles(self, arg):
        """List all profiles. Usage: list_profiles"""
        if not self.profiles:
            print(f"{Fore.YELLOW}[*] No profiles available{Style.RESET_ALL}")
            return
        print(f"{Fore.BLUE}[+] Available Profiles:{Style.RESET_ALL}")
        for profile_name, profile in self.profiles.items():
            print(f"  - {profile_name} (Created: {profile['created']}, Scans: {len(profile['scans'])}, Searches: {len(profile['searches'])})")

    def do_view_profile(self, arg):
        """View details of a profile. Usage: view_profile <profile_name>"""
        if not arg:
            print(f"{Fore.RED}[-] Profile name is required. Usage: view_profile <profile_name>{Style.RESET_ALL}")
            return
        profile_name = arg
        if profile_name not in self.profiles:
            print(f"{Fore.RED}[-] Profile '{profile_name}' does not exist{Style.RESET_ALL}")
            return
        profile = self.profiles[profile_name]
        print(f"\n{Fore.YELLOW}[*] Profile: {profile_name}{Style.RESET_ALL}")
        print(f"  Created: {profile['created']}")
        print(f"  File: {profile.get('file', 'N/A')}")
        print(f"  Scans ({len(profile['scans'])}):")
        for scan in profile['scans']:
            print(f"    - Target: {scan['target']}, File: {scan['file']}")
        print(f"  Searches ({len(profile['searches'])}):")
        for search in profile['searches']:
            print(f"    - Query: {search['query']}, File: {search['file']}")
        print(f"  Entities ({len(profile['entities'])}):")
        for entity in profile['entities']:
            print(f"    - Type: {entity['type']}, Value: {entity['value']}")

    def do_add_entity(self, arg):
        """Add a manual entity to the current profile. Usage: add_entity <type> <value>"""
        if not self.current_profile:
            print(f"{Fore.RED}[-] No current profile set. Use set_profile first.{Style.RESET_ALL}")
            return
        args = arg.split(maxsplit=1)
        if len(args) < 2:
            print(f"{Fore.RED}[-] Type and value are required. Usage: add_entity <type> <value>{Style.RESET_ALL}")
            return
        entity_type, value = args
        entity = {"type": entity_type, "value": value, "added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        self.profiles[self.current_profile]["entities"].append(entity)
        save_to_file(self.profiles[self.current_profile], self.output_dir, f"profile_{self.current_profile}")
        print(f"{Fore.GREEN}[+] Entity '{entity_type}: {value}' added to profile '{self.current_profile}'{Style.RESET_ALL}")

    def do_expand_data(self, arg):
        """Expand profile data by scanning entities. Usage: expand_data <profile_name>"""
        if not arg:
            print(f"{Fore.RED}[-] Profile name is required. Usage: expand_data <profile_name>{Style.RESET_ALL}")
            return
        profile_name = arg
        if profile_name not in self.profiles:
            print(f"{Fore.RED}[-] Profile '{profile_name}' does not exist{Style.RESET_ALL}")
            return
        profile = self.profiles[profile_name]
        self.current_profile = profile_name
        for entity in profile["entities"]:
            if entity["type"] in ["domain", "ip"]:
                print(f"{Fore.YELLOW}[*] Scanning entity: {entity['type']} - {entity['value']}{Style.RESET_ALL}")
                try:
                    scan_data = host_lookup(entity["value"])
                    display_results(scan_data, self.verbose)
                    filename = save_to_file(scan_data, self.output_dir, f"scan_{entity['value']}")
                    profile["scans"].append({"target": entity["value"], "file": filename, "data": scan_data})
                except Exception as e:
                    print(f"{Fore.RED}[-] Error scanning {entity['value']}: {str(e)}{Style.RESET_ALL}")
        save_to_file(profile, self.output_dir, f"profile_{profile_name}")
        print(f"{Fore.GREEN}[+] Profile '{profile_name}' updated with new scans{Style.RESET_ALL}")

    def do_find_identity(self, arg):
        """Find closest identity match in a profile. Usage: find_identity <profile_name>"""
        if not arg:
            print(f"{Fore.RED}[-] Profile name is required. Usage: find_identity <profile_name>{Style.RESET_ALL}")
            return
        profile_name = arg
        if profile_name not in self.profiles:
            print(f"{Fore.RED}[-] Profile '{profile_name}' does not exist{Style.RESET_ALL}")
            return
        profile = self.profiles[profile_name]
        print(f"{Fore.YELLOW}[*] Analyzing profile '{profile_name}' for identity correlation{Style.RESET_ALL}")
        
        # Simple correlation logic: combine organizations, locations, and search results
        entities = []
        for scan in profile["scans"]:
            for host, info in scan["data"]["hosts"].items():
                entities.append({
                    "type": "host",
                    "value": host,
                    "orgs": info["orgs"],
                    "locations": info["location_address"],
                    "dns": info["dns_resolve"]
                })
        for search in profile["searches"]:
            if isinstance(search["data"], dict):
                for result in search["data"].get("results", []):
                    entities.append({
                        "type": "search_result",
                        "value": result["text"],
                        "source": result["source"]
                    })

        # Basic identity correlation (example: group by orgs and locations)
        org_count = {}
        loc_count = {}
        for entity in entities:
            if "orgs" in entity:
                for org in entity["orgs"]:
                    org_count[org] = org_count.get(org, 0) + 1
            if "locations" in entity:
                for loc in entity["locations"]:
                    loc_count[loc] = loc_count.get(loc, 0) + 1

        print(f"\n{Fore.BLUE}[+] Identity Correlation Results{Style.RESET_ALL}")
        print("  Top Organizations:")
        for org, count in sorted(org_count.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"    - {org}: {count} occurrences")
        print("  Top Locations:")
        for loc, count in sorted(loc_count.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"    - {loc}: {count} occurrences")
        
        # Suggest identity based on most frequent org/location
        top_org = max(org_count.items(), key=lambda x: x[1], default=("Unknown", 0))[0]
        top_loc = max(loc_count.items(), key=lambda x: x[1], default=("Unknown", 0))[0]
        print(f"\n{Fore.GREEN}[+] Suggested Identity: Associated with '{top_org}' in '{top_loc}'{Style.RESET_ALL}")

    def do_set_output(self, arg):
        """Set the output directory. Usage: set_output <directory>"""
        if not arg:
            print(f"{Fore.RED}[-] Directory is required. Usage: set_output <directory>{Style.RESET_ALL}")
            return
        self.output_dir = arg
        print(f"{Fore.GREEN}[+] Output directory set to: {self.output_dir}{Style.RESET_ALL}")

    def do_set_verbose(self, arg):
        """Set verbose mode. Usage: set_verbose <true/false>"""
        if arg.lower() not in ["true", "false"]:
            print(f"{Fore.RED}[-] Value must be 'true' or 'false'. Usage: set_verbose <true/false>{Style.RESET_ALL}")
            return
        self.verbose = arg.lower() == "true"
        print(f"{Fore.GREEN}[+] Verbose mode set to: {self.verbose}{Style.RESET_ALL}")

    def do_exit(self, arg):
        """Exit the interactive menu."""
        print(f"{Fore.CYAN}[*] Exiting PremiusTool{Style.RESET_ALL}")
        return True

    def do_help(self, arg):
        """Display help for commands."""
        print(f"{Fore.CYAN}Available Commands:{Style.RESET_ALL}")
        print("  scan <target> [verbose] - Perform a full host lookup scan (ports, DNS, SSL, VirusTotal, etc.)")
        print("  search <query> - Perform a DuckDuckGo search")
        print("  create_profile <profile_name> - Create a new profile")
        print("  load_profile <profile_name> - Load an existing profile from file")
        print("  set_profile <profile_name> - Set the current profile for adding data")
        print("  list_profiles - List all loaded profiles")
        print("  view_profile <profile_name> - View details of a profile")
        print("  add_entity <type> <value> - Add a manual entity to the current profile (e.g., domain, ip, email)")
        print("  expand_data <profile_name> - Expand profile by scanning entities")
        print("  find_identity <profile_name> - Find closest identity match in a profile")
        print("  set_output <directory> - Set the output directory for saving results")
        print("  set_verbose <true/false> - Enable or disable verbose output")
        print("  exit - Exit the interactive menu")
        print("  help - Display this help message")

def main():
    print_banner()
    PremiusToolMenu().cmdloop()

if __name__ == "__main__":
    main()
