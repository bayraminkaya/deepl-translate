import requests

def translate_text(text, target_language="TR"):
    deepL_api_key = "your api key"
    api_url = "https://api-free.deepl.com/v2/translate"

    params = {
        "auth_key": deepL_api_key,
        "text": text,
        "target_lang": target_language,
    }

    response = requests.post(api_url, data=params)
    translation = response.json()["translations"][0]["text"]
    return translation

def main(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        input_text = file.read()

    # Gerekirse metni paragraflara bölün
    paragraphs = input_text.split("\n")

    translated_text = ""
    for paragraph in paragraphs:
        if paragraph.strip() != "":
            translated_paragraph = translate_text(paragraph)
            translated_text += translated_paragraph + "\n"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(translated_text)

    print("Çeviri tamamlandı. Çevirilen metinler", output_file, "dosyasına kaydedildi.")

if __name__ == "__main__":
    input_file_path = ""  # Değiştirebilirsiniz
    output_file_path = ""  # Değiştirebilirsiniz

    main(input_file_path, output_file_path)
