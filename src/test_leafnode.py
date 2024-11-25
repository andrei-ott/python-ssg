import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_values(self):
        props = { "href": "url", "target": "_blank" }
        a_node = LeafNode("a", "This is a link", props)

        self.assertEqual(a_node.tag, "a")
        self.assertEqual(a_node.value, "This is a link")
        self.assertEqual(a_node.children, None)
        self.assertEqual(a_node.props, props)

    def test_to_html(self):
        a_node = LeafNode("a", "This is a link", { "href": "url", "target": "_blank" })

        self.assertEqual(a_node.to_html(), "<a href=\"url\" target=\"_blank\">This is a link</a>")

    def test_to_html_without_tag(self):
        node = LeafNode(None, "This is a link")

        self.assertEqual(node.to_html(), "This is a link")

    def test_to_html_value_error(self):
        node = LeafNode(None, None)

        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    unittest.main()