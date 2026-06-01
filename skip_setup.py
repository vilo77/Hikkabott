import os
import sys

print("=" * 60, flush=True)
print("🚀 Starting Hikka userbot (Direct)...", flush=True)
print("=" * 60, flush=True)

# Cek env vars
required_vars = ['API_ID', 'API_HASH', 'STRING_SESSION']
missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    print(f"❌ ERROR: Missing: {', '.join(missing)}", flush=True)
    sys.exit(1)

print("✅ All env vars found", flush=True)

# JALANKAN HIKKA LANGSUNG (tanpa import)
os.execvp("python", ["python", "-m", "hikka"])
