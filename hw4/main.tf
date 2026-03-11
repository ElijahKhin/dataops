terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = ">=0.80"
    }
  }
}

provider "yandex" {
  zone = "ru-central1-a"
}

resource "yandex_compute_instance" "ml_vm" {

  name = "ml-fastapi-server"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd8d8c8k9t8example" # ubuntu 22.04
      size     = 20
    }
  }

  network_interface {
    subnet_id = "your-subnet-id"
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}

output "external_ip" {
  value = yandex_compute_instance.ml_vm.network_interface.0.nat_ip_address
}
