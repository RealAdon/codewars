# Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.

# Here are the rules:

#     Use spaces to fill in the gaps between words.
#     Each line should contain as many words as possible.
#     Use '\n' to separate lines.
#     Gap between words can't differ by more than one space.
#     Lines should end with a word not a space.
#     '\n' is not included in the length of a line.
#     Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
#     Last line should not be justified, use only one space between words.
#     Last line should not contain '\n'
#     Strings with one word do not need gaps ('somelongword\n').

# Example with width=30:

# Lorem  ipsum  dolor  sit amet,
# consectetur  adipiscing  elit.
# Vestibulum    sagittis   dolor
# mauris,  at  elementum  ligula
# tempor  eget.  In quis rhoncus
# nunc,  at  aliquet orci. Fusce
# at   dolor   sit   amet  felis
# suscipit   tristique.   Nam  a
# imperdiet   tellus.  Nulla  eu
# vestibulum    urna.    Vivamus
# tincidunt  suscipit  enim, nec
# ultrices   nisi  volutpat  ac.
# Maecenas   sit   amet  lacinia
# arcu,  non dictum justo. Donec
# sed  quam  vel  risus faucibus
# euismod.  Suspendisse  rhoncus
# rhoncus  felis  at  fermentum.
# Donec lorem magna, ultricies a
# nunc    sit    amet,   blandit
# fringilla  nunc. In vestibulum
# velit    ac    felis   rhoncus
# pellentesque. Mauris at tellus
# enim.  Aliquam eleifend tempus
# dapibus. Pellentesque commodo,
# nisi    sit   amet   hendrerit
# fringilla,   ante  odio  porta
# lacus,   ut   elementum  justo
# nulla et dolor.

# Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).

# Have fun :)

# Solution:

def justify(text, width):
    words = text.split()
    lines = []
    current_line = []

    # Step 1 & 2: Split text into words and group them into lines
    current_length = 0
    for word in words:
        if current_length + len(word) + len(current_line) > width:
            lines.append(current_line)
            current_line = []
            current_length = 0
        current_line.append(word)
        current_length += len(word)
    lines.append(current_line)  # Add the last line

    # Step 3: Justify lines except the last
    for i in range(len(lines) - 1):
        line = lines[i]
        spaces_needed = width - sum(len(word) for word in line)
        if len(line) == 1:
            justified_line = line[0] + ' ' * spaces_needed
        else:
            spaces = [(spaces_needed // (len(line) - 1)) + (1 if x < spaces_needed % (len(line) - 1) else 0) for x in range(len(line) - 1)]
            justified_line = ''.join(word + (' ' * space) for word, space in zip(line, spaces + [0]))
        lines[i] = justified_line.strip()

    # Step 4: Handle the last line
    lines[-1] = ' '.join(lines[-1])

    return '\n'.join(lines)

# Example usage
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor."
width = 30

# Call the justify function
justified_text = justify(text, width)
print(justified_text)
