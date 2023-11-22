from Audiobook import (  # noqa
    extract_from_pdf,
    extract_from_txt,
    extract_text,
    convert_text_to_speech,
)

# def test_extract_from_pdf():

#     #result = extract_from_pdf('D:\work\Audiobook\Audiobook\script.pdf')
#     #expected = open("script.txt", "r")

#     result = extract_from_pdf('D:\work\Audiobook\Audiobook\script.pdf').replace('\n', ' ').strip() # noqa
#     expected = open("script.txt", "r").replace('\n', ' ').strip()

#     print("Result:", result)
#     print("Expected:", expected)
#     assert result == expected.read()


def test_extract_from_txt():
    result = extract_from_txt(r"D:\work\Audiobook\Audiobook\script.txt")
    expected = open("script.txt", "r")
    assert result == expected.read()


def test_extract_text():
    result = extract_text(r"D:\work\Audiobook\Audiobook\script.txt")
    expected = open("script.txt", "r")
    assert result == expected.read()


# def test_convert_text_to_speech():
#     Mock the pyttsx3 library or use Pytest fixtures for more complex scenarios # noqa
#     pass
