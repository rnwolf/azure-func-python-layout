"""
For pytest.

By defining conftest.py in your root path, pytest will recognize application
modules without specifying PYTHONPATH.
In the background, py.test modifies your sys.path by including all
submodules which are found from the root path.

"""
