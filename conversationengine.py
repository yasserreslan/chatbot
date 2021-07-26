
#Sample phrases
recommend_main = ('Tell me, are you ready to recommend our company to your friends? '
                'Please rate it on a scale from "0" to "10", where "0" - I will not '
                'recommend it, "10" - I will definitely recommend it.')

recommend_repeat = ('How would you rate the opportunity to recommend our company to your '
                    'friends on a scale from 0 to 10, where 0 - I will definitely not recommend it, '
                    '10-I will definitely recommend it.')


recommend_default = "I'm sorry I don't understand, could you repeat that ?"

positive_word = ('yes','Yes')

reject_word = ('no','No','Busy','busy','Sorry', 'sorry', "Can't", "can't")



def hello(name,company):
    
    return 'Hello %s, good afternoon! You are concerned about %s, we are conducting a survey of satisfaction with our services. Tell me, is it convenient for you to talk now?'% (name,company)


def hello_repeat(company):

    return 'This is %s,  Tell me, is it convenient for you to talk now?'% company



def forward():
    return 'To understand your question, I will transfer you to my colleague. Please Hang On!.'


def Hangup_action(level):
    if level == 'positive':
        return ('Great! Thank you so much for your time! All the best to you! \n '
        'Write Anything into the chat to exit this page!')
    
    elif level == 'negative':
        return ('I understand you. In any case, thank you so much for your time! All the best to you. \n'
                'Write Anything into the chat to exit this page!')
    
    return forward()




def message_handler(msg,stage,name = '',company = ''):  #returns a list containing both the message response 
        if stage == 'hello':                              # and the stage of the current conversation
            if msg == 'hello':
                return [hello(name,company),'hello']


            if any(k in msg for k in positive_word):
                
                return [recommend_main,'recommend']
            
            
            elif any(k in msg for k in reject_word):
                return [Hangup_action('negative'),'hangup']

            else:
                return [hello_repeat('Neuro.net'),'hello']
            

        if stage == 'recommend':

            if str(msg).isdigit():
                if int(msg) <= 8:
                    return [Hangup_action('negative'),'hangup']

                elif int(msg) > 8:
                    return [Hangup_action('positive'),'hangup']
                
                
            else:
                return [recommend_default,'recommend']

        
                
def is_rating(rating):              #determine if user message is a number (i.e rating)

    return str.isdigit(rating)

    


    
