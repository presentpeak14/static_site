from htmlnode import HTMLNode, LeafNode

def test_props_to_html_basic():
    node = HTMLNode(props={"href": "https://www.google.com"})
    expected_output = ' href="https://www.google.com"'
    assert node.props_to_html() == expected_output

def test_props_to_html_empty_list():
    node = HTMLNode(props={})
    expected_output = ''
    assert node.props_to_html() == expected_output

def test_props_to_html_no_list():
    node = HTMLNode()
    expected_output = None
    assert node.props_to_html() == expected_output

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")