import src.{{ cookiecutter.project_slug }} as {{ cookiecutter.project_slug }}, unittest


class TestEverything(unittest.TestCase):
    def test_something(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
