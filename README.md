# 「世界一やさしいPython デスクトップアプリ開発のはじめ方」 NSシステムズ 著

2023/9/30 ~ 9/30  

## Anaconda のインストール

## VS Code のインストール

## 仮想環境の構築

```conda create -n GUIenv python=3.11```  
```conda activate GUIenv```  

## 各種パッケージ・ライブラリーのインストール

- PySimpleGUi
- openpyxl
- pyqrcode ..python3.9までの対応
- qrcode
- pypng

## デバッグ

## ファイル操作

pathlibモジュール  

- Path.cwd() ..カレントディレクトリを取得
- Path.open() ..ファイルを開く
- Path.read_text() ..テキストファイルを読み込む
- Path.write_text() ..テキストファイルを書き込み作成
- Path.unlink() ..ファイルを削除
- Path.mkdir() ..フォルダを作成

エクセル操作の基本  

xlwings と openpyxl  
openpyxl のメソッド  

- wb = openpyxl.load_workbook(path)
- ws = wb['sheet1']
- wb.save['path']
- wb = openpyxl.Workbook()
- ws.title = 'ワークシート名'
- ws.cell(row='行番号',column='列番号').value
- ws['セル番地'].value
- ws.cell(row='行番号',column='列番号',value='値')

Exel ファイルの新規作成  

## GUI アプリの基本  

PySimpleGUI  
その他の GUI ライブラリ

- Tkinter ..標準搭載 シンプル
- PyQt ..モダン Android、iOS対応
- Kivy ..ゲームに強い Android、iOS対応
- wxPython ..機能充実

GUI アプリ開発の流れ

1. レイアウトの設定 ..ウィジェットの配置
2. ウィンドウの設定
3. イベントの設定
4. ウインドウのクローズ

```python
layout = [
  [sg.Text('テキストを表示します')],
  [sg.InputText()],
  [sg.Button('ボタン1')]
]
```

```python
window = sg.Window('window のタイトル'),
layout,finalize=True
```

```python
while True:
  event,values = window.read() # イベントの入力を待つ
  if event == sg.WIN_CLOSED or event == 'Exit':
    break
```

ウィジェット共通設定  

- テキストカラーの設定
- テキストフォント、フォントサイズの設定
- テキストエリアのサイズ設定 ..sg.Text(size=(文字数(半角),行数))
- 背景色の設定
- 位置の設定 ..pad=(left/right,top/bottom)
- 表示、非表示の設定 ..visible
- ウィジェットの無効化の設定 ..disabled

各種ウィジェットのプロパティと使い方  

- Text(テキスト)
- Input(インプット)
---
kindleUnlimited 解約 __ここまで