# S3 to Iguana Forwarder Lambda Function

This AWS Lambda function is triggered by an S3 `PUT` event. It reads the HL7 file content and forwards it to the configured Iguana gateway endpoint via HTTP POST.

## 🔧 Environment Variables
- `IGUANA_ENDPOINT`: Full HTTPS URL of your Iguana SaaS endpoint.
- `IGUANA_API_KEY`: (Optional) API key header for Iguana authentication.

## Event Format
Triggered via S3 PUT:
```
{
  "Records": [
    {
      "s3": {
        "bucket": {"name": "your-bucket"},
        "object": {"key": "path/to/your/file.hl7"}
      }
    }
  ]
}
```
