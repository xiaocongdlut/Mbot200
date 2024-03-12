cmake_minimum_required(VERSION 2.8.3)

project(Mbot200)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)


find_package(catkin  REQUIRED COMPONENTS
move_base_msgs 
actionlib
roscpp
)

include_directories(include ${catkin_INCLUDE_DIRS} )

add_executable(set_nav_goals set_nav_goals.cpp)
target_link_libraries(set_nav_goals ${catkin_LIBRARIES})

catkin_install_python(PROGRAMS
  scripts/keyboard_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)