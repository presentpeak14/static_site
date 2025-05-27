from enum import Enum

class TextType(Enum):
    normal = "normal"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        if self.text == target.text and self.text_type == target.text_type and self.url == target.url:
            return True
        return False
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")