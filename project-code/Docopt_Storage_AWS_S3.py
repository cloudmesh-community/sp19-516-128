document what a container is

"""
Usage:
    cms storage [--cloud=<SERVICE>] list containers
    cms storage [--cloud=<SERVICE>] create container CONTAINER
    cms storage [--cloud=<SERVICE>] delete container CONTAINER
    cms storage [--cloud=<SERVICE>] putfile CONTAINER FILESOURCE FILETARGET
    cms storage [--cloud=<SERVICE>] delete file CONTAINER FILENAME
    cms storage [--cloud=<SERVICE>] get file CONTAINER FILENAME
    cms storage [--cloud=<SERVICE>] list container files CONTAINER
    cms storage [--cloud=<SERVICE>] list file info CONTAINER FILENAME ...

Manage file storage on AWS S3 buckets and perform operations like put, get, delete on the files.

Arguments:
    CONTAINER   Mame of the logical container to host a file. E.g this will be the bucket name on AWS S3
    FILESOURCE  Complete file path (including the directory and filename) of the local file to be uploaded on cloud
    FILETARGET  Complete file path (including the directory and filename) where the file is to be uploaded on cloud
    FILENAME    Complete file path (including the directory and filename) on the cloud

Options:
  -h --help
  --cloud=<SERVICE>  Cloud service name like aws or azure or box or google [default: aws]

Description:
    Commands to manage file storage on cloud/

    storage listcontainers
        lists all containers present on the cloud storage

    storage createcontainer CONTAINER
        creates a container with the given name in the cloud storage

    storage deletecontainer CONTAINER
        deletes a container with the given name in the cloud storage

    storage putfile CONTAINER FILESOURCE FILETARGET
        uploads a file from the source file path to the target file on the cloud storage in the specified container

    storage deletefile CONTAINER FILENAME
        deletes a file from the specified container on the cloud storage

    storage getfile CONTAINER FILENAME
        downloads a file from the specified container on the cloud storage

    storage listcontainerfiles CONTAINER
        lists all file in the specified container on the cloud storage

    storage listfileinfo CONTAINER [FILENAME] ...
        returns properties of the specified files in the container on the cloud storage


Examples:
replace python Docopt_Storage_AWS_S3.py  with cms

   python Docopt_Storage_AWS_S3.py storage listcontainers

    python Docopt_Storage_AWS_S3.py storage listcontainers --cloud=aws

    python Docopt_Storage_AWS_S3.py storage createcontainer my_container

    python Docopt_Storage_AWS_S3.py storage deletecontainer my_container

    python Docopt_Storage_AWS_S3.py storage putfile my_container file1 file2

    python Docopt_Storage_AWS_S3.py storage	deletefile my_container file1

    python Docopt_Storage_AWS_S3.py storage	getfile my_container file1

    python Docopt_Storage_AWS_S3.py storage	listcontainerfiles my_container

    python Docopt_Storage_AWS_S3.py storage listfileinfo my_container file1 file2

"""

from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)
