
  required_version = ">= 1.4.0"
}

provider "aws" {
  region = var.aws_region
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = ">= 19.0.0"

  cluster_name    = var.cluster_name_tf
  cluster_version = "1.27"

  # REPLACE these with correct references from your config:
  # If you have a VPC module named 'vpc':
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.public_subnets # or module.vpc.private_subnets / var.subnet_ids

  cluster_endpoint_public_access  = true
  cluster_endpoint_private_access = true

  create_kms_key              = false
  create_cloudwatch_log_group = false

  # If you don't want encryption, either omit this or set to an empty list:
  cluster_encryption_config = []

  eks_managed_node_groups = {
    default = {
      min_size     = 2
      max_size     = 4
      desired_size = 2

      instance_types = ["t3.medium"]
      capacity_type  = "ON_DEMAND"
    }
  }

  tags = {
    Environment = var.cluster_name_tf
    Project     = "tic-tac-toe-gitops"
  }
}


