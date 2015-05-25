from os import path
from time import time

def create_file_name(parent_folder_name, instance_name, uploaded_filename):
    filename_only, file_extension = path.splitext(uploaded_filename)
    timestamp = str(time()).replace('.', '_')
    return "%s/%s_%s%s" % (parent_folder_name, instance_name, timestamp, file_extension)
