import os
import git


# paths:
ROOT_DIR = git.Repo(".", search_parent_directories=True).working_tree_dir
DATA_DIR = os.path.join(ROOT_DIR, "data")
LOG_DIR = os.path.join(ROOT_DIR, "logs")


