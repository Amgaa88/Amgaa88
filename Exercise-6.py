#!/usr/bin/env python
# coding: utf-8

# In[48]:


grocery_list=['orange', 'apple', 'cake', 'candy', 'watermelon']


# In[36]:


i=1
while (i<len(grocery_list)+1):
    for j in grocery_list:
        print(i,j)
        i+=1
    


# In[47]:


for i in range(len(grocery_list)):
    print(i+1,grocery_list[i])


# In[53]:


for (i,j) in enumerate(grocery_list):
    print(i+1, j)


# In[54]:


#Lesson-3 Flow control exercises


# In[56]:


for i in range(10):
    print(i+1)


# In[57]:


'skyscraper'.index('c')


# In[88]:


def getindex(x, y):
    for (i,j) in enumerate(x):
        if j==y:
            print(i)


# In[89]:


getindex('amgaa', 'a')


# In[55]:


def shout_words(z):
    z=z.split(' ')
    for (i,j) in enumerate(z):
        print(j.upper()+'!')


# In[56]:


shout_words('Everybody likes bananas')


# In[150]:


def extract_longer(x,y):
    y=y.split(' ')
    for i in range(len(y)):
        if len(y[i])>int(x):
            print(y[i])
        else:
            continue
    return False


# In[152]:


#Container data types-exercises


# In[163]:


def eulerM(x,y,z,q):
    sum=0
    for i in range(x,y):
        if(i%z==0 or i%q==0):
            sum+=i
    print(sum)


# In[164]:


eulerM(1,1000,3,5)


# In[180]:


a=[]
for i in range(5):
    b=input('enter numbers ')
    a.append(b)
print(a)

    


# In[224]:


a=[]
c=[]
def duplicatedOrNot(x):
    for i in range(x):
        b=input('enter items: ')
        a.append(b)
    for i in range(0,len(a)):
        for j in range(i+1, len(a)):
            if(a[i]==a[j]):
                c.append(a[j])

    print(c)


# In[225]:


duplicatedOrNot(10)


# In[471]:


def fxn(stng):
    oupt=stng[0]
    for i in range(1,len(stng)):
        if stng[i-1]==' ':
            oupt+=stng[i]
    oupt=oupt.upper()
    return oupt
inpt1='Computer science engineering'
print(fxn(inpt1))


# In[5]:


myfile=open('data.txt', 'w')
myfile.write('I am writing data to my file')
myfile.close()


# In[6]:


myfile=open('data.txt', 'r')


# In[7]:


myfile.read()


# In[9]:


with open('data.txt') as f:
    print(f.read())


# In[10]:


name='Mark'


# In[11]:


len(name) #function


# In[12]:


name.upper() #method


# In[13]:


class Person(object):
    pass


# In[14]:


type(Person)


# In[15]:


type(Person)==type(int)


# In[16]:


nobody=Person()


# In[17]:


type(nobody)


# In[18]:


class Person(object):
    species='Homo sapiens'
    def talk(self):
        return "hello there, how are you?"


# In[19]:


nobody=Person()


# In[20]:


nobody.species


# In[21]:


nobody.talk()


# In[22]:


# function defined in the class is called method


# In[23]:


somebody=Person()


# In[24]:


somebody.species="homo internetus"


# In[25]:


somebody.name='Mark'


# In[26]:


nobody.species


# In[27]:


Person.species='Unknown'


# In[28]:


nobody.species


# In[29]:


somebody.species


# In[30]:


Person.name='Unknown'


# In[31]:


nobody.name


# In[32]:


somebody.name


# In[33]:


del somebody.name


# In[34]:


somebody.name


# 

# In[2]:


liste=[1,2,3,4,5,]


# In[ ]:


liste.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




