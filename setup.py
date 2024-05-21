"""
Python setup file for the Clothoids C++ library. It uses the SWIG interface to
generate the Python bindings for the C++ library.

Authors:
 - Sebastiano Taddei
 - Gabriele Masina
"""

import os
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from urllib.request import urlretrieve
import zipfile

dirname = os.path.dirname(os.path.abspath(__file__))

# # Define the include directories
# include_dirs = [
#     dirname,
#     os.path.join(dirname, "lib", "include"),
#     os.path.join(dirname, "lib3rd", "include"),
# ]

# # Define the library directories
# library_dirs = [
#     os.path.join(dirname, "lib", "lib"),
#     os.path.join(dirname, "lib3rd", "lib"),
# ]

# # Define the libraries
# library_names = []
# prefix = "lib"
# for library_dir in library_dirs:
#     # Get the filenames in the library directory
#     filenames = os.listdir(library_dir)

#     # For each filename, remove the prefix and suffix
#     for filename in filenames:
#         # Remove the file extension
#         root = os.path.splitext(filename)[0]

#         if root.startswith(prefix):
#             root = root[len(prefix) :]

#         library_names.append(root)

clothoids_module = Extension(
    "_Clothoids",
    sources=[os.path.join("src_py", "Clothoids.i")],
    include_dirs=[],
    library_dirs=[],
    libraries=[],
    swig_opts=["-c++"],
    extra_compile_args=["-std=c++11"],
)


# class build_with_cmake(build_ext):

#     def run(self):
#         for ext in self.extensions:
#             self.build_cmake(ext)
#         super().run()

#     def build_cmake(self, ext):
#         cwd = pathlib.Path().absolute()

#         # these dirs will be created in build_py, so if you don't have
#         # any python sources to bundle, the dirs will be missing
#         build_temp = pathlib.Path(self.build_temp)
#         build_temp.mkdir(parents=True, exist_ok=True)
#         extdir = pathlib.Path(self.get_ext_fullpath(ext.name))
#         extdir.mkdir(parents=True, exist_ok=True)

#         # example of cmake args
#         config = "Debug" if self.debug else "Release"
#         cmake_args = [
#             "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + str(extdir.parent.absolute()),
#             "-DCMAKE_BUILD_TYPE=" + config,
#         ]

#         # example of build args
#         build_args = ["--config", config, "--", "-j4"]

#         os.chdir(str(build_temp))
#         self.spawn(["cmake", str(os.path.join(cwd, ".."))] + cmake_args)
#         if not self.dry_run:
#             self.spawn(["cmake", "--build", "."] + build_args)
#         # Troubleshooting: if fail on line above then delete all possible
#         # temporary CMake files including "CMakeCache.txt" in top level dir.
#         os.chdir(str(cwd))


class build_with_rake(build_ext):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get the path to this file
        self.dirname = os.path.dirname(os.path.abspath(__file__))

    def run(self):
        # Clone the repository
        # print("Cloning the Clothoids repository...")
        # self.clone_repo()

        for ext in self.extensions:
            print("Building the Clothoids library...")
            self.build_rake(ext)
            self.setup_ext(ext)

        super().run()

    def clone_repo(self):
        # Download the latest release from github
        url = "https://github.com/SebastianoTaddei/Clothoids/releases/download/2.0.14/Clothoids.zip"
        filename = os.path.join(self.dirname, "Clothoids.zip")
        unzipdirname = os.path.join(self.dirname, "Clothoids")
        print(f"Downloading {url} to {filename}")
        urlretrieve(url, filename)

        # Unzip the file
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(unzipdirname)

    def build_rake(self, ext):
        # os.chdir(self.dirname)
        self.spawn(["rake", "clean"])
        self.spawn(["rake"])
        # os.chdir(self.dirname)

    def setup_ext(self, ext):
        # Define the include directories
        include_dirs = [
            self.dirname,
            os.path.join(self.dirname, "lib", "include"),
            os.path.join(self.dirname, "lib3rd", "include"),
        ]

        # Define the library directories
        library_dirs = [
            os.path.join(self.dirname, "lib", "lib"),
            os.path.join(self.dirname, "lib3rd", "lib"),
        ]

        # Define the libraries
        library_names = []
        prefix = "lib"
        for library_dir in library_dirs:
            # Get the filenames in the library directory
            filenames = os.listdir(library_dir)

            # For each filename, remove the prefix and suffix
            for filename in filenames:
                # Remove the file extension
                root = os.path.splitext(filename)[0]

                if root.startswith(prefix):
                    root = root[len(prefix) :]

                library_names.append(root)

        ext.include_dirs = include_dirs
        ext.library_dirs = library_dirs
        ext.libraries = library_names


setup(
    ext_modules=[clothoids_module],
    py_modules=["Clothoids"],
    package_dir={"": "src_py"},
    cmdclass={
        "build_ext": build_with_rake,
    },
)
