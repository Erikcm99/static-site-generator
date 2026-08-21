import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_header(self):
        header= """# test"""
        result = markdown_to_html_node(header)
        self.assertEqual("<div><h1>test</h1></div>",result.to_html())

    def test_paragraphs(self):
        md = """
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with _italic_ text and `code` here

            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        correct = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        print(f"\n\n\nASSERTEQUAL CORRECT: {correct}\n\n\n")
        print(f"\n\n\nASSERTEQUAL TEST: {html}\n\n\n")
        self.assertEqual(
            html,
            correct,
        )

    def test_quote(self):
        md = """
        > The mountains are calling
        > and I must go
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        correct = "<div><blockquote>The mountains are calling and I must go</blockquote></div>"
        print(f"\n\n\nASSERTEQUAL CORRECT: {correct}\n\n\n")
        print(f"\n\n\nASSERTEQUAL TEST: {html}\n\n\n")
        self.assertEqual(
            html,
            correct,
        )

    def test_ul(self):
        md = """
        - The mountains are calling
        - and I must go
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        correct = "<div><ul><li>The mountains are calling</li><li>and I must go</li></ul></div>"
        print(f"\n\n\nASSERTEQUAL CORRECT: {correct}\n\n\n")
        print(f"\n\n\nASSERTEQUAL TEST: {html}\n\n\n")
        self.assertEqual(
            html,
            correct,
        )

    def test_ol(self):
        md = """
        1. The mountains are calling
        2. and I must go
        3. forever
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        correct = "<div><ol><li>The mountains are calling</li><li>and I must go</li><li>forever</li></ol></div>"
        print(f"\n\n\nASSERTEQUAL CORRECT: {correct}\n\n\n")
        print(f"\n\n\nASSERTEQUAL TEST: {html}\n\n\n")
        self.assertEqual(
            html,
            correct,
        )

if __name__ == '__main__':
    unittest.main()
