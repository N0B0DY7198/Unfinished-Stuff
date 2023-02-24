import colorama, time, os, random
from json import loads as js
user=os.getlogin()
auth_key_start=["0x87sduwopjhde", "0xuhiwfe", "0x20wefh", "0xlbkee", "0x24980yrt", "0x2908wefy"]
auth_key_rands=[f"fr{str(random.randint(2984,34569280))}j3e45{str(random.randint(2984,34569280))}67uy{str(random.randint(2984,34569280))}tre", f"ip{str(random.randint(2984,34569280))}457y45t{str(random.randint(2984,34569280))}ger", f"g3e9{str(random.randint(2984,34569280))}45rgu", f"3240{str(random.randint(2984,34569280))}9f7u3", f"0893{str(random.randint(2984,34569280))}r4yugh", "9340uigf", "3wg09uj", f"309{str(random.randint(2984,34569280))}gfhj", f"30jg{str(random.randint(2984,34569280))}4rip", f"{str(random.randint(2984,34569280))}43789{str(random.randint(2984,34569280))}"]
auth_key_mid=[f"-4e{random.choice(auth_key_rands)}r9085thbjqweb-", f"-f3wr-sdf{random.choice(auth_key_rands)}ver-g345h0enfd", f"-0-9w{random.choice(auth_key_rands)}ru3ejfg-fwer", f"-{random.choice(auth_key_rands)}wweroinf-", random.choice(auth_key_rands)+"frwejh"+random.choice(auth_key_rands)]
def auth_key_builder():
    return random.choice(auth_key_start)+random.choice(auth_key_mid)+random.choice(auth_key_start)

def first_run():
    if not os.path.exists(rf"C:\Users\{user}\TKIT"):
        os.mkdir(rf"C:\Users\{user}\TKIT")
        with open(rf"C:\Users\{user}\TKIT\config.json", "w") as f:
            f.write('''{
                "settings":{
                    "Token":"AUTH_TOKEN",
                    "Banned":false,
                    "BanAttempts":0
                }
            }'''.replace("AUTH_TOKEN", auth_key_builder()))
        return True
    else:
        return False
def build_local_config():
    if first_run():
        with open(rf"C:\Users\{user}\TKIT\config.json", "r") as f:
            return js(f.read())
    else:
        with open(rf"C:\Users\{user}\TKIT\config.json", "r") as f:
            return js(f.read())
def dump_glob2local(): 
    open("settings.json", "w").write(open(rf"C:\Users\{user}\TKIT\config.json").read()) 
dump_glob2local()
def login(key, info, user):
    if js(open("settings.json", "r").read())["settings"]["Token"]==js(open(f"C:\\Users\\{user}\\TKIT\\config.json", "r").read())["settings"]["Token"]:
        print(f"[Auth] Matched tokens! | 2/5")
    else:
        print(f"[Auth] Tokens don't match! | 2/5 | 3 attempts left before revoked access")
        exit()
class colors:
    nigred=colorama.Fore.RED
    nigblue=colorama.Fore.BLUE
    nigger=colorama.Fore.RESET

print(f"[NiggerTools] {colors.nigred}Making your account! | 1/5")
login(auth_key_builder(), "tmp", "null")
