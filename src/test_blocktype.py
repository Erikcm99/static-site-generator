import unittest
from blocktype import block_to_block_type, BlockType


class TestTextNode(unittest.TestCase):
    def test_heading(self):
        node = '''# sdfasdf'''
        blockType = block_to_block_type(node) 
        self.assertEqual(blockType, BlockType.HEADING)
    def test_heading2(self):
        node = '''# sdfasdf\n'''
        blockType = block_to_block_type(node) 
        self.assertEqual(blockType, BlockType.PARAGRAPH)
    def test_code(self):
        node = '''```\nasdjfahsdkfjasd```'''
        blockType = block_to_block_type(node) 
        self.assertEqual(blockType, BlockType.CODE)
    def test_quote(self):
        node = '''>alsdkjflasd\n> afsodfijadsof\n>lsdfkjal'''
        blockType = block_to_block_type(node) 
        self.assertEqual(blockType, BlockType.QUOTE)
    def test_unorderedList(self):
        node = '''- asdifjasldfja\n- afsodfijadsof\n- sdfkjal'''
        blockType = block_to_block_type(node) 
        self.assertEqual(blockType, BlockType.UNORDERED_LIST)
    def test_orderedList(self):
        node = '''1. aosdifh\n2. fiasjdfldsof\n3. iasdjf'''
        blockType = block_to_block_type(node) 
        self.assertEqual(blockType, BlockType.ORDERED_LIST)
    def test_orderedList2(self):
        node = '''2. aosdifh\n2. fiasjdfldsof\n3. iasdjf'''
        blockType = block_to_block_type(node) 
        self.assertEqual(blockType, BlockType.PARAGRAPH)
    def test_orderedList3(self):
        node = '''1. aosdifh\n3. fiasjdfldsof\n3. iasdjf'''
        blockType = block_to_block_type(node) 
        self.assertEqual(blockType, BlockType.PARAGRAPH)
if __name__ == "__main__":
    unittest.main()
