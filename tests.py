import unittest
from functions.get_files_info import get_files_info


class TestsRoot(unittest.TestCase):
    def test_functions(self):
        test_tuple_arr = [("calculator", ".", "- main.py: file_size:576 bytes, is_dir=False\n- pkg: file_size:66 bytes, is_dir=True\n- tests.py: file_size:1343 bytes, is_dir=False"),
                          ("calculator", "pkg", "- calculator.py: file_size:1738 bytes, is_dir=False\n- __pycache__: file_size:96 bytes, is_dir=True\n- render.py: file_size:783 bytes, is_dir=False"),
                          ("calculator", "/bin",
                           "Error: Cannot list \"/bin\" as it is outside the permitted working directory"),
                          ("calculator", "../", "Error: Cannot list \"../\" as it is outside the permitted working directory"),]
        for t in test_tuple_arr:
            self.assertEqual(get_files_info(t[0], directory=t[1]), t[2])
            print(get_files_info(t[0], directory=t[1]), t[2])


if __name__ == "__main__":
    unittest.main()
