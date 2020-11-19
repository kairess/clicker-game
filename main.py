from ursina import *

app = Ursina()

window.borderless = False
window.color = color._20

Text.default_font = '/System/Library/Fonts/AppleSDGothicNeo.ttc'

gold = 0
gold_text = Text(text=str(gold), x=-0.02, y=0.3, scale=2, background=True)
button = Button(text='1G', color=color.orange, x=-0.6, scale=0.2)

def button_click():
    global gold
    gold += 1

button.on_click = button_click

# 골드 자동 생성기
def auto_plus_gold(plus=1, interval=1):
    global gold
    gold += plus

    invoke(auto_plus_gold, plus, delay=interval)

def get_auto_gold(button, plus=1):
    global gold

    if gold >= button.cost:
        gold -= button.cost

        button.cost = int(button.cost * 1.2)
        button.upgrade += 1
        button.text = f'+{button.upgrade}\n{button.earn}G/초\n가격 {button.cost}G'

        invoke(auto_plus_gold, plus=plus, interval=1)

auto_settings = [
    {
        'cost': 10,
        'earn': 1,
        'upgrade': 0,
    },
    {
        'cost': 100,
        'earn': 5,
        'upgrade': 0,
    },
    {
        'cost': 1000,
        'earn': 25,
        'upgrade': 0,
    },
    {
        'cost': 10000,
        'earn': 125,
        'upgrade': 0,
    },
]

auto_buttons = []

for i, setting in enumerate(auto_settings):
    b = Button(
        text=f'{setting["earn"]}G/초\n가격 {setting["cost"]}G',
        x=(0.3 * (i+1) - 0.6), scale=0.2,
        disabled=True,
        cost=setting['cost'],
        earn=setting['earn'],
        upgrade=setting['upgrade']
    )

    b.on_click = Func(get_auto_gold, b, b.earn)

    auto_buttons.append(b)

def update():
    global gold

    gold_text.text = str(gold)

    for button in auto_buttons:
        if gold >= button.cost:
            button.disabled = False
            button.color = color.green
            button.text_color = color.black
        else:
            button.disabled = True
            button.color = color.gray
            button.text_color = color.white

app.run()