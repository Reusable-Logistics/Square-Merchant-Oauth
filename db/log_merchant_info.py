from supabase import create_client, Client


# Supabase settings
SUPABASE_URL = "https://vqssuexxzajyciiqdnek.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZxc3N1ZXh4emFqeWNpaXFkbmVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY1NjM2NTcsImV4cCI6MjAxMjEzOTY1N30.PdFq6mep2N8dU1vDXd6lofL8krKPjK8FA17lNYrm_N8"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_API_KEY)


def log_merchant_info(response):
    result = supabase.table("Merchants").insert({
        "oauth_access_token": response.body['access_token'],
        "oauth_access_token_expires": response.body['expires_at'],
        "oauth_access_refresh_token": response.body['refresh_token'],
        "merchant_id": response.body['merchant_id']
    }).execute()
