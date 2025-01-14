import os

run sudo apt update
run sudo apt install openjdk-8-jdk -y
run sudo apt install openjdk-11-jdk -y
run curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
run echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
run sudo apt update
run sudo apt install jenkins -y
