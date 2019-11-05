cmake_minimum_required(VERSION 3.0.0)
project(cameraserver)
add_compile_options(-std=c++11)

find_package(OpenCV REQUIRED)

include_directories(
        include
)
add_executable(server src/server.cpp src/imageServer.cpp src/commServer.cpp)
target_link_libraries(server pthread ${OpenCV_LIBS})