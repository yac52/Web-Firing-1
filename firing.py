import requests
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor

# عرض الرسومات الترحيبية
print("""
 ______   ________  ____  _____       _       ______   ________  ________   ______   
|_   _ \ |_   __  ||_   \|_   _|     / \     |_   _ \ |_   __  ||_   __  |.' ____ \  
  | |_) |  | |_ \_|  |   \ | |      / _ \      | |_) |  | |_ \_|  | |_ \_|| (___ \_| 
  |  __'.  |  _| _   | |\ \| |     / ___ \     |  __'.  |  _| _   |  _| _  _.____`.  
 _| |__) |_| |__/ | _| |_\   |_  _/ /   \ \_  _| |__) |_| |__/ | _| |__/ || \____) | 
|_______/|________||_____|\____||____| |____||_______/|________||________| \______.' 
                                                                                     
""")
print("""
      _       ____  ____  ____    ____  ________  ______    
     / \     |_   ||   _||_   \  /   _||_   __  ||_   _ `.  
    / _ \      | |__| |    |   \/   |    | |_ \_|  | | `. \ 
   / ___ \     |  __  |    | |\  /| |    |  _| _   | |  | | 
 _/ /   \ \_  _| |  | |_  _| |_\/_| |_  _| |__/ | _| |_.' / 
|____| |____||____||____||_____||_____||________||______.'  
                                                            
""")
print("""
 ____  ____     _        ______  _____  ____  _____  ________  
|_  _||_  _|   / \     .' ___  ||_   _||_   \|_   _||_   __  | 
  \ \  / /    / _ \   / .'   \_|  | |    |   \ | |    | |_ \_| 
   \ \/ /    / ___ \  | |         | |    | |\ \| |    |  _| _  
   _|  |_  _/ /   \ \_\ `.___.'\ _| |_  _| |_\   |_  _| |__/ | 
  |______||____| |____|`.____ .'|_____||_____|\____||________| 
                                                               
""")
print("""
                                                                                                 
____    __    ____  _______ .______           _______  __  .______       __  .__   __.   _______ 
\   \  /  \  /   / |   ____||   _  \         |   ____||  | |   _  \     |  | |  \ |  |  /  _____|
 \   \/    \/   /  |  |__   |  |_)  |  ______|  |__   |  | |  |_)  |    |  | |   \|  | |  |  __  
  \            /   |   __|  |   _  <  |______|   __|  |  | |      /     |  | |  . `  | |  | |_ | 
   \    /\    /    |  |____ |  |_)  |        |  |     |  | |  |\  \----.|  | |  |\   | |  |__| | 
    \__/  \__/     |_______||______/         |__|     |__| | _| `._____||__| |__| \__|  \______| 
                                                                                                 
""")

# يطلب من المستخدم إدخال الرابط الأساسي
base_url = input("Please enter the base URL (e.g., https://example.com/): ")

# فتح ملف common.txt وقراءة الكلمات
with open("common.txt", "r") as file:
    words = [word.strip() for word in file]

# Function to test each URL
def check_url(word):
    test_url = f"{base_url}{word}"
    try:
        # Send an HTTP GET request to the URL with a timeout
        response = requests.get(test_url, timeout=5)
        
        # Print the result based on response status
        if response.status_code == 200:
            print(colored(f"Valid URL: {test_url}", "green"))
        else:
            print(colored(f"Invalid URL: {test_url}", "red"))
    except requests.exceptions.RequestException:
        # Print invalid if there's an exception (e.g., connection error)
        print(colored(f"Invalid URL: {test_url}", "red"))

# Use ThreadPoolExecutor to send requests concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(check_url, words)
