terraform {
  required_providers {
    intersight = {
      source  = "CiscoDevNet/intersight"
      version = ">= 1.0.22"
    }
  }
}

variable "INTERSIGHT_API_KEY_ID" {
  sensitive = false
}

variable "INTERSIGHT_API_PRIVATE_KEY" {
  sensitive = true
}

provider "intersight" {
  apikey    = var.INTERSIGHT_API_KEY_ID
  secretkey = var.INTERSIGHT_API_PRIVATE_KEY
  endpoint  = "https://intersight.com"
}

data "intersight_organization_organization" "CLUS" {
  name = "CLUS"
}

resource "intersight_ntp_policy" "us_ntp" {
  name = "terraform"
  tags {
    key   = "CLUS2023"
    value = "Devnet-1061"
  }
  tags {
    key   = "Language"
    value = "Terraform"
  }

  organization {
    moid = data.intersight_organization_organization.CLUS.results[0].moid
  }
  enabled = true
  ntp_servers = [
    "1.1.1.1",
    "2.2.2.2",
  ]
  timezone = "America/Phoenix"
}
