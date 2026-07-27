# What is FastLio Support

This is an up do date docker file to easly test FastLio on Unitree data.

* You can visualize the Lidar Odometry online
* You can replay a recorded bag and test Fast LIO

# How to use it
You need to compile the docker image once.
```bash
cd ../FastLioSupport
bash build_fastlio.bash
```

Modify the ```start_fastlio.bash``` with respect to your computer.

Then, to start the docker image, 
```bash
bash start_fastlio.bash
```
