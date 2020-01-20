# led_national_flag
robosys_2019ROS

### 概要
「１」を押したらCIV(コートジボワール)，「２」を押したらITA(イタリア)，「３」を押したらGNI(ギニア)の国旗が光るプログラムです．


### 動作環境
|||
|:--:|:--:|
| Raspberry Pi | Raspberry Pi Model 3B+ |
| OS | Ubuntu18.04 |
| ROS | ROS melodic |

### 実行方法
```
$ cd ~/catkin/src
$ git clone https://github.com/todasayaka/led_national_flag.git
$ cd ..
$ catkin_make
$ cd src/led_national_flag/myled
$ bash setup.bash
$ roslaunch led_national_flag.as flag_launch
```

### 回路図

### Demo
https://youtu.be/33rxStsgfUI
