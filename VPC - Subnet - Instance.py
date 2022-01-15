import boto3
ec2 = boto3.resource('ec2')
vpc = ec2.create_vpc(CidrBlock='172.16.0.0/16') # to create VPC
vpc.create_tags(
    Tags=[                          # to give tag to VPC
        {"Key":"TestVPC",
         "Value":"default_vpc"
         }
    ]
)

vpc.wait_until_available()          # to wait for VPC creation
var1 = vpc.id                    # to store vpc id in variable to
subnet = ec2.create_subnet(CidrBlock = '10.0.2.0/24', VpcId= var1)   # Finally subnet created under that VPC
var2 = subnet.id

# Ceate EC2Instance under the Subnet

instances = ec2.create_instances(
 ImageId='ami-04ad2567c9e3d7893',
 InstanceType='t2.micro',
 MaxCount=1,
 MinCount=1,
 NetworkInterfaces=[
  {
 'SubnetId': var2,
 'DeviceIndex': 0,
 'AssociatePublicIpAddress': True,
 'Groups': [
     securitygroup.group_sg-07ed78e796d775d7d
        ]
    }
 ],
 KeyName='ec2-keypair'
)