import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is another text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.BOLD, "url")

        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "url1")
        node2 = TextNode("This is a text node", TextType.BOLD, "url2")

        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://www.boot.dev")
        
        self.assertEqual(
            "TextNode(This is a text node, normal, https://www.boot.dev)", repr(node)
        )

    def test_text_node_to_html_node(self):
        text = "This is a text node"
        node = TextNode(text, TextType.NORMAL)
        self.assertEqual(
            text_node_to_html_node(node).to_html(), text
        )

        node = TextNode(text, TextType.BOLD)
        self.assertEqual(
            text_node_to_html_node(node).to_html(), f'<b>{text}</b>'
        )

        node = TextNode(text, TextType.ITALIC)
        self.assertEqual(
            text_node_to_html_node(node).to_html(), f'<i>{text}</i>'
        )

        node = TextNode(text, TextType.CODE)
        self.assertEqual(
            text_node_to_html_node(node).to_html(), f'<code>{text}</code>'
        )

        link = "https://www.boot.dev"
        node = TextNode(text, TextType.LINK, link)
        self.assertEqual(
            text_node_to_html_node(node).to_html(), f'<a href="{link}">{text}</a>'
        )

        node = TextNode(text, TextType.IMAGE, link)
        self.assertEqual(
            text_node_to_html_node(node).to_html(), f'<img src="{link}" alt="{text}"></img>'
        )


if __name__ == "__main__":
    unittest.main()