
import sys
import os

# to run this file in command line:
# python apex_install.py apex/install.sql out.sql

install_file_path = sys.argv[1] # apex/install.sql 
output_file_path = sys.argv[2] # out.sql
install_file_parent_directory = "."
sep = os.sep

if sep in install_file_path:
    # "session4/apex/install.sql" -> ["session4", "apex", "install.sql"]
    splited_install_file_path = install_file_path.split(sep)
    install_file_parent_directory = sep.join(splited_install_file_path[0:-1])

# files can be opened directly but they need to be closed later
# install_file = open(install_file_path, "r")
# output_file = open(output_file_path, "w")

with open(install_file_path, "r") as install_file:
    with open(output_file_path, "w") as output_file:
        for line in install_file:
            if line.startswith("@@"):
                file_path = install_file_parent_directory + sep + line.replace("@@", "")
                file_path = file_path.replace("\n", "")
                with open(file_path, "r") as file:
                    output_file.write(file.read())

# install_file.close()
# output_file.close()
