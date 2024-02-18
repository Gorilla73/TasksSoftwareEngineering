add_executable(run_actual_tests testFILE_1.cpp ../../Project_DIR/Source/isPrime.cpp)

target_link_libraries(run_actual_tests gtest gtest_main)
