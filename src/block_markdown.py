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