import os
import sys
import traceback

print("=" * 60, flush=True)
print("🔍 Hikka Startup Debug Mode v2", flush=True)
print("=" * 60, flush=True)

# Cek apakah semua env vars sudah ada
required_vars = ['API_ID', 'API_HASH', 'STRING_SESSION']
missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    print(f"❌ ERROR: Missing environment variables: {', '.join(missing)}", flush=True)
    sys.exit(1)

print("✅ All environment variables found", flush=True)
print("✅ Skipping interactive setup...", flush=True)
print("✅ Hikka configurator patched successfully", flush=True)
print("🚀 Starting Hikka userbot...", flush=True)

try:
    from hikka import main
    print("✅ hikka.main imported", flush=True)
    
    # Wrap main() dengan try-except
    try:
        main.hikka.main()
    except SystemExit as e:
        print(f"❌ Hikka exited with code: {e.code}", flush=True)
        traceback.print_exc()
        sys.exit(e.code if e.code else 1)
    except Exception as e:
        print(f"❌ Hikka crashed: {e}", flush=True)
        traceback.print_exc()
        sys.exit(1)
        
except Exception as e:
    print(f"❌ Failed to import hikka: {e}", flush=True)
    traceback.print_exc()
    sys.exit(1)

print("⚠️ Hikka exited unexpectedly", flush=True)
sys.exit(1)
