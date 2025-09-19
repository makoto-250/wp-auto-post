#!/usr/bin/env python3
import sys
import os

print("="*50)
print("WP自動投稿システム - 環境構築確認")
print("="*50)

print(f"\n✓ Python version: {sys.version}")

# ライブラリのチェック
libraries = [
    ('flask', 'Flask'),
    ('requests', 'Requests'),
    ('bs4', 'BeautifulSoup4'),
    ('MeCab', 'MeCab'),
    ('anthropic', 'Anthropic'),
    ('googleapiclient', 'Google API Client'),
    ('serpapi', 'SerpAPI'),
    ('dotenv', 'python-dotenv'),
]

print("\n✓ インストール済みライブラリ:")
for module_name, display_name in libraries:
    try:
        __import__(module_name)
        print(f"  ✓ {display_name}")
    except ImportError:
        print(f"  ✗ {display_name} - Not installed")

# MeCabの動作確認
try:
    import MeCab
    mecab = MeCab.Tagger()
    result = mecab.parse("テスト")
    print("\n✓ MeCab動作確認: OK")
except Exception as e:
    print(f"\n✗ MeCab動作確認: Error - {e}")

# ファイル構造の確認
print("\n✓ プロジェクト構造:")
files = ['app.py', '.env', '.gitignore', 'requirements.txt']
dirs = ['web', 'prompt', 'venv']

for f in files:
    if os.path.exists(f):
        print(f"  ✓ {f}")
    else:
        print(f"  ✗ {f} - 未作成")

for d in dirs:
    if os.path.exists(d):
        print(f"  ✓ {d}/")
    else:
        print(f"  ✗ {d}/ - 未作成")

print("\n✅ フェーズ1完了！次はフェーズ2（WebUIの作成）に進みます。")
