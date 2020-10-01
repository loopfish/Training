terraform {
  backend "gcs" {
    bucket      = "terraform-training-sk"
    // prefix      = "training.tfstate"
    credentials = "/mnt/c/Users/skomp/GCP-Terraform-Key.json"
  }
}

provider "google" {
  project = "training-291217"
  region  = "us-east1"
  credentials = file("/mnt/c/Users/skomp/GCP-Terraform-Key.json")
}

data "google_service_account" "terraform" {
  account_id = var.service_account_name
  project    = var.project_id
}

resource "google_compute_instance" "vm_training" {
  name                      = "training-vm"
  zone                      = "us-east1-b"
  machine_type              = "f1-micro"
  allow_stopping_for_update = true
  service_account {
    email  = data.google_service_account.terraform.email
    scopes = ["cloud-platform"]
  }     
  labels ={
    project = "training"
  }
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2004-lts"
    }
  }

  network_interface {
    network = google_compute_network.vpc_network.self_link
    access_config {

    }
  }
}

resource "google_compute_network" "vpc_network" {
  name                    = "training-network"
  auto_create_subnetworks = "true"
}