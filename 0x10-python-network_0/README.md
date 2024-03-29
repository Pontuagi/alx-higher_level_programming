# 0x10. Python - Network #0

### Learning Objectives

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

### Requirements

- All your scripts will be tested on Ubuntu 20.04 LTS
- All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
- All your files should end with a new line
- All your files must be executable
- The first line of all your bash files should be exactly #!/bin/bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- All curl commands must have the option -s (silent mode)
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all your Python files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
- All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
- All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'


## File:
1. *0-body_size.sh* - a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
>> The size must be displayed in bytes
>> You have to use curl

1. *1-body.sh:* a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
>> Display only body of a 200 status code response
>> You have to use curl

1. *2-delete.sh:* a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
>> You have to use curl

1. *3-methods.sh:* a Bash script that takes in a URL and displays all HTTP methods the server will accept.
>> You have to use curl

1. *4-header.sh:* a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
>> A header variable X-School-User-Id must be sent with the value 98
>> You have to use curl

1. *5-post_params.sh:* a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
>> A variable email must be sent with the value test@gmail.com
>> A variable subject must be sent with the value I will always be here for PLD
>> You have to use curl

1. *6-peak.py, 6-peak.txt:* a function that finds a peak in a list of unsorted integers.
>> Prototype: def find_peak(list_of_integers):
>> You are not allowed to import any module
>> Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
>> 6-peak.py must contain the function
>> 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
>> Note: there may be more than one peak in the list

