
import boto3
ec2 = boto3.resource('ec2')
instances = ec2.create_instances(
 ImageId='ami-04ad2567c9e3d7893',
 InstanceType='t2.micro',
 MaxCount=1,
 MinCount=1,
 NetworkInterfaces=[
  {
 'SubnetId': 'subnet-7afebe5b',
 'DeviceIndex': 0,
 'AssociatePublicIpAddress': True,
 'Groups': [
  securitygroup.group_sg-07ed78e796d775d7d
           ]
  }
 ],
 KeyName='ec2-keypair'
)
