import PySimpleGUI as sg

layout = [
  [sg.Text('オリジナルテキスト')],
  [sg.Text('_'*100)],
  [sg.Text('テキスト1',pad=(50,0),visible=False)],
  [sg.Text('_'*100)],
  [sg.Text('テキスト2',pad=(150,100),visible=False)],
  [sg.Text('_'*100)],
  [sg.Text('テキスト3',pad=((50,200),(0,100)),visible=True)],
  [sg.Text('_'*100)]
]

window = sg.Window('ウィジェットの表示・非表示設定',layout,finalize=True)

while True:
  event,values = window.read() # イベントの入力を待つ

  if event == sg.WIN_CLOSED or event == 'Exit':
    break

window.close()