from translate import Translator

def translate_chinese_to_english(input_text):
    translator = Translator(to_lang="en", from_lang="zh")
    parts = input_text.split()

    # Initialize an empty list to store translated parts
    translated_parts = []

    for part in parts:
        # Check if the part contains Chinese characters
        if any('\u4e00' <= char <= '\u9fff' for char in part):
            translated_part = translator.translate(part)
        else:
            translated_part = part

        translated_parts.append(translated_part)

    # Join the translated parts back into a single string
    translated_text = ' '.join(translated_parts)

    return translated_text

input_text = "这是一个示例句子，包括一些中文字符。This is an example sentence with some English words."
translated_text = translate_chinese_to_english(input_text)
print(translated_text)
