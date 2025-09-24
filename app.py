"""
WP記事自動投稿システム - メインアプリケーション
フェーズ2: 基本的なFlaskアプリケーションの構築
"""

from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import logging
from datetime import datetime

# 環境変数を読み込む
load_dotenv()

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Flaskアプリケーションの初期化
app = Flask(__name__, template_folder='web', static_folder='web/static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

@app.route('/')
def index():
    """メインページを表示"""
    logger.info("メインページにアクセスされました")
    return render_template('main.html')

@app.route('/generate', methods=['POST'])
def generate_article():
    """記事生成のエンドポイント"""
    try:
        # リクエストからキーワードを取得
        data = request.get_json()
        keyword = data.get('keyword')
        
        if not keyword:
            logger.warning("キーワードが指定されていません")
            return jsonify({'error': 'キーワードを入力してください'}), 400
        
        logger.info(f"記事生成開始 - キーワード: {keyword}")
        
        # TODO: ここに記事生成のロジックを実装
        # 現在はテスト用のダミーレスポンス
        
        # テスト用のレスポンス
        response = {
            'status': 'success',
            'keyword': keyword,
            'post_id': 'test-001',
            'message': f'「{keyword}」の記事生成処理を開始しました（テストモード）',
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"記事生成完了（テスト） - キーワード: {keyword}")
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"記事生成エラー: {str(e)}")
        return jsonify({'error': f'エラーが発生しました: {str(e)}'}), 500

@app.route('/health')
def health_check():
    """ヘルスチェック用エンドポイント"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    # 開発サーバーを起動
    logger.info("Flask開発サーバーを起動します")
    app.run(
        host='0.0.0.0',  # 外部からアクセス可能にする
        port=5009,
        debug=True
    )