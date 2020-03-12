cmake_minimum_required(VERSION 3.0.0)
project(gltfformat_tests)
add_executable(${PROJECT_NAME} 
    tests.cpp
    )
set_property(TARGET ${PROJECT_NAME} 
    PROPERTY CXX_STANDARD 20
    )
target_include_directories(${PROJECT_NAME} PUBLIC
    external_include
    include
    )
