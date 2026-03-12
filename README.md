# codex-chats

Interactive, fzf-driven browser for the Codex CLI session archive (`~/.codex/sessions`). It mirrors the feel of `claude-chats` by listing sessions, showing previews, and mapping keys to common actions.

## Features

- `fzf` picker with header hints, live preview, and shortcut bindings.
- Preview shows the full conversation (scrollable in the preview pane).
- Resume by session ID, rename chats (local overlay), and purge empty sessions.
- Optional AI summaries (Gemini) with cached results.

## Getting started

## Requirements

- Python 3.7+
- `fzf`
- Codex CLI (`codex`) in PATH

## Install (WSL / Linux)

```bash
git clone <this-repo>
cd codex-chats
./install.sh
```

By default it installs to `~/.local/bin/codex-chats`. Make sure `~/.local/bin` is in your `PATH`.

## Install (Windows native)

Requirements:
- Python 3.7+ (in PATH)
- `fzf` in PATH (Scoop: `scoop install fzf`, or Chocolatey: `choco install fzf`)
- `codex` in PATH

```powershell
git clone <this-repo>
cd codex-chats
.\install.ps1
```

This installs to `%USERPROFILE%\\bin` and adds it to your user PATH.

## Usage

```bash
codex-chats
```

## Keys

Project view:
- `Enter` open project
- `Ctrl-N` new session (in selected project)
- `Ctrl-F` create project folder
- `Ctrl-R` resume by session ID
- `Ctrl-E` open folder in file explorer
- `Ctrl-D` delete all chats in project (with confirmation)
- `Ctrl-X` purge empty chats across all projects
- `Ctrl-P` toggle perms mode (adds `--dangerously-bypass-approvals-and-sandbox`)
- `Esc` quit

Chats view:
- `Ent` resume highlighted chat
- `Ctrl-N` new session
- `Ctrl-S` toggle AI summaries (Gemini)
- `Ctrl-R` rename chat (local title overlay)
- `Ctrl-D` delete selected chats
- `Ctrl-X` purge empty chats
- `Ctrl-P` toggle perms mode
- `Backspace` back to project list
- `Ctrl-C` exit

## Notes

- Renames are stored locally in `~/.codex/codex-chats-titles.json`.
- AI summaries use your Gemini API key stored at `~/.gemini_api_key`.
