import PySimpleGUI as sg

layout = [
  [sg.Text('表示したい文字列',text_color='Red')],
  [sg.Text('表示したい文字列',text_color='Cyan')],
  [sg.Text('表示したい文字列',text_color='Green')],
  [sg.Text('表示したい文字列',text_color='magenta')]
]

window = sg.Window('Text_Color',layout,size=(300,150),finalize=True)

while True:
  event,values = window.read() # イベントの入力を待つ

  if event == sg.WIN_CLOSED or event == 'Exit':
    break

window.close()