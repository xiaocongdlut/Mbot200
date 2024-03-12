## 小车建图、导航

文件：
    1、display.launch: 启动 rviz, 显示最初导入的文件，没有 laser 信息
    2、gazebo.launch: 启动 gazebo，显示最初的模型
    3、control.launch: 启动 gazebo，显示加入 senser 后的总模型
    4、gmapping.launch: 绘制二维栅格地图
    5、map_save.launch: 控制小车运动、建图、并保存地图
    6、map_server.launch: 显示保存的地图
    7、amcl.launch: 定位配置文件
    8、test_amcl.launch: 实现机器人定位
    9、path.launch: move_base、代价地图配置文件
    10、test_path.launch: 实现路径规划(move_base)、显示代价地图、并可通过Rviz工具栏的 2D Nav Goal设置目的地实现导航
    11、slam_auto: 控制机器人运动、完成建图
    12、控制机器人移动到目标点：
        set_nav_goals.cpp 文件：设定 x、y 方向移动距离
        方法一：
            依次启动 control.launch、slam_auto.launch 和 rosrun Mbot200 set_nav_goals
        方法二：（集成到一个 launch 文件）
            启动 set_nav_goals.launch（有报错）
    

启动顺序：
    4~11 需先启动 control.launch，再启动相应 launch 文件



注意：1、改完文件后 记得手动保存 Ctrl+s
     2、cpp 编译：ctrl+shift+B
     3、Python 版本（python 2）
     4、节点不可重复包含
     5、存在依赖关系的文件、要注意顺序
     6、在 package.xml 中增加包依赖
     7、用 launch 文件启动自己写的 cpp/python 节点
        eg: <node name="set_nav_goals" pkg="Mbot200" type="set_nav_goals"/>
            name: 自己起的
            pkg: 功能包名
            type: 节点的可执行文件名称



