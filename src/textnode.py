class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
        pass


    def __eq__(self, other):
            if self.text == other.text and self.text_type == other.text_type:
                return True
            if self.text_type == other.text_type and self.url == other.url:
                return True
            if self.url == other.url and self.text == other.text:
                return True


    def __repr__(self):
        return f"{self.text}, {self.text_type}, {self.url}"
