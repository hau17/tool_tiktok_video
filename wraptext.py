import textwrap
from PIL import ImageFont

def soft_wrap_text(
    text: str, 
    fontsize: int, 
    letter_spacing: int, 
    font_family: str, 
    max_width: int,
):
    # Note that font_family has to be an absolut path to your .ttf/.otf
    image_font = ImageFont.truetype(font_family, fontsize) 

    # I am not sure my letter spacing calculation is accurate
    text_width = image_font.getlength(text) + (len(text)-1) * letter_spacing 
    letter_width = text_width / len(text)

    if text_width < max_width:
        return text

    max_chars = max_width / letter_width
    wrapped_text = textwrap.fill(text, width=max_chars)
    return wrapped_text
