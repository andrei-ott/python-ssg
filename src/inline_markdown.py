from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            splitted_texts = node.text.split(delimiter)
            if len(splitted_texts) % 2 != 1:
                raise Exception("No closing delimiter")
            
            splitted_nodes = []
            for i in range(0, len(splitted_texts)):
                text = splitted_texts[i]
                if len(text) == 0:
                    continue

                if i % 2 == 0:
                    splitted_nodes.append(TextNode(text, TextType.NORMAL))
                else:
                    splitted_nodes.append(TextNode(text, text_type))
            new_nodes.extend(splitted_nodes)
    
    return new_nodes