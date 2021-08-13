import os
import telebot
#import text2emotion as te
import random
import numpy
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton , ReplyKeyboardMarkup, Update

# import telegram
# from telegram.ext import InlineQueryHandler, CallbackQueryHandler

my_secret = '1931100716:AAGg2A0Zx2fvq5q1DBF9mvYmXCQAqCR2zzc'
bot = telebot.TeleBot(my_secret)

#use for formatting: parse_mode = 'html'


@bot.message_handler(commands=['start'])
def greet(message): 
  # bot.send_photo(message.chat.id, 'https://www.freeiconspng.com/img/28501', 'Hello there! How are you feeling today? I hope you are well \U0001F604')
  bot.send_message(message.chat.id, 'Welcome to Legal Buddies! I am your <b>one-stop legal companion</b> for people that are looking for legal avenues and where to get help! How may I help you today?\n\n<u><b>Here are a list of things I can assist with:</b></u> \n/legalaid: Find details of legal aid schemes available \n/lawyers: Find details of lawyers available \n', parse_mode = 'html')


#LEGAL AID SCHEMES
#Foreigner/Singaporean
def gen_markup():
    markup = InlineKeyboardMarkup() 
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Foreigner", callback_data="foreigner"), InlineKeyboardButton("Singaporean", callback_data="singaporean"), InlineKeyboardButton("Organisation", callback_data="organisation"))
    return markup

def legal_aid(message):
  if type(message) is str:
    if message == '/legalaid':
      return True

def lawyers(message):
  if type(message) is str:
    if message == '/lawyers':
      return True

