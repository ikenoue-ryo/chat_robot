<h2>対話側ロボット</h2>
main.pyを実行するとスクリプトで実行されます。

<h2>APIキーについて</h2>
<p>ルートディレクトリに.envファイルを作成し、
APIキーを取得後以下のように記載ください。
</p>

<p>.envファイル内------------------------------------</p>
<p>API_KEY=ここにopenweathermapのAPIキー
　#取得先：https://openweathermap.org/api</p>

<p>GNAVI_API_KEY=ここにぐるなびのAPIキー
　#取得先：https://api.gnavi.co.jp/api/</p>

<p>YOUTUBE_API_KEY=ここにYoutubeのAPIキー
　#取得先：Google Cloud Platform から YouTube Data API v3を取得</p>
<p>------------------------------------------------</p>

<h2>仕様</h2>
スクリプトで実行する便利な対話型ロボットです。
ユーザーのinputを受け付けてユーザーリクエストに応じた処理を返します。


<h2>現在の機能</h2>
<ul>
<li>時間によってロボットが挨拶を変更する</li>
<li>天気予報を知らせる</li>
<li>ぐるなびAPIからレストランを紹介する</li>
<li>友達のプロフィールを表示する（ユーザーが閲覧したいプロフィールを選択）</li>
<li>ロボットが新規ユーザーに質問してプロフィールを作成する</li>
<li>YoutubeAPIから動画検索できる</li>
</ul>


<h2>実行結果画面</h2>
<img src="https://user-images.githubusercontent.com/61681360/83609690-95dc5880-a5b9-11ea-895e-34a1a818e0a3.png">
<img src="https://user-images.githubusercontent.com/61681360/83610021-f79cc280-a5b9-11ea-8845-335757845258.png">
<img src="https://user-images.githubusercontent.com/61681360/83610208-156a2780-a5ba-11ea-9f96-ba523292533d.png">
<img src="https://user-images.githubusercontent.com/61681360/83610274-287cf780-a5ba-11ea-9ffa-5c574a9fae04.png">


<h2>直近で導入したい機能について箇条書きする</h2>
<ul>
<li>質問した内容を保存していく</li>
<li>ランダムに質問を表示してデータを蓄積していく（例：今日はご飯を食べましたか？）</li>
<li>ユーザーが住所を入力したら午後から雨が振りそうですと、予想する</li>
<li>もし気温が高かったら冷やし系のお店をランダムに提案（ぐるなびAPIのお店のリンク）</li>
<li>何かお探しですか？シリーズ　→ Google検索など</li>
<li>検索欄を作って検索にヒットしたものと根拠を表示　例:slack</li>
<li>スクレイピング</li>
<li>何回そのinputを取得したか回数のログを取りユーザー心理を分析する</li>
<li>matplotlibなどで集めたデータの可視化</li>
</ul>

<h2>将来的な案</h2>
<ul>
<li>起動と同時にsiriが読み上げる。</li>
<li>後々、機械学習に使える具体的なデータに仕上げる</li>
</ul>


