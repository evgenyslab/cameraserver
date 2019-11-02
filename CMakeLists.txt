cmake_minimum_required(VERSION 3.0.0)
project(cameraserver)
add_compile_options(-std=c++11)

find_package(OpenCV REQUIRED)

include_directories(
        include
)
add_executable(source src/source.cpp src/serverWriter.cpp)
target_link_libraries(source pthread ${OpenCV_LIBS})