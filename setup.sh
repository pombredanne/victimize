#!/bin/bash

# Downloading victims-client.1.0
printf "Downloading victims from github\n"
wget https://github.com/victims/victims-client-java/archive/alpha-0.1.zip
printf "Current directory\n"
echo $(pwd)
# Unzip, rename folder and run maven

printf "Decompress the downloaded file and renaming to victims-client\n"
unzip alpha-0.1.zip	
mv victims-client-java-alpha-0.1 victims-client
rm -rf alpha-0.1.zip
cd victims-client
# Running Maven commands clean package
printf "running mvn clean package -- building Victims-cleint\n"
mvn clean package

printf "Maven Invoation done\n"

sudo cp target/victims-client-1.0-SNAPSHOT-standalone.jar /usr/bin
# Setting the victims alias for future use --- Writing into .bashrc file
#echo "# Redhat Victims" >> ~/.bashrc
#echo "alias victims='java -jar /usr/bin/victims-client-1.0-SNAPSHOT-standalone.jar'" >> ~/.bashrc
# The bashrc script invokation
#source ~/.bashrc

# Change back to previous working directory and delete victims source
cd ..
rm -rf victims-client

printf "Updating database\n"
java -jar /usr/bin/victims-client-1.0-SNAPSHOT-standalone.jar --update
i
printf "installing python requirements\n"
pip install -r requirements.txt

print "Done! Quitting! Bye!\n"
