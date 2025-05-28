from htmlnode import HTMLNode

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