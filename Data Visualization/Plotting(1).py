

#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
data=pd.read_excel("February.xlsx")
data2=pd.read_excel("March.xlsx")
data3=pd.read_excel("April.xlsx")
#Total Post count
Total=data.count(axis=1) #Total posts February
Total2=data2.count(axis=1) #Total posts March
Total3=data3.count(axis=1) #Total posts April
#transposing datasets
df_t = data.T
df2_t=data2.T
df3_t=data3.T


# In[58]:


#Counting the Occurances;
Zero=df_t.loc[df_t[0]==0].count()
One=df_t.loc[df_t[0]==1].count()
Two=df_t.loc[df_t[0]==2].count()
Three=df_t.loc[df_t[0]==3].count()
Four=df_t.loc[df_t[0]==4].count()

Z_p=(Zero/Total)*100 #Percentage of Zero values
O_p=(One/Total)*100 #Percentage of One values
Tw_p=(Two/Total)*100 #Percentage of Two values
Th_p=(Three/Total)*100 #Percentage of Three values
F_p=(Four/Total)*100 #Percentage of Four values

#Counting the Occurances; March
Zero2=df2_t.loc[df2_t[0]==0].count()
One2=df2_t.loc[df2_t[0]==1].count()
Two2=df2_t.loc[df2_t[0]==2].count()
Three2=df2_t.loc[df2_t[0]==3].count()
Four2=df2_t.loc[df2_t[0]==4].count()

Z_p2=(Zero2/Total2)*100 #Percentage of Zero values
O_p2=(One2/Total2)*100 #Percentage of One values
Tw_p2=(Two2/Total2)*100 #Percentage of Two values
Th_p2=(Three2/Total2)*100 #Percentage of Three values
F_p2=(Four2/Total2)*100 #Percentage of Four values



#Counting the Occurances; April
Zero3=df3_t.loc[df3_t[0]==0].count()
One3=df3_t.loc[df3_t[0]==1].count()
Two3=df3_t.loc[df3_t[0]==2].count()
Three3=df3_t.loc[df3_t[0]==3].count()
Four3=df3_t.loc[df3_t[0]==4].count()

Z_p3=(Zero3/Total3)*100 #Percentage of Zero values
O_p3=(One3/Total3)*100 #Percentage of One values
Tw_p3=(Two3/Total3)*100 #Percentage of Two values
Th_p3=(Three3/Total3)*100 #Percentage of Three values
F_p3=(Four3/Total3)*100 #Percentage of Four values


# In[59]:


#Type casting
Z_p=float(Z_p)
O_p=float(O_p)
Tw_p=float(Tw_p)
Th_p=float(Th_p)
F_p=float(F_p)

Z_p2=float(Z_p2)
O_p2=float(O_p2)
Tw_p2=float(Tw_p2)
Th_p2=float(Th_p2)
F_p2=float(F_p2)


Z_p3=float(Z_p3)
O_p3=float(O_p3)
Tw_p3=float(Tw_p3)
Th_p3=float(Th_p3)
F_p3=float(F_p3)

#Creating dataframes
Plot_data=pd.DataFrame([[Z_p,O_p,Tw_p,'Feb.']],columns=['negative','neutral','Positive','Month'])
Plot_data2=pd.DataFrame([[Z_p2,O_p2,Tw_p2,'March']],columns=['negative','neutral','Positive','Month'])
Plot_data3=pd.DataFrame([[Z_p3,O_p3,Tw_p3,'April']],columns=['negative','neutral','Positive','Month'])
#Merging
Merge1=Plot_data.append(Plot_data2)
#Merging
Merge1=Merge1.append(Plot_data3)
Merge1=Merge1.set_index('Month')
#plotting the merged dataframe of Feb, Mar, April
from matplotlib import pyplot as plt
ax = Merge1.plot.bar(figsize=(10,5))
plt.ylabel("Percentage")
plt.show()


# In[ ]:




