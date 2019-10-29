import base64
from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
    core
)

class VpcStack(core.Stack):
    def __init__(self, app: core.App, id: str):
        super().__init__(app, id)
        
        # custom /19 subnets for EKS NG to leave some address space for other services in future
        vpcSubnetConfigurationList = []

        vpcSubnetConfigurationList.append(
            ec2.SubnetConfiguration(name="cash-subnet-public", subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=19)
        )
        vpcSubnetConfigurationList.append(
            ec2.SubnetConfiguration(name="cash-subnet-private", subnet_type=ec2.SubnetType.PRIVATE, cidr_mask=19)
        ) 
        
        self.vpc = ec2.Vpc(self, "EKS-VPC",
            cidr="10.1.0.0/16",
            nat_gateways=1,
            subnet_configuration=vpcSubnetConfigurationList
        )
        
class RDSStack(core.Stack):
    def __init__(self, app: core.App, id: str, vpc = ec2.Vpc, **kwargs):
        super().__init__(app, id, **kwargs)
        
        db_cluster = rds.DatabaseCluster(self, "EKS-RDS",
            engine=rds.DatabaseClusterEngine.AURORA_POSTGRESQL,
            master_user=rds.Login(username="root"),
            instance_props=rds.InstanceProps(
                instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MEDIUM),
                vpc=vpc
            )
        )
    
        
app = core.App()
vpc_stack = VpcStack(app, "EKS-VPC-stack")
RDSStack(app, "RDS-stack", vpc_stack.vpc)
app.synth()