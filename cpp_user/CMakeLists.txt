cmake_minimum_required(VERSION 3.0.0)
project(sukonbu_cpp)
set(PROJECT_NAME sukonbu_cpp)
file(GLOB SRC
     *.cpp
     *.h
    ) 
add_executable(${PROJECT_NAME} 
    ${SRC}
    )
set_property(TARGET ${PROJECT_NAME} 
    PROPERTY CXX_STANDARD 20
    )
target_include_directories(${PROJECT_NAME} PUBLIC
    Catch2/include
    nlohmann-json
    ../generated/cpp
    )
