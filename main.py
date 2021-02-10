import posixpath
from types import DynamicClassAttribute
from yaml import load as y_load, dump as y_dump
from os.path import isfile, dirname, realpath
from os import kill, system as run
import time

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumperx

selfpath = dirname(realpath(__file__))


def scp(address, port, usernamde, password, local_root, local_path, remote_root, remote_path, ssh_private_key):
    if not ssh_private_key:
        scp_cmd = f"sshpass -p '{password}' scp -P {port} -r {local_root}/{local_path} {username}@{address}:{remote_root}/{remote_path}"
    else:
        scp_cmd = f"sshpass -p '{password}' scp -t {ssh_private_key} -P {port} -r {local_root}/{local_path} {username}@{address}:{remote_root}/{remote_path}"
    run(scp_cmd)


try:
    with open(selfpath + "/settings.yml", "r") as f:
        settings = y_load(f.read(), Loader=Loader)
except:
    print("\033[91m\033[1m" + "No access to `settings.yml` file!" + "\033[0m")
    exit(1)

if "project" in settings and isfile(selfpath + "/projects/" + settings["project"] + ".yml") \
        or isfile(selfpath + "/projects/" + settings["project"]):
    project_file = "projects/" + settings["project"]
    if not project_file.endswith(".yml"):
        project_file += ".yml"
else:
    project_file = "projects/default.yml"

if project_file != "projects/default.yml":
    try:
        with open(selfpath + "/projects/default.yml", "r") as f:
            default_project = y_load(f.read(), Loader=Loader)
    except:
        print("\033[91m\033[1m" +
              "No access to `default` project file!" + "\033[0m")
        exit(1)
    try:
        with open(selfpath + "/" + project_file, "r") as f:
            project = y_load(f.read(), Loader=Loader)
    except:
        print(
            "\033[91m\033[1m" + f"No access to '{project_file.split('/')[-1].split('.')[0]}' project file!" + "\033[0m")
        exit(1)
    default_project.update(project)
    project = default_project
else:
    try:
        with open(selfpath + "/projects/default.yml", "r") as f:
            project = y_load(f.read(), Loader=Loader)
    except:
        print("\033[91m\033[1m" +
              "No access to `default` project file!" + "\033[0m")
        exit(1)

for i in project["paths"]:
    i_split = i.split(" ")
    local_path = i_split[0]
    remote_path = i_split[1]
    scp(project["address"], project["port"], project["user"], project["password"], project["local_root"], local_path,
        project["remote_root"], remote_path, project["ssh_private_key"])
if settings["notify"]:
    run(f"notify-send '{project_file.split('/')[-1].split('.')[0]}'")
