#!/snap/bin/pwsh
$intersight = @{
    BasePath          = "https://intersight.com"
    ApiKeyId          = (Get-item -Path env:\INTERSIGHT_API_KEY_ID).Value
    ApiKeyFilePath    = "./key.pem"
    HttpSigningHeader = @("(request-target)", "Host", "Date", "Digest")
}

Set-IntersightConfiguration @intersight
Get-IntersightConfiguration
