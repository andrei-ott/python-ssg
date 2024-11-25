from textnode import *
import re


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)

    return nodes


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


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            splitted_texts = re.split(r"(?<!!)\[(.*?)\]\((.*?)\)", node.text)
            
            splitted_nodes = []
            link_text = ""
            for i in range(0, len(splitted_texts)):
                text = splitted_texts[i]
                if len(text) == 0:
                    continue

                if i % 3 == 0:
                    splitted_nodes.append(TextNode(text, TextType.NORMAL))
                elif i % 3 == 1:
                    link_text = text
                else:
                    splitted_nodes.append(TextNode(link_text, TextType.LINK, text))
            new_nodes.extend(splitted_nodes)
    
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            splitted_texts = re.split(r"!\[(.*?)\]\((.*?)\)", node.text)
            
            splitted_nodes = []
            image_text = ""
            for i in range(0, len(splitted_texts)):
                text = splitted_texts[i]
                if len(text) == 0:
                    continue

                if i % 3 == 0:
                    splitted_nodes.append(TextNode(text, TextType.NORMAL))
                elif i % 3 == 1:
                    link_text = text
                else:
                    splitted_nodes.append(TextNode(link_text, TextType.IMAGE, text))
            new_nodes.extend(splitted_nodes)
    
    return new_nodes