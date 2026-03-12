#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${1:-$HOME/.local/bin}"

mkdir -p "$TARGET_DIR"
install -m 0755 "$SCRIPT_DIR/codex-chats" "$TARGET_DIR/codex-chats"

echo "Installed to: $TARGET_DIR/codex-chats"

case ":$PATH:" in
  *":$TARGET_DIR:"*)
    ;;
  *)
    echo "Note: $TARGET_DIR is not in your PATH."
    echo "Add this to your shell config:"
    echo "  export PATH=\"$TARGET_DIR:\$PATH\""
    ;;
 esac
