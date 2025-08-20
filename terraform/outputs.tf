output "lambda_api_url" {
  value = aws_api_gateway_deployment.api_gw.invoke_url
  description = "URL de invocación de la Lambda a través de API Gateway"
}
