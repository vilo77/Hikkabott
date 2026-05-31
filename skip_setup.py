import os
import sys

# Cek apakah semua env vars sudah ada
required_vars = ['API_ID', 'API_HASH', 'STRING_SESSION']
missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    print(f"❌ ERROR: Missing environment variables: {', '.join(missing)}")
    print("Please set these variables in Railway Dashboard -> Variables")
    sys.exit(1)

print("✅ All environment variables found, skipping interactive setup...")

# Patch Hikka untuk skip setup wizard
try:
    import hikka.configurator as configurator
    
    # Override api_config untuk skip input interaktif
    def skip_api_config(*args, **kwargs):
        print("✅ Using environment variables (non-interactive mode)")
        return {
            'api_id': int(os.getenv('API_ID')),
            'api_hash': os.getenv('API_HASH'),
            'session_string': os.getenv('STRING_SESSION'),
            'colored': False
        }
    
    configurator.api_config = skip_api_config
    print("✅ Hikka configurator patched successfully")
    
except ImportError as e:
    print(f"⚠️ Warning: Could not patch configurator: {e}")
    print("Hikka will try to use environment variables automatically")

# Jalankan Hikka
print("🚀 Starting Hikka userbot...")
from hikka import main
main.hikka.main()
