cmake_minimum_required(VERSION 3.0.0)
project(sukonbu_cpp)
set(PROJECT_NAME sukonbu_cpp)
add_executable(${PROJECT_NAME} 
    tests.cpp
    )
set_property(TARGET ${PROJECT_NAME} 
    PROPERTY CXX_STANDARD 20
    )
target_include_directories(${PROJECT_NAME} PUBLIC
    Catch2/single_include
    nlohmann-json/include
    ../generated/cpp
    )