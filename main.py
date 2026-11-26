import flet as ft
import random

def main(page: ft.Page):
    state = {"s": 0, "ok": 0, "ans": 0}
    txt = ft.Text(size=40)
    inp = ft.TextField(label="Ответ")

    def go(e):
        if state["s"] > 0 and inp.value == str(state["ans"]):
            state["ok"] += 1
        state["s"] += 1
        if state["s"] > 5:
            txt.value = f"Итог: {state['ok']}/5"
            page.update()
            return
        a, b = random.randint(1, 10), random.randint(1, 10)
        state["ans"] = a + b
        txt.value = f"{a} + {b} = ?"
        inp.value = ""
        page.update()

    page.add(txt, inp, ft.ElevatedButton("ОК", on_click=go))
    go(None)

ft.run(main)
