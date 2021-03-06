pyCheck
=======

pyCheck can be used to check whether a project adheres to certain guidelines.
For this purpose it provides a set of checkers, each for a specific task. 
Currently the following checker types exist:

- CheckPath
- CheckJson
- CheckComposerJson

Each checker is invoked with the target as its constructor argument (see examples below).

CheckPath
---------
Checks file paths

.. code:: python

    path = CheckPath('path/to/check')
    path.does_exist()
    path.is_file()

CheckJson
---------
Checks JSON files

.. code:: python

    json = CheckJson('path/to/file.json')
    json.does_contain_member('foo')

CheckComposerJson
-----------------
Checks composer JSON files (i.e. composer.json)

.. code:: python

    composer = CheckComposer('path/to/composer.json')
    composer.does_contain_member('foo')

Usage
=====
You can use it by writing a python script where you instantiate the required checkers:

.. code-block:: python

    import pycheck.checkpath
    import sys
    import os


    def main(project_path):
        if pycheck.checkpath.CheckPath(project_path).does_exist():
            print project_path, "exists"

            if pycheck.checkpath.CheckPath(project_path).does_contain("src"):
                print project_path, "does contain 'src'"
                src_dir = os.path.join(project_path, "src")
                if pycheck.checkpath.CheckPath(src_dir).is_a_directory():
                    print src_dir, "is a directory"
                else:
                    print src_dir, "is not a directory"
            else:
                print project_path, "does not contain 'src'"
        else:
            print project_path, "does not exist"

    if __name__ == '__main__':
        main(sys.argv[1:][0])



