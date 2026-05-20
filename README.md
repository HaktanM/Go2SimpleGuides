# Go2SimpleGuides
Simple tricks to communicate with Unitree GO2


# Ethernet Connection

## Set wired connection settings
* Go to settings -> Network
* Add new wired connection
* Choose bar, IPv4, set manual. Add a new address using following settings: \
    - Address: 192.168.123.222 
    - Netmask: 255.255.255.0
* Make sure this wired connection is chosen.

## SSH Connection
Connect Expension PC with ethernet cable. Power on. First check if you have a communication channel.
```bash
ping 192.168.123.18
```
If you verify you have connection, you can connect with SSH.
```bash
ssh unitree@192.168.123.18
```

## ROS2
### Installation
First install the docker image.
```bash
sudo docker build -t unitree_go2_humble -f Dockerfile-humble . 
```

Clone Unitree SDK2 and Unitree ROS repos to your host PC. Then modify accoardingly. 