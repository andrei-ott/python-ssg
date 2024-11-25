import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_values(self):
        children = [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        node = ParentNode(
            "p",
            children,
        )

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, None)

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_value_error(self):
        node1 = ParentNode(None, None)
        node2 = ParentNode("p", None)

        self.assertRaises(ValueError, node1.to_html)
        self.assertRaises(ValueError, node2.to_html)

    def test_to_html_deep_nested(self):
        leaf_node1 = LeafNode("b", "Bold text")
        leaf_node2 = LeafNode("a", "This is a link", { "href": "url", "target": "_blank" })
        leaf_node3 = LeafNode(None, "Normal text")
        leaf_node4 = LeafNode("i", "italic text")

        node = ParentNode(
            "section",
            [
                leaf_node1,
                ParentNode(
                    "div",
                    [
                        leaf_node2,
                        ParentNode(
                            "p",
                            [leaf_node3]
                        )
                    ]
                ),
                leaf_node4
            ],
            { "class": "flex" }
        )

        self.assertEqual(node.to_html(), '<section class="flex"><b>Bold text</b><div><a href="url" target="_blank">This is a link</a><p>Normal text</p></div><i>italic text</i></section>')


if __name__ == "__main__":
    unittest.main()