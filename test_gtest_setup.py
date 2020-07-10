import pytest
from gtest_setup import GTestSetup


def test_cmake_template():
    assert GTestSetup(project="foobar").GetCMakeTemplate() == """
cmake_minimum_required(VERSION 3.16)
project(foobar)

set(CMAKE_CXX_STANDARD 20)
SET(GCC_COVERAGE_COMPILE_FLAGS "-g -O0 -coverage -fprofile-arcs -ftest-coverage")
SET(GCC_COVERAGE_LINK_FLAGS    "-coverage -lgcov")
SET( CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} ${GCC_COVERAGE_COMPILE_FLAGS}" )
SET( CMAKE_EXE_LINKER_FLAGS  "${CMAKE_EXE_LINKER_FLAGS} ${GCC_COVERAGE_LINK_FLAGS}" )

# Locate GTest
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

add_executable(foobar test_foobar.cc)
target_link_libraries(foobar ${GTEST_LIBRARIES} pthread)
                                                               """.strip()


def test_gtest_template():
    assert GTestSetup(project="foobar").GetGTestTemplate() == """
#include "foobar.cc"
#include <gtest/gtest.h>

TEST(test_solution, test_connection) {
  ASSERT_EQ(true, false);
}

int main(int argc, char** argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
} 
    """.strip()


def test_solution_template():
    assert GTestSetup(project="foobar").GetSolutionTemplate() == """
#include <iostream>    
    """.strip()


def test_foobar_setup():
    assert GTestSetup(project="foobar").Setup() == [
        '/home/jwhite/CLionProjects/interview_practice/foobar/CMakeLists.txt',
        '/home/jwhite/CLionProjects/interview_practice/foobar/test_foobar.cc',
        '/home/jwhite/CLionProjects/interview_practice/foobar/foobar.cc']
