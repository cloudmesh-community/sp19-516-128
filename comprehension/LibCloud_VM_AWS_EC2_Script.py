# This script allows to create, start, stop and delete a VM on AWS EC2

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.base import NodeImage
import yaml

# read access key, id and region from config file
config = yaml.load(open('config.yml'))
ACCESS_ID = config['ACCESS_ID']
SECRET_KEY = config['SECRET_KEY']
REGION = config['REGION']
AMI_ID = config['AMI_ID']
KEYPAIR_NAME = config['KEYPAIR_NAME']

# EC2 Size
SIZE_ID = 't2.micro'
# A list of security groups you want this node to be added to
SECURITY_GROUP_NAMES = ['default']
#EC2 node name
NODE_NAME = 'test-node-1'


cls = get_driver(Provider.EC2)
CONNECTION = cls(ACCESS_ID, SECRET_KEY, region=REGION)


# function to create node
def create_node(node_name, connection, size_id, ami_id, keypair_name, security_group_names):
    print('Creating node : ' + node_name)
    sizes = connection.list_sizes()
    size = [s for s in sizes if s.id == size_id][0]
    image = NodeImage(id=ami_id, name=None, driver=connection)
    print('Selected images :')
    print(image)
    print('Selected size : ')
    print(size)
    node = connection.create_node(name=node_name, image=image, size=size,
                              ex_keyname=keypair_name,
                              ex_securitygroup=security_group_names)
    print('Created !!')


# Function to stop a node
def stop_node(node_name, connection):
    node = [n for n in connection.list_nodes() if n.name == node_name][0]
    print('Stopping node : '+ node_name)
    connection.ex_stop_node(node=node)
    print('Stopped !!')


# Function to start the node
def start_node(node_name, connection):
    node = [n for n in connection.list_nodes() if n.name == node_name][0]
    print('Starting node : '+ node_name)
    connection.ex_start_node(node=node)
    print('Started !!')


def delete_node(node_name, connection):
    node = [n for n in connection.list_nodes() if n.name == node_name][0]
    print('Deleting node : '+ node_name)
    node.destroy()
    print('Deleted !!')



#Uncomment the respective call for various steps as needed after adding entries in config.yml for the below values
# ACCESS_ID
# SECRET_KEY
# REGION
# AMI_ID
# KEYPAIR_NAME

#create_node(NODE_NAME, CONNECTION, SIZE_ID, AMI_ID, KEYPAIR_NAME, SECURITY_GROUP_NAMES)

#stop_node(NODE_NAME, CONNECTION)

#start_node(NODE_NAME, CONNECTION)

#delete_node(NODE_NAME, CONNECTION)
