import json
import re


class Text:
    # Constants
    
    
    def __init__(self,text):
        self.text = text


    PREFIXES = set(['ي', 'ت', 'ب', 'ل','ف','س'])
    SUFIXES = set(['هن', 'هم'])
    PREFIXES_OF_WAW_ALEF = set(['ب', 'ا', 'ي'])

    # Used to check if the first letter is a prefix or part of the word
    prefeix_conditions_dict = dict()
    prefeix_conditions_dict['ي'] = ['ها', 'ون', 'هان','وا', 'ة']
    prefeix_conditions_dict['ت'] = ['ها', 'ون','ين' ,'هان','وا', 'ة', 'ت']
    prefeix_conditions_dict['ب'] = [ 'ه', 'ان', 'ات', 'ين', 'ها', 'ة']
    prefeix_conditions_dict['ل'] = [ 'ة', 'ان', 'ات', 'ين', 'ها']
    prefeix_conditions_dict['ف'] = ['ها', 'ين', 'ات', 'ان', 'ة']

    def hun_hum_sufix_removal(word):
        '''
        Remove هم and هن and associated suffixes

        Args:
            String - word.
        Returns:
            String - word with هم or هن removed.
        '''
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

    def remove_sufixe_waw_alef(word):
        if len(word) > 3 and word[-2:0] == 'وا' and word[0] in PREFIXES_OF_WAW_ALEF:
            return word[1:-2]
        return word

    def remove_prefix_sin(word):
        '''
        Remove prefix س as it follows a diffrent logic from the prfixes listed in the dictionary
        Args:
            String - word.
        Returns:
            String - word with prefix س and the following prefix (ي or ب)removed.
        '''
        if len(word) > 2 and word[0] == 'س' and (word [1] == 'ي' or word [1] == 'ت'):
            for sufix in prefeix_conditions_dict['ب']:
                sufix = re.search(sufix + '$', word)
                if sufix != None:
                    return word[2:sufix.start()]
        return word

    def remove_prefixe_wsufixes(word):
        '''
        Args:
            String - word.
        Returns:
            String - word with prefixes and sufixes removed.
        '''
        for prefix in prefeix_conditions_dict.keys():
            if len(word) > 0 and word[0] == prefix:
                sufix = None
                for sufix in prefeix_conditions_dict[prefix]:
                    sufix = re.search(sufix + '$', word)
                    if sufix != None:
                        word = word[1:sufix.start()]
                        return word
        return word

    def remove_propositions_from_sentences(sentence):
        '''
        Args:
            A String - sentnece.
        Returns:
            A string containing Sentence with prefixes remove.
        '''
        #assert type(sentence) == str
        output = list()
        for word in str(sentence).split():
            word = hun_hum_sufix_removal(word)
            word = remove_sufixe_waw_alef(word)
            word = remove_prefix_sin(word)
            word = remove_prefixe_wsufixes(word)
            output.append(word)
        return ' '.join(output)

    def remove_tashkeel(text):
        tashkeel = 'َ ُ ِ ّ ْ ً ٌ ٍ'.split()
        for mark in tashkeel:
            text = text.replace(mark, '')
        return text


    # file_path = "poemtext1.txt"

    # # Open the file in read mode
    # f = open(file_path, "r" , encoding='utf-8') 
    #     # Load the JSON data
    # data  = f.readlines()
    # ff = open('modelPoem','w', encoding='utf-8')
    # i = 1
    @staticmethod
    def cleanText(text):
        for y in text:
            text=y.replace('*','')
            text=text.replace('\n',' ')
            text = text.replace('.','')
            text = remove_tashkeel(text)
            words = text.split()
            no_al_words = [word[2:] if word.startswith("ال") and word != 'الله' else word for word in words]
            text_without_al = ' '.join(no_al_words)
            arabic_particles = ['له', 'يا', 'إذا', 'قد', 'ولا', 'كل', 'أو', 'ذي', 'وما', 'لي', 'إلا', 'فيه',
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
            text = ' '.join(word for word in text_without_al.split() if word not in arabic_particles)
            text = text
            text = remove_propositions_from_sentences(text)
            text = ' '.join(word for word in text.split() if word != 'ي')
        return text
            
    #     x[j] = x[key]
    #     del x[y]
    #     dic[i] = x
    #     json.dump(dic,ff)
    #     ff.write('\n')
    #     i+=1
    # ff.close()
    # f.close()
    