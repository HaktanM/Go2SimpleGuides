# Go2SimpleGuides
Simple tricks to communicate with Unitree GO2


# Ethernet Connection

## Set wired connection settings
* Go to settings -> Network
* Add a new wired connection
* Click IPv4, set manual. Add a new address using following settings:
    - Address: 192.168.123.222 
    - Netmask: 255.255.255.0
* Make sure this wired connection is chosen.

## SSH Connection
Connect Expension PC with ethernet cable. Power on. First check if you have a communication channel.
```bash
ping 192.168.123.18 # External PC (Jetson Device)
```
If you verify you have connection, you can connect with SSH.
```bash
ssh unitree@192.168.123.18 # External PC (Jetson Device)
```
The password is 123

### Internet sharing through Ethernet Cable
If you do not have a USB dongle or wifi router, then the expansion PC (Unitree Device) will not have a different channel to get connected to internet. However, it is possible to share internet through the ethernet cable between your pc and unitree go2 which is the chanel you use for SSH connection.

On the host PC
```bash
ifconfig
# or
ip a
```

Check 
- What channel provides the internet for your host pc.
- What channel is connected to unitree go2.
  
As an example
- wlp129s0 provides internet to my host PC
- enp130s0 is connected to unitree.

Then, we need to tell that we want to share internet from wlp129s0 to enp130s0. On the host PC terminal
```bash
sudo iptables -t nat -A POSTROUTING -o wlp129s0 -j MASQUERADE
sudo iptables -A FORWARD -i enp130s0 -j ACCEPT
```

Now, the host PC shares internet through the ethernet cable. Now, we need to tell expansion PC on unitree that there is internet on the ethernet cable. On the expansion pc terminal, write 
```bash
sudo ip route add default via 192.168.123.222 dev eth0
```
where 192.168.123.222 is the address determined at the beginning of this document.

Then, check the internet connection from the expansion pc terminal.
```bash
ping 8.8.8.8
```

### WIFI with USB Dongle in Expansion PC
First you need to install a driver for the USB dongle. Depending on chip used in the USB, you might need a different dongle. I have used
```bash
cd https://github.com/shenmintao/aic8800d80
```

Then, in the expansion PC terminal, check the visible wifi list
```bash
nmcli device wifi list
# and check if the PC recognizes the USB dongle as a wifi device
nmcli device
```

Connect the expansion PC to one of the visible wifi.
```bash
sudo nmcli device wifi connect "WIFI_NAME" password "WIFI_PASSWORD"
```

### Tailscale for SSH connection through internet
If the expansionc PC is connected to the internet, and if you want to have a SSH connection through internet, I strictly recommend you to use [TAILSCALE](https://tailscale.com/).

## ROS2
### Installation
- First install the docker image.
```bash
sudo docker build -t unitree_go2_humble -f Dockerfile-humble . 
```
- Clone [Unitree SDK](https://github.com/unitreerobotics/unitree_sdk2) and [Unitree ROS2](https://github.com/unitreerobotics/unitree_ros2) repos to your host PC. At that stage, don't install them to your host PC.

- Open [start_go2.bash](https://github.com/HaktanM/Go2SimpleGuides/blob/main/start_go2.bash). Modify Unitree SDK and Unitree Ros paths
```bash
  -v /home/clear/workspace/unitree_ros2_ws:/unitree_ros2_ws \
  -v /home/clear/workspace/unitree_sdk2:/unitree_sdk2 \
```

- Start the docker image
```bash
bash start_go2.bash
```

- First install [Unitree SDK](https://github.com/unitreerobotics/unitree_sdk2), then install [Unitree ROS2])(https://github.com/unitreerobotics/unitree_ros2).

### Usage
Once the docker image is installed, you can start it.
```bash
bash start_go2.bash
```
Make sure your host PC has ethernet connection or wireless connection to Unitree. Check if you can hear from the onboard PC .
```bash
ping 192.168.123.161   # Internal PC on Unitree Go2 
```
Source the unitree ros package.
```bash
source /unitree_ros2/setup.sh
```
You are ready.
```bash
ros2 topic list
ros2 topic echo [topic_name]
ros2 topic echo [topic_name] --field [sub_message_name]
```

# Useful Links
- [GO2 Extended Documents](https://www.docs.quadruped.de/projects/go2/html/index.html)
