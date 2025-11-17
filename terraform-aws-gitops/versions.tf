if (-not (Test-Path .\versions.tf)) {
@'
terraform {
  required_version = ">= 1.3, < 2.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.66"
    }
  }
}
'@ | Set-Content versions.tf -Force
Write-Output "Created versions.tf with recommended provider pinning."
} else {
  Write-Output "versions.tf exists; ensure it contains the root terraform block and provider constraint."
}
