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
![ROS_kairozu_2](https://user-images.githubusercontent.com/58972091/73038265-187b3b80-3e95-11ea-9066-97b043a31ee1.jpg)

### Demo
https://youtu.be/33rxStsgfUI
