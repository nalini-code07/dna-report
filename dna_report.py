# DNA composition report for the learning lab.
# Ask for a sequence of A, C, G, T and print how much of each base it holds.


def build_report(sequence):
    # Tidy the text the student typed: drop spaces at the ends, ignore case.
    sequence = sequence.strip().upper()
    length = len(sequence)

    if length == 0:
        return "Error: the sequence is empty. Please type some letters A, C, G or T."

    a = sequence.count("A")
    c = sequence.count("C")
    g = sequence.count("G")
    t = sequence.count("T")

    # If every letter is A, C, G or T, the four counts add up to the length.
    if a + c + g + t != length:
        return "Error: the sequence may only contain the letters A, C, G and T."

    # "/" always gives a float in Python 3, even when both sides are integers.
    a_percent = a * 100 / length
    c_percent = c * 100 / length
    g_percent = g * 100 / length
    t_percent = t * 100 / length
    gc_percent = (g + c) * 100 / length

    lines = [
        f"A: {a} ({a_percent:.1f}%)",
        f"C: {c} ({c_percent:.1f}%)",
        f"G: {g} ({g_percent:.1f}%)",
        f"T: {t} ({t_percent:.1f}%)",
        f"Length: {length}, GC content: {gc_percent:.1f}%",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    print("Type a DNA sequence (letters A, C, G, T) and press Enter:")
    typed = input()
    print(build_report(typed))

