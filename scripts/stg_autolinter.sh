#!/bin/bash
# 🏛️ STG AUTO-LINTING PROTOCOL
# PURPOSE: CLEAN SYNTAX, NO DELETION.

echo "🧹 SCANNING FOR SYNTAX STAINS..."

# Merapikan file JSON (ABI & Metadata)
find . -name "*.json" -exec python3 -m json.tool {} --indent 2 \;

# Merapikan file Markdown (Akte & Log)
# Menghapus spasi berlebih di akhir baris
find . -name "*.md" -exec sed -i 's/[[:space:]]*$//' {} +

# Pengecekan Sintaks Python (Linter)
find . -name "*.py" -exec python3 -m py_compile {} \;

echo "✅ CLEANING COMPLETE. ALL REPOS ARE SHINING."
