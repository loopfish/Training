terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.33.0"
    }
  }
  required_version = "~> 1.3.0"

  cloud {
    organization = "loopfish"
    workspaces {
      name = "learn-terraform-azure"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location

  tags = var.resource_tags
}

# Create a virtual network
resource "azurerm_virtual_network" "vnet" {
  name                = "myTFVnet"
  address_space       = ["10.0.0.0/16"]
  location            = var.location
  resource_group_name = var.resource_group_name

  tags = var.resource_tags

  depends_on = [
    azurerm_resource_group.rg
  ]
}

resource "azurerm_storage_account" "storage" {
  name                     = replace("sa${var.resource_tags["project"]}${var.resource_tags["environment"]}", "-", "")
  location                 = var.location
  resource_group_name      = var.resource_group_name
  account_tier             = "Standard"
  account_replication_type = "LRS"

  depends_on = [
    azurerm_resource_group.rg
  ]
}
