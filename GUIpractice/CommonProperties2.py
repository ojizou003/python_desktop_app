import PySimpleGUI as sg

layout = [
  [sg.Text('オリジナルテキスト')],
  [sg.Text('_'*100)],
  [sg.Text('テキスト1',pad=(50,0),visible=False)],
  [sg.Text('_'*100)],
  [sg.Button('ボタン1',key=('-Btn1-'))],
  [sg.Text('_'*100)],
  [sg.Button('ボタン2',key=('-Btn2-'),disabled=True,disabled_button_color=('red',''))],
  [sg.Text('_'*100)]
]

window = sg.Window('ウィジェット無効化',layout,finalize=True)

while True:
  event,values = window.read() # イベントの入力を待つ

  if event =='-Btn1-':
    window['-Btn2-'].Update(disabled=False)

  if event == sg.WIN_CLOSED or event == 'Exit':
    break

window.close()