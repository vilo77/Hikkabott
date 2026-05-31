import os
import sys
import traceback

print("=" * 60, flush=True)
print("🔍 Hikka Startup Debug Mode", flush=True)
print("=" * 60, flush=True)

# Cek apakah semua env vars sudah ada
required_vars = ['API_ID', 'API_HASH', 'STRING_SESSION']
missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    print(f"❌ ERROR: Missing environment variables: {', '.join(missing)}", flush=True)
    print("Please set these variables in Railway Dashboard -> Variables", flush=True)
    sys.exit(1)

print("✅ All environment variables found", flush=True)
print(f"   API_ID: {os.getenv('API_ID')[:5]}...", flush=True)
print(f"   API_HASH: {os.getenv('API_HASH')[:10]}...", flush=True)
print(f"   STRING_SESSION: {os.getenv('STRING_SESSION')[:20]}...", flush=True)

print("✅ Skipping interactive setup...", flush=True)

# Patch Hikka untuk skip setup wizard
try:
    import hikka.configurator as configurator
    
    def skip_api_config(*args, **kwargs):
        print("✅ Using environment variables (non-interactive mode)", flush=True)
        return {
            'api_id': int(os.getenv('API_ID')),
            'api_hash': os.getenv('API_HASH'),
            'session_string': os.getenv('STRING_SESSION'),
            'colored': False
        }
    
    configurator.api_config = skip_api_config
    print("✅ Hikka configurator patched successfully", flush=True)
    
except ImportError as e:
    print(f"❌ ERROR patching configurator: {e}", flush=True)
    traceback.print_exc()

# Jalankan Hikka
print("🚀 Starting Hikka userbot...", flush=True)
print("📦 Importing hikka.main...", flush=True)

try:
    from hikka import main
    print("✅ hikka.main imported successfully", flush=True)
    print("🔥 Calling main.hikka.main()...", flush=True)
    main.hikka.main()
except Exception as e:
    print(f"❌ ERROR starting Hikka: {e}", flush=True)
    traceback.print_exc()
    sys.exit(1)
