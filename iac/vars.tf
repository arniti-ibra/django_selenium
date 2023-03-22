variable "project" {
  default = 
  type        = string
  description = "Google Cloud Project ID"
}

variable "region" {
  type        = string
  default     = "us-central1"
  description = "Google Cloud Region"
}

variable "service" {
  type        = string
  default     = "gametracker"
  description = "The name of the service"
}
