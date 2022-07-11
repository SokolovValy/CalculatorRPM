cmake_minimum_required(VERSION 3.5)

project(Calculator LANGUAGES CXX)

set(CMAKE_CXX_STANDART 17)
set(CMAKE_CXX_STANDART_REQUIRED ON)

add_executable(Calculator calc.cpp)

install ( PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/Calculator
          DESTINATION bin )