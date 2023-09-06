from mypackage import greet, maths
import requests
import webbrowser
urls_list = [
    "http://www.google.com",
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
]

# for url in urls_list:
#     webbrowser.open_new_tab(url)

# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'  # text from a website
# response = requests.get(url)
# print(response)
# print(response.status_code)  # status code, success:200
# print(response.headers)     # headers information
# print(response.text)

maths.add_numbers(1, 2, 3, 5)
maths.multiple(3, 2)
print(greet.greet_person("Twinkle", "Patelk")
      )
