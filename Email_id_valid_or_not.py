# Email id is valid or not
import re 
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

email = input("Enter a Email_Id: ")

if(re.search(regex,email)): 
    print("Valid Email_id") 	
else: 
    print("Invalid Email_id") 

	 
	 

