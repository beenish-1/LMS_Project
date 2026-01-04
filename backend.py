import json
DATA_FILE = "users.json"
def load_data():
    try:
        with open(DATA_FILE,"r") as f:
            return json.load(f)
    except:
        return {"users":[]}
def save_data(data):
    with open(DATA_FILE,"w") as f:
        json.dump(data, f, indent=4)
def create_account(name,email,password):
    data = load_data()
    email = email.lower()
    for u in data.get("users",[]):
        if u.get("email","").lower() == email:
            return False  
    data["users"].append({
        "name": name,
        "email": email,
        "password": password,
        "role": "student"
    })
    save_data(data)
    return True
def login_user(email,password):
    data = load_data()
    email = email.lower()
    for u in data.get("users",[]):
        if u.get("email","").lower() == email and u.get("password","") == password:
            return u
    return None
