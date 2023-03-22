variable "project" {
  default     = "django-auto-test-420"
  type        = string
  description = "Google Cloud Project ID"
}

variable "region" {
  type        = string
  default     = "eu-west1"
  description = "Google Cloud Region"
}

variable "service" {
  type        = string
  default     = "djangosite"
  description = "The name of the service"
}
