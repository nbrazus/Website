import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_single_child(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(
            parent.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child], {"class": "container", "id": "main"})
        self.assertEqual(
            parent.to_html(),
            '<div class="container" id="main"><span>child</span></div>',
        )

    def test_to_html_no_tag_raises(self):
        parent = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_no_children_raises(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_nested_parents(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode(None, "first")]),
                ParentNode("p", [LeafNode("b", "second")]),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><p>first</p><p><b>second</b></p></div>",
        )

    def test_parent_value_is_none(self):
        parent = ParentNode("div", [LeafNode("span", "child")])
        self.assertIsNone(parent.value)


if __name__ == "__main__":
    unittest.main()
