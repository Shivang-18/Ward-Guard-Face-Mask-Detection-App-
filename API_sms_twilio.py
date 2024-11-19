#!/usr/bin/env python
# coding: utf-8

# In[1]:


from twilio.rest import Client


# In[3]:

def message_ward():
    acc_sid = "ACXXXXXXXXXXXXXXXXXXXb36"
    auth_program = "597XXXXXXXXXXXXXXXXXXX0"
    twilio_num = "+14XXXXXXXXXX"
    target_num="+91XXXXXXXXXX"
    
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




