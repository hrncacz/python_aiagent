import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


class TestsRoot(unittest.TestCase):
    # def test_get_files_info(self):
    #     test_tuple_arr = [("calculator", ".", "- main.py: file_size:576 bytes, is_dir=False\n- pkg: file_size:66 bytes, is_dir=True\n- tests.py: file_size:1343 bytes, is_dir=False"),
    #                       ("calculator", "pkg", "- calculator.py: file_size:1738 bytes, is_dir=False\n- __pycache__: file_size:96 bytes, is_dir=True\n- render.py: file_size:783 bytes, is_dir=False"),
    #                       ("calculator", "/bin",
    #                        "Error: Cannot list \"/bin\" as it is outside the permitted working directory"),
    #                       ("calculator", "../", "Error: Cannot list \"../\" as it is outside the permitted working directory"),]
    #     for t in test_tuple_arr:
    #         self.assertEqual(get_files_info(t[0], directory=t[1]), t[2])
    #         print(get_files_info(t[0], directory=t[1]), t[2])

    # def test_get_file_content(self):
    #     test_tuple_arr = [("calculator", "main.py"),
    #                       ("calculator", "pkg/calculator.py"),
    #                       ("calculator", "/bin/cat")]
    #
    #     for t in test_tuple_arr:
    #         print(get_file_content(t[0], t[1]))

    # def test_write_file(self):
    #     test_tuple_arr = [("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    #                       ("calculator", "pkg/morelorem.txt",
    #                        "lorem ipsum dolor sit amet"),
    #                       ("calculator", "/tmp/temp.txt", "this should not be allowed")]
    #     for t in test_tuple_arr:
    #         print(write_file(t[0], t[1], t[2]))

    def test_run_python_file(self):
        test_tuple_arr = [("calculator", "main.py"),
                          ("calculator", "tests.py"),
                          ("calculator", "../main.py"),
                          ("calculator", "nonexistent.py")]
        for t in test_tuple_arr:
            print(run_python_file(t[0], t[1]))


if __name__ == "__main__":
    unittest.main()
