variable "aws_region" {
  description = "AWS region for infrastructure"
  type        = string
}

variable "cluster_name_tf" {
  description = "EKS Cluster name"
  type        = string
}

variable "vpc_id" {
  description = "VPC id to deploy the EKS cluster into"
  type        = string
}

variable "subnet_ids" {
  description = "List of subnet IDs for the EKS cluster (private or public subnets depending on your design)"
  type        = list(string)
}
