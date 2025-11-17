module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 3.0"

  name = "${var.cluster_name_tf}-vpc"
  cidr = "10.0.0.0/16"

  # Consider replacing these AZs with data.aws_availability_zones to avoid hardcoding
  azs             = ["eu-central-1a", "eu-central-1b", "eu-central-1c"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true

  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Environment = var.cluster_name_tf
    Project     = "tic-tac-toe-gitops"
  }

  # optional: add more observability/cost tags if desired
  # enable_flow_logs = true
}
