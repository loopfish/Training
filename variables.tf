variable "resource_group_name" {
  default = "myTFResourceGroup"
}

variable "resource_tags" {
    description = "Tags to set for all resources"
    type = map(string)
    default = {
      "project" = "project-alpha"
      "environment" = "dev"
    }
}

variable "location" {
  default = "uksouth"
}