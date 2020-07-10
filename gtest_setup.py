import os
from string import Template

class GTestSetup:
    def __init__(self, project, path=None):
        self.project = project
        if path is None:
            self.path = "/home/jwhite/CLionProjects/interview_practice/" + self.project + "/"
        else:
            self.path = path

        self.cmake_file = self.path + 'CMakeLists.txt'
        self.solution_file = self.path + self.project + ".cc"
        self.gtest_file = self.path + "test_" + self.project + ".cc"

    def Setup(self):
        files_written = []
        configuration = [{"file_path": self.cmake_file,
                          "contents": self.GetCMakeTemplate()},
                         {"file_path": self.gtest_file,
                          "contents": self.GetGTestTemplate()},
                         {"file_path": self.solution_file,
                          "contents": self.GetSolutionTemplate()}]
        os.makedirs(self.path, exist_ok=True)

        for file in configuration:
            with open(file["file_path"], 'w') as f:
                f.write(file["contents"])
                files_written.append(file["file_path"])

        return files_written

    def GetCMakeTemplate(self):
        cmake_template = Template("""
cmake_minimum_required(VERSION 3.16)
project($project)

set(CMAKE_CXX_STANDARD 20)
SET(GCC_COVERAGE_COMPILE_FLAGS "-g -O0 -coverage -fprofile-arcs -ftest-coverage")
SET(GCC_COVERAGE_LINK_FLAGS    "-coverage -lgcov")
SET( CMAKE_CXX_FLAGS  "$${CMAKE_CXX_FLAGS} $${GCC_COVERAGE_COMPILE_FLAGS}" )
SET( CMAKE_EXE_LINKER_FLAGS  "$${CMAKE_EXE_LINKER_FLAGS} $${GCC_COVERAGE_LINK_FLAGS}" )

# Locate GTest
find_package(GTest REQUIRED)
include_directories($${GTEST_INCLUDE_DIRS})

add_executable($project test_$project.cc)
target_link_libraries($project $${GTEST_LIBRARIES} pthread)
            """)
        return cmake_template.substitute(project=self.project).strip()

    def GetGTestTemplate(self):
        gtest_template = Template("""
#include "$project.cc"
#include <gtest/gtest.h>

TEST(test_solution, test_connection) {
  ASSERT_EQ(true, false);
}

int main(int argc, char** argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
        """)
        return gtest_template.substitute(project=self.project).strip()

    def GetSolutionTemplate(self):
        return "#include <iostream>"


