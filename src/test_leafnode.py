import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_to_html_multiple_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://boot.dev" target="_blank">Click me!</a>',
        )

    def test_to_html_no_tag_returns_raw_value(self):
        node = LeafNode(None, "Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")

    def test_to_html_no_value_raises(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_has_no_children(self):
        node = LeafNode("span", "text")
        self.assertIsNone(node.children)

    def test_props_to_html_none(self):
        node = LeafNode("p", "text")
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
