from Rabbit.Rendering.Manegers.ManagerStyleText import Maneger

maneger = Maneger()
def printf(text, color="defolt", light=False, backgraund="defolt", style=False, end=False, print_pr=True):
    """Печатает текст в разных стилях

        text = Сам текст
        color = Цвет текста
        light = Яркость текста
        backgraund = Фон текста
        style = Жирность текста  """

    new_text = ""

    new_text += maneger.maneger_color_text(color)
    new_text += maneger.maneger_light_text(color, light)
    new_text += maneger.maneger_backgraund_text(backgraund)
    new_text += maneger.manefer_style_text(style)

    new_text += str(text)

    if print_pr:
        if end:
            print(new_text, end="")
        else:
            print(new_text)

        return new_text
    else:
        return new_text