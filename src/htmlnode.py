class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_HTML(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        new_props = []
        for key, value in self.props.items():
            # Now you have the key and the value for each property
            new_props.append(f' {key}="{value}"')
        return "".join(new_props)
    
    def __repr__(self):
        return(f"{self.tag}, {self.value}, {self.children}, {self.props}")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"