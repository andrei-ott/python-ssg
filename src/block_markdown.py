import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    splitted_blocks = markdown.split("\n\n")

    formatted_blocks = []
    for block in splitted_blocks:
        if block == "":
            continue

        lines = block.split("\n")
        new_block = ""
        for line in lines:
            new_block += line.strip() + "\n"

        formatted_blocks.append(new_block.strip("\n"))
    
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