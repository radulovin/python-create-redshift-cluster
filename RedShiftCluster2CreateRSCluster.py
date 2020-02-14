import pandas as pd
import boto3
import json

#Create a new IAM user in your AWS account
#Give it AdministratorAccess, From Attach existing policies directly Tab
#Take note of the access key and secret
#Edit the file dwh.cfg in the same folder as this notebook and fill
#[AWS]
#KEY= YOUR_AWS_KEY
#SECRET= YOUR_AWS_SECRET

import configparser
config = configparser.ConfigParser()
config.read_file(open('dwh_cluster.cfg'))

KEY                    = config.get('AWS','KEY')
SECRET                 = config.get('AWS','SECRET')

DWH_CLUSTER_TYPE       = config.get("DWH","DWH_CLUSTER_TYPE")
DWH_NUM_NODES          = config.get("DWH","DWH_NUM_NODES")
DWH_NODE_TYPE          = config.get("DWH","DWH_NODE_TYPE")

DWH_CLUSTER_IDENTIFIER = config.get("DWH","DWH_CLUSTER_IDENTIFIER")
DWH_DB                 = config.get("DWH","DWH_DB")
DWH_DB_USER            = config.get("DWH","DWH_DB_USER")
DWH_DB_PASSWORD        = config.get("DWH","DWH_DB_PASSWORD")
DWH_PORT               = config.get("DWH","DWH_PORT")

DWH_IAM_ROLE_NAME      = config.get("DWH", "DWH_IAM_ROLE_NAME")

#####################################
#Create client for Redshift
redshift = boto3.client('redshift',
                       region_name='us-west-2',
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET
                       )
iam = boto3.client('iam',aws_access_key_id=KEY,
                     aws_secret_access_key=SECRET,
                     region_name='us-west-2'
                  )

#STEP 2: Redshift Cluster
roleArn = iam.get_role(RoleName=DWH_IAM_ROLE_NAME)['Role']['Arn']

try:
    response = redshift.create_cluster(
        #HW
        ClusterType=DWH_CLUSTER_TYPE,
        NodeType=DWH_NODE_TYPE,
        NumberOfNodes=int(DWH_NUM_NODES),

        #Identifiers & Credentials
        DBName=DWH_DB,
        ClusterIdentifier=DWH_CLUSTER_IDENTIFIER,
        MasterUsername=DWH_DB_USER,
        MasterUserPassword=DWH_DB_PASSWORD,

        #Roles (for s3 access)
        IamRoles=[roleArn]
    )
except Exception as e:
    print(e)
