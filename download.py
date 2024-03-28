import requests
from googletrans import Translator

from loader import db



HADITH_PAGE_COUNT = 97
MAIN_LINK = "https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/rus-bukhari/sections/(id).min.json"
MAX_RETRIES = 3


def translate_to(text, lang="uz"):
    translator = Translator()
    return translator.translate(text, dest=lang).text


def download_hadith(link):
    response = requests.get(link)
    if response.status_code == 200:
        hadith_s = response.json().get("hadiths")
        hadith_section = response.json().get('metadata').get('section')
        return hadith_s, hadith_section
    else:
        return False


def write_to_database():
    link_count = 1
    try:
        while link_count < HADITH_PAGE_COUNT + 1:
            link = MAIN_LINK.replace("(id)", str(link_count))
            hadith_data, section = None, None
            retries = 0
            while retries < MAX_RETRIES and not hadith_data:
                hadith_data, section = download_hadith(link)
                retries += 1
            if not hadith_data:
                print("Failed to download data for link:", link)
                continue
            try:
                hadith_data, section = download_hadith(link)
                section_name = next(iter(section.values()), '')
                section_name_ru = translate_to(section_name, lang="ru")
                section_name_uz = translate_to(section_name)
                for hadith in hadith_data:
                    hadith_ru = hadith.get("text")
                    hadith_uz = translate_to(hadith_ru)
                    db.add_hadis_3(
                        UZ_S=section_name_uz,
                        UZ=hadith_uz,
                        RU_S=section_name_ru,
                        RU=hadith_ru
                    )
                    print("Saved 1 hadith to Database")
                link_count += 1
            except Exception as e:
                link_count += 1
                continue
    except Exception as e:
        print(e)
        return str(e)
    else:
        print('Success: Saved all hadiths')
        return True


if __name__ == '__main__':
    write_to_database()
