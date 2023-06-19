import PySimpleGUI as sg
import random
sg.theme("DarkBrown3")

layout = [[sg.T("さあ、おみくじを引きましょう。")],
          [sg.Im("futaba0.png")],
          [sg.T(k="txt")],
          [sg.B(" おみくじを引く ", k="btn")]]
win = sg.Window("おみくじアプリ", layout, font=(None, 14))

def omikuji():
    kuji = ["大吉", "中吉", "小吉", "凶"]
    kekka = random.choice(kuji)
    txt = f"結果は、{kekka}でした。"
    win["txt"].update(txt)

while True:
    e, v = win.read()
    if e == "btn":
        omikuji()
    if e == None:
        break
win.close()