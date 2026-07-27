import numpy as np
import os
import rosbag2_py
from rclpy.serialization import serialize_message
from sensor_msgs.msg import Imu
 
IMU_TOPIC = "/lowstate/imu"

def topic_meta(name, type_str, fmt="cdr"):
    try:
        return rosbag2_py.TopicMetadata(name=name, type=type_str, serialization_format=fmt)
    except TypeError:  # Jazzy+ needs an id
        return rosbag2_py.TopicMetadata(id=0, name=name, type=type_str, serialization_format=fmt)
 


def add_imu(bag_in, bag_out, imu):
    reader = rosbag2_py.SequentialReader()
    reader.open(rosbag2_py.StorageOptions(uri=bag_in, storage_id="sqlite3"),
                rosbag2_py.ConverterOptions("", ""))
 
    writer = rosbag2_py.SequentialWriter()
    writer.open(rosbag2_py.StorageOptions(uri=bag_out, storage_id="sqlite3"),
                rosbag2_py.ConverterOptions("", ""))
 
    for t in reader.get_all_topics_and_types():
        writer.create_topic(topic_meta(t.name, t.type, t.serialization_format))
    writer.create_topic(topic_meta(IMU_TOPIC, "sensor_msgs/msg/Imu"))
 
    # copy original messages
    while reader.has_next():
        topic, data, t = reader.read_next()
        writer.write(topic, data, t)
 
    # append IMU rows (arrival_ms is the stamp AND the bag time)
    for imu_sample in imu:
        ns = int(imu_sample[0]) * 1_000_000        # ms -> ns, integer math
        imu = Imu()
        imu.header.stamp.sec = ns // 10**9
        imu.header.stamp.nanosec = ns % 10**9
        # imu.orientation.w, imu.orientation.x, imu.orientation.y, imu.orientation.z      = 1.0, 0.0, 0.0, 0.0
        imu.angular_velocity.x, imu.angular_velocity.y, imu.angular_velocity.z          = imu_sample[1], imu_sample[2], imu_sample[3]
        imu.linear_acceleration.x, imu.linear_acceleration.y, imu.linear_acceleration.z = imu_sample[4], imu_sample[5], imu_sample[6]
        writer.write(IMU_TOPIC, serialize_message(imu), ns)
 
    del writer



if __name__ == "__main__":
    import os
    import pandas as pd

    dataset_path = "lidar_calibration"
    item_list = os.listdir(dataset_path)

    datasets = []
    for item in item_list:
        date_str = item.split("_")[0]
        time_str = item.split("_")[1]
        date_time_str = date_str + "_" + time_str
        if date_time_str not in datasets:
            datasets.append(date_time_str)
    datasets.sort()
    
    
    for dataset in datasets:
        path_to_bag = os.path.join(dataset_path, dataset)
        path_to_out = os.path.join(dataset_path, dataset + "_ver2")
        path_to_imu = os.path.join(dataset_path, dataset + "_lowstate.txt")
        
        lowlevel_data = pd.read_csv(path_to_imu)
        
        imu = np.array([
            lowlevel_data['# arrival_ms'],
            lowlevel_data['gyro_x'],
            lowlevel_data['gyro_y'],
            lowlevel_data['gyro_z'],
            lowlevel_data['acc_x'],    
            lowlevel_data['acc_y'],
            lowlevel_data['acc_z'],    
        ]).T
        
        add_imu(bag_in=path_to_bag, bag_out=path_to_out, imu=imu)