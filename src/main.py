from textnode import TextNode, TextType

def main():
    text_node1 = TextNode("This is some anchor text", TextType.link, "https://www.boot.dev")
    print(text_node1)

main()