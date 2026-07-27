xhost +local:docker
sudo docker run -it --privileged --net=host \
  --gpus all \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /home/clear/workspace/dataset:/datasets \
  -v /home/clear/workspace/fastlio2_ws:/fastlio2_ws \
  -v /home/clear/workspace/lidar_init:/lidar_init \
  fastlio2 \
  bash -c "source /fastlio2_ws/install/setup.bash && bash"
  
xhost -local:docker
