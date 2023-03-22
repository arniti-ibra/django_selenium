# Step 14: View final output
output "superuser_password" {
  value     = google_secret_manager_secret_version.superuser_password.secret_data
  sensitive = true
}

output "service_url" {
  value = google_cloud_run_service.service.status[0].url
}