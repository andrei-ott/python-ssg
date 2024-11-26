import re
from htmlnode import *
from inline_markdown import text_to_leafnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == block_type_paragraph:
            children.append(paragraph_to_node(block))
        elif block_type == block_type_heading:
            children.append(heading_to_node(block))
        elif block_type == block_type_code:
            children.append(code_to_node(block))
        elif block_type == block_type_quote:
            children.append(quote_to_node(block))
        elif block_type == block_type_olist:
            children.append(olist_to_node(block))
        elif block_type == block_type_ulist:
            children.append(ulist_to_node(block))
            

    return ParentNode("div", children)

def paragraph_to_node(block):
    lines = block.split("\n")
    return ParentNode("p", text_to_leafnodes(" ".join(lines)))

def heading_to_node(block):
    header_start = re.findall(r"^#{1,6}", block)[0]
    tag = "h" + str(len(header_start))

    text = block[(len(header_start) + 1):]
    return ParentNode(tag, text_to_leafnodes(text))

def code_to_node(block):
    text = block[4:-3]
    return ParentNode("pre", [ParentNode("code", text_to_leafnodes(text))])

def quote_to_node(block):
    lines = block.split("\n")
    text = " ".join(map(lambda l: l[2:], lines))
    return ParentNode("blockquote", text_to_leafnodes(text))

def olist_to_node(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        text = line.split(". ", 1)[1]
        children.append(ParentNode("li", text_to_leafnodes(text)))
    return ParentNode("ol", children)

def ulist_to_node(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        children.append(ParentNode("li", text_to_leafnodes(line[2:])))
    return ParentNode("ul", children)


def markdown_to_blocks(markdown):
    splitted_blocks = markdown.split("\n\n")

    formatted_blocks = []
    for block in splitted_blocks:
        if block == "":
            continue
        formatted_blocks.append(block.strip())
    
    return formatted_blocks

def block_to_block_type(block):
    if re.match(r"^#{1,6} .+", block):
        return "heading"
    
    if re.match(r"^```.*```$", block, re.DOTALL):
        return "code"
    
    lines = block.split("\n")

    is_quote = True

    is_unordered_list = True
    unorder_list_symbol = None

    is_ordered_list = True
    ordered_list_num = 1

    for i, line in enumerate(lines):
        if line[0] != ">":
            is_quote = False

        if i == 0:
            if line[0] == "*":
                unorder_list_symbol = "*"
            else:
                unorder_list_symbol = "-"
        
        if len(line) < 2 or line[0] != unorder_list_symbol or  line[1] != " ":
            is_unordered_list = False
        
        if  len(line) < 3 or line[0] != str(ordered_list_num) or line[1] != "." or line[2] != " ":
            is_ordered_list = False
        ordered_list_num += 1
    
    if is_quote:
        return "quote"
    if is_unordered_list:
        return "unordered_list"
    if is_ordered_list:
        return "ordered_list"
    return "paragraph"