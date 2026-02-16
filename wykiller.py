import os
import time
import shutil
import json

with open('setting.json', 'r') as f:
    settings = json.load(f)

lang_file = settings['lang'] + '.json'
with open(os.path.join('lang', lang_file), 'r', encoding='utf-8') as f:
    lang = json.load(f) 

root_path=settings['root_path']
modpath=os.path.join(root_path,'mods')
modname=''

try:
    os.listdir(modpath)
except FileNotFoundError:
    print(lang["mod_path_error"])
    time.sleep(2)
    exit()

def search_mod():
    for i in os.listdir(modpath):
        if(i.find('@') != -1):
            time.sleep(1.5)
            modname=i
            try:
                os.remove(os.path.join(modpath, modname))
            except:
                print(lang["deleted_failed"] + modname)
            return True
    return False

def copy_mods(source_mods_dir, target_mods_dir):
    for file_name in os.listdir(source_mods_dir):
        source_file = os.path.join(source_mods_dir, file_name)
        if os.path.isfile(source_file):
            target_file = os.path.join(target_mods_dir, file_name)
            try:
                shutil.copy2(source_file, target_file)
                print(lang["copy"] + file_name)
            except Exception:
                print(lang["copy_failed"] + file_name)

def delete_all_files_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
            except Exception:
                print(lang["deleted_failed"] + file_name)

print('------------------------------')
print(lang["welcome_text"][0]+modpath)
print(lang["welcome_text"][1])
print(lang["welcome_text"][2])
print('------------------------------')


print(lang["start_search"])
i=1
while True:
    print(lang["searching"]+'.'*(i%4)+'     ',end='\r')
    i+=1
    if search_mod():
        break
    time.sleep(0.5)

print(lang["mod_deleted"]+modname+'            ')
print('------------------------------\n')

if(settings['copy_mod']==False):
    exit()

print(lang["start_copy"])
print('modx --> '+modpath)
delete_all_files_in_folder(modpath)
if(len(os.listdir('modx'))>settings['mod_limit']):
    print(lang["too_many_mod"])
else: 
    try:
        copy_mods('modx', modpath)
        print(lang["copy_success"])
    except Exception as e:
        print(lang["copy_error"] + str(e))

time.sleep(5)
exit()
