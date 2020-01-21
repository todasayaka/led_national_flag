# led_national_flag
robosys_2019ROS

### 概要
「１」を押したらCIV(コートジボワール)，「２」を押したらITA(イタリア)，「３」を押したらGNI(ギニア)の国旗が光るプログラムです．


### 動作環境
|||
|:--:|:--:|
| Raspberry Pi | Raspberry Pi Model 3B+ |
| OS | Ubuntu18.04 |
| ROS | ROS Melodic |

### 実行方法
```
$ cd ~/catkin/src
$ git clone https://github.com/todasayaka/led_national_flag.git
$ cd ..
$ catkin_make
$ cd src/led_national_flag/myled
$ bash setup.bash
$ roslaunch led_national_flag flag.launch
```

### 回路図
![kairozu](https://user-images.githubusercontent.com/58972091/72800038-ca461c80-3c89-11ea-88c3-2e26f33f3e2c.JPG)

### Demo
https://youtu.be/33rxStsgfUI
