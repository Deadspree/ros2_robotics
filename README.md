# ros2_robotics

* Build and run container

```bash
cd dockerfiles
docker-compose build
docker-compose up -d
docker exec -it ros2_dev_container bash
```

* Inside the container run the following code
```bash
cd ~/ros2_ws
colcon build --packages-select my_package
source install/setup.bash
ros2 run my_package my_node
```

