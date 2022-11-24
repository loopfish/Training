variable "resource_group_name" {
  type = string
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
  type = string
  default = "uksouth"
}