# TinyFish CLI wrapper (26/11/2026): parse JSON, discover TikTok links, degrade quietly without the binary.
import importlib.util, json, os, subprocess, types
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec_ = importlib.util.spec_from_file_location("tinyfish_client", os.path.join(R, "pipeline/scripts/tinyfish_client.py"))
tf = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(tf)

SEARCH = {"results": [
    {"title": "Thói quen nhỏ", "url": "https://tiktok.com/@abc.xyz/video/7500043731798658312", "snippet": "ngâm chân", "date": "2025-05-03T02:40:15Z"},
    {"title": "dup", "url": "https://www.tiktok.com/@abc.xyz/video/7500043731798658312?lang=vi", "snippet": ""},
    {"title": "not a clip", "url": "https://www.tiktok.com/@abc.xyz", "snippet": ""}]}

def fake_run(payload, code=0):
    def run(args, **kw):
        return types.SimpleNamespace(returncode=code, stdout=json.dumps(payload), stderr="")
    return run

def test_tiktok_discover_dedupes_and_parses(monkeypatch, tmp_path):
    exe = tmp_path / "tinyfish"; exe.write_text("#!/bin/sh\n"); monkeypatch.setattr(tf.P, "TINYFISH_BIN", str(exe))
    monkeypatch.setattr(subprocess, "run", fake_run(SEARCH))
    c = tf.tiktok_discover(["thói quen"])
    assert len(c) == 1 and c[0]["creator"] == "abc.xyz" and c[0]["video_id"] == "7500043731798658312"
    assert c[0]["url"] == "https://www.tiktok.com/@abc.xyz/video/7500043731798658312"

def test_fetch_marks_blocked(monkeypatch, tmp_path):
    exe = tmp_path / "tinyfish"; exe.write_text(""); monkeypatch.setattr(tf.P, "TINYFISH_BIN", str(exe))
    monkeypatch.setattr(subprocess, "run", fake_run({"results": [{"url": "u", "title": "Site Maintenance", "text": "Oops"}]}))
    assert tf.fetch(["u"])[0]["blocked"] is True

def test_missing_binary_returns_empty(monkeypatch):
    monkeypatch.setattr(tf.P, "TINYFISH_BIN", "/nope/tinyfish")
    assert tf.search("x") == [] and tf.tiktok_discover(["x"]) == []

def test_nonzero_exit_returns_empty(monkeypatch, tmp_path):
    exe = tmp_path / "tinyfish"; exe.write_text(""); monkeypatch.setattr(tf.P, "TINYFISH_BIN", str(exe))
    monkeypatch.setattr(subprocess, "run", fake_run({}, code=1))
    assert tf.search("x") == []
