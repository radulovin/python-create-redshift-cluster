# python-create-redshift-cluster
All the scripts below use a config files with the following structure:

------------------------
[CLUSTER]
HOST=dwhcluster.cwoejef1o2x3.us-west-2.redshift.amazonaws.com
DB_NAME=dwh
DB_USER=dwhuser
DB_PASSWORD=somepassword
DB_PORT=5439

[IAM_ROLE]
ARN='arn:aws:iam::144117907596:role/dwhRole'
------------------------

RedShiftCluster1CreateRolePolicy.py
Creates a role and attaches a policy to the role

RedShiftCluster2CreateRSCluster.py
Creates and lunches a ResdShift cluster

RedShiftCluster3DescribeCluster.py
Describes the RedShift cluster

RedShiftCluster4DeleteRDCluster.py
Deletes the cluster

RedShiftCluster5DeleteRolePolicy.py
Deletes the role and the policy
