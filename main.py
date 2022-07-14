from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint


def pdf_to_audio(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'[+] File {Path(file_path).name}')
        print('[+] Processing...')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            text = ''.join(pages).replace('\n', '')
        with open('result.txt', 'w') as file:
            file.write(text)

        file_name = Path(file_path).stem
        audio = gTTS(text=text, lang=language, slow=False)
        audio.save(f'{file_name}.mp3')
        return '[+] Successful !'
    else:
        return "[-] Incorrect file_path ! "


def main():
    tprint('Make_MP3_from_PDF', font="small")
    path = input('>>> Input your pdf file path.\n')
    print(pdf_to_audio(path))


if __name__ == "__main__":
    main()
