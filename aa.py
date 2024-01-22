# import csv

# def count_students(csv_data, gender, college, degree):
#     count = 0

#     f = open(csv_data, 'r', encoding='utf-8')
#     reader = csv.reader(f)
#     next(reader) 

#     for row in reader:
#         if row[0] == gender and row[1] == college and row[2] == degree:
#             count += 1
#     f.close
#     return count
# print(count_students('student.csv',   'ذكر' ,  'علوم الحاسب والمعلومات'  , 'البكالوريوس'))

words_list = ['له', 'يا', 'إذا', 'قد', 'ولا', 'كل', 'أو', 'ذي', 'وما', 'لي', 'إلا', 'فيه', 'وقد', 'منه', 'غير', 'ومن', 'ي', 'لو', 'يوم', 'و', 'وإن', 'ولم', 'فما', 'هذا', 'كنت', 'كما', 'وهو', 'هوى', 'دهر', 'وفي', 'أنت', 'فلا', 'عليه', 'هو', 'ناس', 'مثل', 'لك', 'قلب', 'أنا', 'منها', 'أرض', 'أم', 'ثم', 'حين', 'ذا', 'ليل', 'زمان', 'كم', 'لنا', 'حب', 'خير', 'تي', 'منك', 'فإن', 'حسن', 'ذاك', 'ابن', 'ك', 'قلبي', 'ملك', 'دنيا', 'ولو', 'عين', 'شمس', '،', 'بما', 'ماء', 'لقد', 'قوم', 'فقد', 'عنه', 'بي', 'ترى', 'كيف', 'مجد', 'فتى', 'نفس', 'بحر', 'حق', 'ولكن', 'مني', 'من', 'عليك', 'وكم', 'علم', 'وهي', 'يوما', 'أيام', 'فلم', 'دين', 'بلا', 'فضل', 'أهل', 'سوى', 'فيك', 'هي', 'وأنت', 'وإذا', 'أمر', 'بل', 'ر', 'ألا', 'إليك', 'موت', 'ن', 'ورى', 'إليه', 'حيث', 'دون', 'بدر', 'قلت', 'نار', 'حياة', 'وكل', 'قال', 'عد', 'أرى', 'ان', 'وليس', 'دار', 'حي', 'تلك', 'يكن', 'وجه', 'نور', 'صبا', 'عني', 'كانت', 'بني', 'فهو', 'شعر', 'عز', 'لمن', 'خلق', 'فيا', 'إني', 'سماء', 'شيء', 'ذكر', 'أين', 'ذو', 'عليها', 'ندى', 'لله', 'يد', 'قلوب', 'بك', 'أما', 'قول', 'أيها', 'ورد', 'علا', 'عبد', 'عيون', 'فمن', 'ويا', 'وهل', 'يرى', 'بن', 'سر', 'سيف', 'نفسي', 'حرب', 'رأيت', 'وكان', 'أني', 'ليالي', 'كريم', 'عيش']
arabic_particles = ['من', 'في', 'إلى', 'عن', 'على', 'رب', 'فوق', 'تحت', 'خلف', 
                    'أمام', 'بين', 'عند', 'مع', 'حول', 'ضد', 'منذ', 'قبل', 'بعد', 
                    'خلا', 'حاشا', 'ما عدا', 'أن', 'أي', 'كي', 'لن', 'لم', 'هل', 
                    'ل', 'إذ', 'إن', 'كأن', 'لكن', 'ليت', 'لعل', 'حتى', 'ليس', 
                    'كان', 'أصبح', 'بات', 'صار', 'ما زال', 'ما فتئ', 'ما انفك', 
                    'لا يزال', 'ما دام', 'ظل', 'عاد', 'أضحى', 'غدا', 'لا يبلى', 
                    'أمسى', 'لما' ,'لا','علي' , 'كأني' , 'كأنه', 'كأنها' ,'ما' , ] 
x = words_list + arabic_particles
print(x)

x = ['له', 'يا', 'إذا', 'قد', 'ولا', 'كل', 'أو', 'ذي', 'وما', 'لي', 'إلا', 'فيه',
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
                              'ما دام', 'ظل', 'عاد', 'أضحى', 'غدا', 'لا يبلى', 'أمسى', 'لما', 'لا', 'علي', 'كأني', 'كأنه', 'كأنها', 'ما']
