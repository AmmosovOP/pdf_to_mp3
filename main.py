from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path




def pdf_to_mp3(file_path='test.pdf', language='ru'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # return 'File exist!'

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:

            print(f'[+] Original file: {Path(file_path).name}')
            print('[+] Processing...')

            pages = [page. extract_text() for page in pdf.pages]

            text = ''.join(pages)
            text = text.replace('\n', '')
            with open('text.txt', 'w') as file:
                file.write(text)

            my_audio = gTTS(text=text, lang=language)
            file_name = Path(file_path).stem
            my_audio.save(f'{file_name}.mp3')

            return f'[+] {file_name}.mp3 saved successfully! \n --Have a nice day!--'

    else:
        return 'File not exist'

def main():
    tprint('PDF>>TO>>MP3', font='random')
    file_path = input("\n Enter the path to the file: ")
    language = input("\n Choose the file's language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == "__main__":
    main()
