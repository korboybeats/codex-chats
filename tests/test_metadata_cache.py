import importlib.machinery
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock


def load_codex_chats():
    loader = importlib.machinery.SourceFileLoader(
        "codex_chats_under_test", str(Path(__file__).resolve().parents[1] / "codex-chats")
    )
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


class MetadataCacheTests(unittest.TestCase):
    def test_parse_one_chat_reuses_persistent_cache_for_unchanged_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sessions = root / "sessions"
            sessions.mkdir()
            cache_file = root / "metadata-cache.json"
            path = sessions / "rollout-2026-05-15T00-00-00-019e0000-0000-7000-8000-000000000001.jsonl"
            cwd = str(root / "project")
            path.write_text(
                "\n".join(
                    [
                        json.dumps(
                            {
                                "timestamp": "2026-05-15T00:00:00.000Z",
                                "type": "session_meta",
                                "payload": {
                                    "id": "019e0000-0000-7000-8000-000000000001",
                                    "cwd": cwd,
                                    "timestamp": "2026-05-15T00:00:00.000Z",
                                },
                            }
                        ),
                        json.dumps(
                            {
                                "timestamp": "2026-05-15T00:01:00.000Z",
                                "type": "response_item",
                                "payload": {
                                    "type": "message",
                                    "role": "user",
                                    "content": [{"type": "input_text", "text": "hello cached world"}],
                                },
                            }
                        ),
                    ]
                )
                + "\n"
            )

            cc = load_codex_chats()
            cc.SESSION_ROOT = sessions
            cc.METADATA_CACHE = cache_file
            cc._SESSION_METADATA_CACHE = None
            cc._METADATA_CACHE_DIRTY = False

            first = cc.parse_one_chat(path)
            self.assertEqual(first["message"], "hello cached world")
            cc._save_metadata_cache()
            self.assertTrue(cache_file.exists())

            cc = load_codex_chats()
            cc.SESSION_ROOT = sessions
            cc.METADATA_CACHE = cache_file
            cc._SESSION_METADATA_CACHE = None
            cc._METADATA_CACHE_DIRTY = False

            with mock.patch.object(cc, "_parse_one_chat_uncached", side_effect=AssertionError("cache miss")):
                second = cc.parse_one_chat(path)

            self.assertEqual(second["message"], "hello cached world")
            self.assertEqual(second["cwd"], cwd)


if __name__ == "__main__":
    unittest.main()
