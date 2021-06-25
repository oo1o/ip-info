import urllib.request
import json


#Through the tool, you can locate anyone you want in addition to the location coordinates from IP address only.
#من خلال الأداة يمكنك تحديد موقع أي شخص تريد بالإضافة إلى إحداثيات الموقع من عنوان الايبي فقط

print("\t       [•]IP Information[•] ")

print(""" 
		 _   _             _             
		| \ | |           | |            
		|  \| | __ _ _ __ | | ___  _ __  
		| . ` |/ _` | '_ \| |/ _ \| '_ \ 
		| |\  | (_| | |_) | | (_) | | | |
		|_| \_|\__,_| .__/|_|\___/|_| |_|
		            | |                  
		            |_| 
	--------------------------------------
	|       -> By >> Naplon ◕_◕         |
	|       -> Instagram: 3h6h           |
	|       -> Twitter : _naplon         |
	|       -> Telegram: naplon0         | 
	--------------------------------------                                                 

Determine the location of the IP address and all private information
تحديد موقع عنوان IP وجميع المعلومات الخاصة به
""")


while True:
	ipcheck = 0
	print("-" * 40)
	iip = input("Enter ip address: ")
	try:
		url = "https://ipinfo.io/" + iip
		req = urllib.request.Request(url)
		with urllib.request.urlopen(req) as response:
			data = response.read()
			data = json.loads(data)
	except:
		print("Not a valid ip")
		ipcheck = 1

	if ipcheck == 0:
		try:
			print("-" * 40)
			print("Ip address:" , data['ip'])
		except:
			print("Ip address: N/A")
		try:
			print("City:" , data['city'])
		except:
			print("City: N/A")
		try:
			print("State:" , data['region'])
		except:
			print("State: N/A")
		try:
			print("Country:" , data['country'])
		except:
			print("Country: N/A")
		try:
			print("Location:" , data['loc'])
		except:
			print("Location: N/A")
		try:
			print("timezone:" , data['timezone'])
		except:
			print("timezone: N/A")
		try:
			print("phone:" , data['phone'])
		except:
			print("phone: N/A")
		try:
			print("Zip:" , data['postal'])
		except:
			print("Zip: N/A")
		try:
			print("ISP:" , data['org'])
		except:
			print("ISP: N/A")
		try:
			print("network:" , data['network:'])
		except:
			print("network: N/A")
		print("-" * 40)
		
		
