import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        p_node = HTMLNode("p", "This is a paragraph", None, None)
        props = { "href": "url", "target": "_blank" }
        a_node = HTMLNode("a", "This is a link", [p_node], props)

        self.assertEqual(a_node.tag, "a")
        self.assertEqual(a_node.value, "This is a link")
        self.assertEqual(a_node.children, [p_node])
        self.assertEqual(a_node.props, props)

    def test_props_to_html(self):
        node = HTMLNode("a", "This is a link", None, { "href": "url", "target": "_blank" })

        self.assertEqual(node.props_to_html(), " href=\"url\" target=\"_blank\"")

    def test_repr(self):
        p_node = HTMLNode("p", "This is a paragraph", None, None)
        a_node = HTMLNode("a", "This is a link", [p_node], { "href": "url", "target": "_blank" })
        
        self.assertEqual(repr(a_node), "HTMLNode(a, This is a link, [HTMLNode(p, This is a paragraph, None, None)], {'href': 'url', 'target': '_blank'})")


if __name__ == "__main__":
    unittest.main()