terraform {
  backend "s3" {
    bucket         = "marwan-devsecops-terraform-state"  # ← your bucket name
    key            = "dev/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
