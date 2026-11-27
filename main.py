import flet as ft
import random

def main(page: ft.Page):
    page.title = "Unitatry"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    state = {"s": 0, "ok": 0, "ans": 0}
    txt = ft.Text(size=40, weight=ft.FontWeight.BOLD)
    inp = ft.TextField(
        label="Ответ",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=200,
        text_align=ft.TextAlign.CENTER,
    )

    def go(e):
        if state["s"] > 0 and inp.value.strip() == str(state["ans"]):
            state["ok"] += 1
        state["s"] += 1
        if state["s"] > 5:
            txt.value = f"Итог: {state['ok']}/5"
            inp.visible = False
            btn.visible = False
            page.update()
            return
        a, b = random.randint(1, 10), random.randint(1, 10)
        state["ans"] = a + b
        txt.value = f"{a} + {b} = ?"
        inp.value = ""
        page.update()

    inp.on_submit = go
    btn = ft.Button(content="ОК", on_click=go)

    page.add(txt, inp, btn)
    go(None)

ft.run(main)
