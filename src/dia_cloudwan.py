from diagrams import Cluster, Diagram
from diagrams.aws.iot import IotCore
from diagrams.aws.network import TransitGateway
from diagrams.aws.network import VPC
from diagrams.aws.network import DirectConnect
from diagrams.aws.network import VpnConnection as VPN
from diagrams.aws.general import Client
from diagrams.aws.iot import IotGreengrassConnector
from diagrams.aws.network import TransitGatewayAttachment
from diagrams.aws.iot import IotFactory


with Diagram("CloudWAN", show=False, direction="TB"):
    base = IotFactory("base")
    tgw_useast2 = TransitGateway("tgw-019d8b")

    with Cluster("us-east-2"):
        us_east_2_core = IotCore("us-east-2")
        us_east_2 = [
            VPN("vpn-0e8c90"),
            VPC("vpc-0e2150"),
            VPC("vpc-00559"),
            VPC("vpc-0871d2"),
            VPC("vpc-092722"),
            VPC("vpc-0957a8"),
            VPN("vpn-0d9add"),
            VPC("vpc-0fa7ff"),
            VPC("vpc-0575ee"),
            VPC("vpc-0322cf"),
            VPC("vpc-017f93"),
            VPC("vpc-074095"),
            VPC("vpc-08f0d2")
        ]
        us_east_2_core - us_east_2
    
    with Cluster("us-west-2"):
        us_west_2_core = IotCore("us-west-2")
        us_west_2 = [
            VPN("vpn-0e8c90"),
            VPC("vpc-0e2150"),
            VPC("vpc-00559"),
            VPC("vpc-0871d2"),
            VPC("vpc-092722"),
            VPC("vpc-0957a8"),
            VPN("vpn-0d9add"),
            VPC("vpc-0fa7ff"),
            VPC("vpc-0575ee"),
            VPC("vpc-0322cf"),
            VPC("vpc-017f93"),
            VPC("vpc-074095"),
            VPC("vpc-08f0d2")
        ]
        us_west_2_core - us_west_2

    with Cluster("eu-west-1"):
        eu_west_1_core = IotCore("eu-west-1")
        eu_west_1 = [
            VPN("vpn-0e8c90"),
            VPC("vpc-0e2150"),
            VPC("vpc-00559"),
            VPC("vpc-0871d2"),
            VPC("vpc-092722"),
            VPC("vpc-0957a8"),
            VPN("vpn-0d9add"),
            VPC("vpc-0fa7ff"),
            VPC("vpc-0575ee"),
            VPC("vpc-0322cf"),
            VPC("vpc-017f93"),
            VPC("vpc-074095"),
            VPC("vpc-08f0d2")
        ]
        eu_west_1_core - eu_west_1
    
    base - tgw_useast2 - us_east_2_core
    us_west_2_core - us_east_2_core - eu_west_1_core
    us_east_2_core - eu_west_1_core