@bot.message_handler(func=lambda msg: legal_aid(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "Are you a foreigner, Singaporean, or are you representing an organisation (e.g. NGOs)?", reply_markup=gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "foreigner":
        bot.send_message(call.message.chat.id,"<b>| QUICK LINKS |</b>\n\U0001F538 <b>Humanitarian Organisation for Migration Economics (HOME)</b> - workplace abuse: https://www.home.org.sg/contact \n\n\U0001F539 <b>Transient Workers Count Too (TWC2)</b> - workplace injury, abuse, or late salary payments: https://twc2.org.sg/\n\n\U0001F538 <b>Justice Without Borders (JWB)</b> - workplace abuse or violation:  https://forjusticewithoutborders.org/get-help/ \n\n\U0001F539<b>Foreign Domestic Worker Association for Social Support and Training (FAST)</b> - mediation services: https://www.fast.org.sg/care/", parse_mode = 'html', disable_web_page_preview=True)
    elif call.data == 'organisation':
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
        markup.add('Description [PLH]', 'Apply now [PLH]')
        bot.send_message(call.message.chat.id,'Currently in Singapore, only ProjectLawHelp is available to aid NGOs', reply_markup=markup)
    elif call.data == "singaporean":
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
        markup.add('Civil', 'Criminal')
        bot.send_message(call.message.chat.id,'What field of law does your case fall under?', reply_markup=markup)

#Singaporean - type of case
def type_case_civil(message):
  if type(message) is str:
    if message == 'Civil':
      return True

def type_case_crim(message):
  if type(message) is str:
    if message == 'Criminal':
      return True

@bot.message_handler(func=lambda msg: type_case_crim(msg.text))
def message_handler(message):
   markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
   markup.add('Description [CLAS]', 'Apply Now [CLAS]')
   bot.send_message(message.chat.id,'CLAS info basic', reply_markup=markup)

#Criminal- ClAS
def type_case_clas_description(message):
  if type(message) is str:
    if message == 'Description [CLAS]':
      return True

def type_case_clas_apply(message):
  if type(message) is str:
    if message == 'Apply Now [CLAS]':
      return True
      
@bot.message_handler(func=lambda msg: type_case_clas_description(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "Description")


@bot.message_handler(func=lambda msg: type_case_clas_apply(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "link to clas")




#CIVIL
# def gen_markup2():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(InlineKeyboardButton("Legal Aid Bureau", callback_data="lab"), InlineKeyboardButton("Primary Justice Project", callback_data="pjp"))
    return markup

def civil(message):
  if type(message) is str:
    if message == 'Civil':
      return True

@bot.message_handler(func=lambda msg: civil(msg.text))
def message_handler(message):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
    markup.add('Legal Aid Bureau', 'Primary Justice Project')
    bot.send_message(message.chat.id,'How would you like to find out more about Legal Aid Bureau?', reply_markup=markup)
    bot.send_message(message.chat.id, "There are currently two schemes available for civil cases. Click the scheme you are interested to find more about.", reply_markup=markup)

def lab(message):
  if type(message) is str:
    if message == 'Legal Aid Bureau':
      return True

def pjp(message):
  if type(message) is str:
    if message == 'Primary Justice Project':
      return True

@bot.message_handler(func=lambda msg: lab(msg.text))
def message_handler(message):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
    markup.add('Description [LAB]', 'Apply Now [LAB]')
    bot.send_message(message.chat.id,'How would you like to find out more about Legal Aid Bureau?', reply_markup=markup)
    
@bot.message_handler(func=lambda msg: pjp(msg.text))
def message_handler(message):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard = True)
    markup.add('Description [PJP]', 'Apply Now [PJP]')
    bot.send_message(message.chat.id,'How would you like to find out more about Legal Aid Bureau?', reply_markup=markup)

# LAB
def lab_description(message):
  if type(message) is str:
    if message == 'Description [LAB]':
      return True

def lab_application(message):
  if type(message) is str:
    if message == 'Apply Now [LAB]':
      return True

@bot.message_handler(func=lambda msg: lab_description(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "<b><u>Legal Advice</u></b>\nLAB lawyers can give you oral advice on questions relating to Singapore law and suggest practical steps you may take in your case. \n\n<b><u>Legal Assistance (Drafting of Simple Legal Documents)</u></b>\nLAB can help you draft the following: \n1. Will (a legal document by which a person expresses his wishes as to how his property will be distributed upon his death and the persons who will manage the distribution of such property) \n2.Deed of Separation (a legal document signed by a married couple stating their mutual decision to live separately, before deciding on a divorce).\n\n<b><u>Legal Aid</u></b>\nLAB lawyers or a lawyer assigned by LAB can represent you in many kinds of civil proceedings, as set out in the Legal Aid and Advice Act. These include proceedings before the Court of Appeal, the High Court, District Courts, Magistrates’ Courts, the Family Courts, the Syariah Court and the Syariah Court Appeal Board, and the Commissioner of Labour under the Work Injury Compensation Act.\n\n<i>LAB does not handle criminal proceedings, some civil proceedings (defamation cases, proceedings from Small Claims tribunals, proceedings in the Family Justice Courts)</i>", parse_mode = 'html')

@bot.message_handler(func=lambda msg: lab_description(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "<b>Apply here:</b> https://eservices.mlaw.gov.sg/labesvc/\n(a) For Legal Advice and Assistance matters, you must pass the Means Test. (b) For Legal Aid, you must pass both the Means and Merits Test. \n\n<b><u>Means Test</u></b>1. The average Per Capita Gross Monthly Household Income (PCHI) must be $950 or lower for the last 12 months prior to the application\n2. The Annual Value of applicant’s place of residence owned by the applicant must be $13,000 or lower\n3. The applicant’s savings and non-CPF investments must be $10,000 or lower, if he is younger than 60 years old. Applicants aged 60 and above are allowed to have savings and non-CPF investments of $40,000 or lower.\n4. The applicant must not own any other property besides his/her place of residence.\n\n<u><b>Merits Test</b></u>\nWhether there are reasonable grounds for filing a case will be determined by the Legal aid Bureau. ", parse_mode = 'html')

#PJP
def pjp_description(message):
  if type(message) is str:
    if message == 'Description [PJP]':
      return True

def pjp_application(message):
  if type(message) is str:
    if message == 'Apply Now [PJP]':
      return True

@bot.message_handler(func=lambda msg: pjp_description(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "desc pjp")

@bot.message_handler(func=lambda msg: pjp_description(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "Apply pjp")


#ProjectLawHelp
def type_case_description(message):
  if type(message) is str:
    if message == 'Description [PLH]':
      return True

def type_case_application(message):
  if type(message) is str:
    if message == 'Apply Now [PLH]':
      return True

@bot.message_handler(func=lambda msg: type_case_description(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "We match community organisations which qualify for assistance with law firms willing to provide free non-litigation commercial legal services.Examples of such legal services include:Corporate Law (e.g. advice on contracts with suppliers, indemnity agreements for corporate sponsors, drafting pledges for donors);Employment Law (e.g. drafting or reviewing employment contracts);Intellectual Property Law (e.g. advice on copyright, data protection, website use);Property Law (e.g. lease terms); and other legal matters not involving court litigation advice or representation.Successful applicants will work directly with the law firm assigned. All legal matters of the community organisation are handled in professional confidence by he volunteer law practice.")


@bot.message_handler(func=lambda msg: type_case_application(msg.text))
def message_handler(message):
    bot.send_message(message.chat.id, "https://form.jotform.me/91284013638456")


#Find no of lawyers available

@bot.message_handler(func=lambda msg:lawyers(msg.text))
def message_handler(message):
   my_number= str(numpy.random.randint(0,100))
   bot.send_message(message.chat.id,"Number of available lawyers: " + my_number)


bot.polling()

