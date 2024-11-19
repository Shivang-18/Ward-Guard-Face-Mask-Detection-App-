#!/usr/bin/env python
# coding: utf-8

# In[1]:


from twilio.rest import Client


# In[3]:

def message_ward():
    acc_sid = "AC3cda6ea5fd57703f4e8cbec75767fb36"
    auth_program = "597dc57a12cbc744644c18b28499bb40"
    twilio_num = "+14847598258"
    target_num="+919650229309"
    
    client=Client(acc_sid,auth_program)

    message=client.messages.create(
        body="wassup",
        from_=twilio_num,
        to=target_num
        )
    return(message.body)

message_ward()


# In[ ]:





# In[ ]:




