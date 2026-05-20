xhost +local:docker
sudo docker run -it --privileged --net=host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /home/clear/workspace/unitree_ros2_ws:/unitree_ros2_ws \
  -v /home/clear/workspace/unitree_sdk2:/unitree_sdk2 \
  -v /home/clear/workspace/unitree_sdk2_python:/unitree_sdk2_python \
  -v /home/clear/workspace/tmp:/temporary \
  unitree_go2_humble
  
xhost -local:docker
