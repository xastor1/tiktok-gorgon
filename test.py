from gorgon import gorgon
# Parmes from url split ?
# example :
#https://api16-core-c-useast1a.tiktokv.com/aweme/v1/user/?user_name=iy2j&retry_type=no_retry&iid=0&device_id=0&os_api=18&app_name=musical_ly&channel=app%20store&version_name=14.2.0&device_type=iphone%208&language=en&os_version=14.0&app_version=14.2.0&screen_width=750&aid=1233&ac=wifi&count=20&cursor=0&download_click_id=&openudid=0b1638096e8c6ab638da6c2d6dfaf29a3658b00f&uid=0&timestamp=1601300687&search_id=&click_id=&session_id=62a465b9-6420-4fe5-923c-246375bbbeba
# parmes : user_name=iy2j&retry_type=no_retry&iid=0&device_id=0&os_api=18&app_name=musical_ly&channel=app%20store&version_name=14.2.0&device_type=iphone%208&language=en&os_version=14.0&app_version=14.2.0&screen_width=750&aid=1233&ac=wifi&count=20&cursor=0&download_click_id=&openudid=0b1638096e8c6ab638da6c2d6dfaf29a3658b00f&uid=0&timestamp=1601300687&search_id=&click_id=&session_id=62a465b9-6420-4fe5-923c-246375bbbeba
params = ""
data = ""
cookies = "sessionid="
get = gorgon(params=params,data=data,cookies=cookies).get_value()

print(f"X-Gorgon: {get['X-Gorgon']} X-Khronos: {get['X-Khronos']}")
