# 0x11. Python - Network #1

### 0x11-python-network_1

#### Learning Objectives

- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests #requestsiswaysimplerthanurllib
- How to make HTTP GET request
- How to make HTTP POST/PUT/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service


#### Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly "#!/usr/bin/python3"
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.8._)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using if __name__ == "__main__":)


#### Task Files

**0-hbtn_status.py**

- a Python script that fetches https://alx-intranet.hbtn.io/status
- ---Requirements---
	- You must use the package urllib
	- You are not allowed to import any packages other than urllib
	- The body of the response must be displayed like the following example (tabulation before -)
	- You must use a with statement

**1-hbtn_header.py**

- A Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
- ---Requirements---
	- You must use the packages urllib and sys
	- You are not allow to import packages other than urllib and sys
	- The value of this variable is different for each request
	- You don’t need to check arguments passed to the script (number or type)
	- You must use a with statement

***2-post_email.py***

- A Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
- ---Requirements---
- The email must be sent in the email variable
- You must use the packages urllib and sys
- You are not allowed to import packages other than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement

***3-error_code.py***

- A Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
- ***Requirements***
- You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
- You must use the packages urllib and sys
- You are not allowed to import other packages than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement

***4-hbtn_status.py***

- a Python script that fetches https://alx-intranet.hbtn.io/status
- ***Requirements***
- You must use the package requests
- You are not allow to import packages other than requests
- The body of the response must be display like the following example (tabulation before -)

***5-hbtn_header.py***

- a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
- Requirements
- You must use the packages requests and sys
- You are not allow to import other packages than requests and sys
- The value of this variable is different for each request
- You don’t need to check script arguments (number and type)

***6-post_email.py***

- a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
- ***Requirements***
- The email must be sent in the variable email
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to error check arguments passed to the script (number or type)

***7-error_code.py***

- a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
- ***Requirements***
-If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)

***8-json_api.py***

- a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
- ***Requirements***
- The letter must be sent in the variable q
- If no argument is given, set q=""
- If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
- Otherwise:
	- Display Not a valid JSON if the JSON is invalid
	- Display No result if the JSON is empty
- You must use the package requests and sys
- You are not allowed to import packages other than requests and sys

***10-my_github.py***

- a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
- ***Requirements***

	- You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
	- The first argument will be your username
	- The second argument will be your password (in your case, a personal access token as password)
	- You must use the package requests and sys
	- You are not allowed to import packages other than requests and sys
	- You don’t need to check arguments passed to the script (number or type)



