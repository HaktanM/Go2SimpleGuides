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
The password is 123

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
Make sure your host PC has ethernet connection or wireless connection. Check if you can hear from the onboard PC or from extarnal PC of the unitree go2.
```bash
ping 192.168.123.18    # External PC (Jetson Device)
ping 192.168.123.161   # Internal PC 
```
