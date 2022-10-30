import json

'''
  * Takes User Info and converts to str and dict json. 
'''


 
login_info= {
    "USER": "TEST",
    "PASS": "TEST",
}

json_string = json.dumps(login_info, indent=3)
with open('config_str.json', 'w') as f:
    f.write(json_string)
    #

json_dict = json.dumps(login_info, indent=3)
with open('config_dict.json', 'w') as fp:
    json.dump(login_info, fp)

  
def read_config_ii():
    #config_loc = os.getcwd() + "/config.json"
    with open("config_str.json", 'r') as f:
        config_data = json.loads(f.read())
    USER, PASS = config_data.get('USER'), config_data.get('PASS')
    return USER, PASS
   
   
read_config_ii()

