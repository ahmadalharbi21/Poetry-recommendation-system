import re
import json

class Text:
    # Class Constants
    PREFIXES = {'ي', 'ت', 'ب', 'ل', 'ف', 'س'}
    SUFFIXES = {'هن', 'هم'}
    PREFIXES_OF_WAW_ALEF = {'ب', 'ا', 'ي'}
    TASHKEEL = {'َ', 'ُ', 'ِ', 'ّ', 'ْ', 'ً', 'ٌ', 'ٍ'}
    ARABIC_PARTICLES = ['له', 'يا', 'إذا', 'قد', 'ولا', 'كل', 'أو', 'ذي', 'وما', 'لي', 'إلا', 'فيه',
        'وقد', 'منه', 'غير', 'ومن', 'ي', 'لو', 'يوم', 'و', 'وإن', 'ولم', 'فما', 'هذا',
            'كنت', 'كما', 'وهو',   'وفي', 'أنت', 'فلا', 'عليه', 'هو',  'مثل', 'لك', 
            'أنا', 'منها',  'أم', 'ثم', 'حين', 'ذا',  
            'كم', 'لنا',  'تي', 'منك', 'فإن',  'ذاك', 'ابن', 'ك',  
            'ولو',   '،', 'بما',  'لقد',  'فقد', 'عنه', 'بي',  'كيف', 
                'ولكن', 'مني', 'من', 'عليك', 'وكم',  'وهي',
                'يوما', 'أيام', 'فلم',  'بلا',  'سوى', 'فيك', 'هي', 'وأنت', 
                'وإذا', 'أمر', 'بل', 'ر', 'ألا', 'إليك',  'ن',  'إليه', 'حيث',
                    'دون',  'قلت',  'وكل', 'قال', 
                    'ان', 'وليس',  'تلك', 'يكن', 'عني', 'كانت',
                        'بني', 'فهو',  'لمن',  'فيا', 'إني', 'شيء',  
                        'أين', 'ذو', 'عليها',  'بك', 'أما', 'قول', 'أيها',
                        'فمن', 'ويا', 'وهل', 'يرى', 'بن', 
                            'رأيت', 'وكان', 'أني', 'من', 'في', 'إلى', 'عن', 'على',
                            'فوق', 'تحت', 'خلف', 'أمام', 'بين', 'عند', 'مع', 'حول', 'ضد', 'منذ', 'قبل', 'بعد',
                                'خلا', 'حاشا', 'ما عدا', 'أن', 'أي', 'كي', 'لن', 'لم', 'هل', 'ل', 'إذ', 'إن', 'كأن', 'لكن', 
                                'ليت', 'لعل', 'حتى', 'ليس', 'كان', 'أصبح', 'بات', 'صار', 'ما زال', 'ما فتئ', 'ما انفك', 'لا يزال',
                                'ما دام', 'ظل', 'عاد', 'أضحى', 'غدا', 'لا يبلى', 'أمسى', 'لما', 'لا', 'علي', 'كأني', 'كأنه', 'كأنها', 'ما', 'ذي' , 'ي', 'ك' ,'من'] 
          

    PREFIX_CONDITIONS = {
        'ي': ['ها', 'ون', 'هان', 'وا', 'ة'],
        'ت': ['ها', 'ون', 'ين', 'هان', 'وا', 'ة', 'ت'],
        'ب': ['ه', 'ان', 'ات', 'ين', 'ها', 'ة'],
        'ل': ['ة', 'ان', 'ات', 'ين', 'ها'],
        'ف': ['ها', 'ين', 'ات', 'ان', 'ة']
    }

    def __init__(self, text):
        self.text = text

    def hun_hum_suffix_removal(self, word):
        #  ''''
        # Remove هم and هن and associated suffixes

        # Args:
        #     String - word.
        # Returns:
        #     String - word with هم or هن removed.
        # ''''
        # Detect suffix presence
        if (word[-2:] in SUFIXES):
            # Search if the word begins with Alef_lam or Alef_lam and paired with a suffix
            alef_lam_search = re.search('ال', word)
            if(alef_lam_search != None and alef_lam_search.start() <= 1):
                if(word[0] in PREFIXES):
                    return word[1:]
            else:
                if(word[0] in PREFIXES):
                    return word[1:-2]
                else:
                    return word[:-2]
        return word

        

    def remove_suffix_waw_alef(self, word):
        if len(word) > 3 and word[-2:0] == 'وا' and word[0] in PREFIXES_OF_WAW_ALEF:
            return word[1:-2]
        return word
    

    def remove_prefix_sin(self, word):
        # '''
        # Remove prefix س as it follows a diffrent logic from the prfixes listed in the dictionary
        # Args:
        #     String - word.
        # Returns:
        #     String - word with prefix س and the following prefix (ي or ب)removed.
        # '''
        if len(word) > 2 and word[0] == 'س' and (word [1] == 'ي' or word [1] == 'ت'):
            for sufix in PREFIX_CONDITIONS['ب']:
                sufix = re.search(sufix + '$', word)
                if sufix != None:
                    return word[2:sufix.start()]
        return word
        pass

    def remove_prefixes_suffixes(self, word):
#  '''
#         Remove prefix س as it follows a diffrent logic from the prfixes listed in the dictionary
#         Args:
#             String - word.
#         Returns:
#             String - word with prefix س and the following prefix (ي or ب)removed.
#         '''
        if len(word) > 2 and word[0] == 'س' and (word [1] == 'ي' or word [1] == 'ت'):
            for sufix in PREFIX_CONDITIONS['ب']:
                sufix = re.search(sufix + '$', word)
                if sufix != None:
                    return word[2:sufix.start()]
        return word
        pass

    def remove_tashkeel(self, text):
        for mark in self.TASHKEEL:
            text = text.replace(mark, '')
        return text

    def remove_propositions_from_sentences(self, sentence):
        words = sentence.split()
        for i, word in enumerate(words):
            word = self.hun_hum_suffix_removal(word)
            word = self.remove_suffix_waw_alef(word)
            word = self.remove_prefix_sin(word)
            word = self.remove_prefixes_suffixes(word)
            words[i] = word
        return ' '.join(words)

    def clean_text(self):
        text = self.remove_tashkeel(self.text)
        words = text.split()
        no_al_words = [word[2:] if word.startswith("ال") and word != 'الله' else word for word in words]
        text_without_al = ' '.join(no_al_words)
        text_without_al = ' '.join(word for word in text_without_al.split() if word not in self.ARABIC_PARTICLES)
        cleaned_text = self.remove_propositions_from_sentences(text_without_al)
        return cleaned_text
def process_poems(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        poems = json.load(file)

    processed_poems = {}

    for index, data in poems.items():
        poem_text = list(data.keys())[0]
        additional_info = data[poem_text]

        text_processor = Text(poem_text)
        cleaned_text = text_processor.clean_text()

        processed_poems[index] = {cleaned_text: additional_info}

    # with open(output_file_path, 'w', encoding='utf-8') as file:
    #     json.dump(processed_poems, file, ensure_ascii=False, indent=4)

# Example usage
input_file_path = 'orgPoem'
output_file_path = 'Model'
# process_poems(input_file_path, output_file_path)
f = open ('org_poem', 'a', encoding='utf-8')
with open(input_file_path, 'w', encoding='utf-8') as file:
    for line in file:
        json_data = line
        json_data_double_quotes = json.dumps(json.loads(json_data), ensure_ascii=False)
        f = open ('org_poem', 'a', encoding='utf-8')
        f.write(json_data_double_quotes)

print(json_data_double_quotes)
