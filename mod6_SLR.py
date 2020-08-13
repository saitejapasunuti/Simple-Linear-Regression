#import necessary libraries
import pandas as pd#deals with dataframe
#pandas is used for data manipulation,cleaning &analysis
import numpy as np#deals with the numerical values
#numpy is used for scientific calculations
cc=pd.read_csv("D:\\360digiTMG\module 6\DataSets (2)\calories_consumed.csv")
cc
cc.columns='weight_gained','calories_consumed'
import matplotlib.pylab as plt#used for different type of plots
plt.scatter(x=cc['weight_gained'],y=cc['calories_consumed'],color='green')#scatter plot
#direction=positive
#strength=strong
#linear relationship
np.corrcoef(cc.weight_gained,cc.calories_consumed)
#|r|=correlation=0.94699101>0.85=strong correaltion&positive correlation
import statsmodels.formula.api as smf#contains all the statistical formula
model=smf.ols('calories_consumed~weight_gained',data=cc).fit()
model.summary()
#higher R^2 value better the model fits
#R-squared: 0.897>0.8=>strong correlation
#Prob (F-statistic):2.86e-07<0.05=>overall model is good
#Kurtosis:2.169=>positive kurtosis
#Skew:-0.098=>negatively skewed
pred1=model.predict(pd.DataFrame(cc['weight_gained']))
pred1
print(model.conf_int(0.01))# confidence interval 99% 
res=cc.calories_consumed-pred1
sqres=res*res
mse=np.mean(sqres)
rmse=np.sqrt(mse)
#rmse(root mean square error)=232.8335007096088


###########QUESTION 2#################

dt=pd.read_csv("D:\\360digiTMG\module 6\DataSets (2)\delivery_time.csv")
dt
dt.columns='delivery_time','sorting_time'
plt.scatter(x=dt["delivery_time"],y=dt["sorting_time"],color="yellow")
#moderate positive correlation
np.corrcoef(dt.delivery_time,dt.sorting_time)
# 0.82599726

######log transformation##################

#x=log(delivery_time),y=sorting_time
plt.scatter(x=np.log(dt["delivery_time"]),y=dt["sorting_time"])
#moderate positive correaltion
np.corrcoef(np.log(dt.delivery_time),dt.sorting_time)
#0.84317726=>moderate correlatrion
model_dt=smf.ols('sorting_time~np.log(delivery_time)',data=dt).fit()
model_dt.summary()
#R-squared:0.711<0.8=>moderate correlation
#Prob (F-statistic):1.59e-06 <0.05=>over it is a good model
pred_dt=model_dt.predict(pd.DataFrame(dt['delivery_time']))
pred_dt
print(model_dt.conf_int(0.01))

res_dt=dt.sorting_time-pred_dt
sqres_dt=res_dt*res_dt
mse_dt=np.mean(sqres_dt)
rmse=np.sqrt(mse_dt)
#rmse=1.3337477286899515


################Question 3################

emp=pd.read_csv('D:\\360digiTMG\module 6\DataSets (2)\emp_data.csv')
emp
plt.scatter(x=emp['Salary_hike'],y=emp['Churn_out_rate'],color='red')
np.corrcoef(emp.Salary_hike,emp.Churn_out_rate)
#-0.91172162=>negative correlation
model3=smf.ols('Churn_out_rate~Salary_hike',data=emp).fit()
model.summary()
#R-squared:0.897>0.8=>strong correlation
#Prob (F-statistic):2.86e-07<0.05=>overall model is good
pred3=model3.predict(pd.DataFrame(emp['Salary_hike']))
pred3
print(model3.conf_int(0.01))

res3=emp.Churn_out_rate-pred3
sqres3=res3*res3
mse3=np.mean(sqres3)
rmse3=np.sqrt(mse3)
rmse3
#3.997528462337793

############log transformation###########
plt.scatter(x=np.log(emp['Salary_hike']),y=emp['Churn_out_rate'],color='green')
np.corrcoef(np.log(emp.Salary_hike),emp.Churn_out_rate)
#-0.92120773>0.85=>strong negative correltion
#slightly increase in the value
model3l=smf.ols('Churn_out_rate~Salary_hike',data=emp).fit()
model3l.summary()
#R-squared:0.831=>strong correlation
#Prob (F-statistic):0.000239<0.05=>overall model is good

pred3l=model3l.predict(pd.DataFrame(emp['Salary_hike']))
pred3l
print(model3l.conf_int(0.01))

res3l=emp.Churn_out_rate-pred3l
sqres3l=res3l*res3l
mse3l=np.mean(sqres3l)
rmse3l=np.sqrt(mse3l)
rmse3l
#rmse=3.997528462337793

##########exponential transformation############

plt.scatter(x=emp['Salary_hike'],y=np.log(emp['Churn_out_rate']),color='orange')

np.corrcoef(emp.Salary_hike,np.log(emp.Churn_out_rate))
#-0.93463607=>strong -ve correlation
model3e=smf.ols('np.log(Churn_out_rate)~Salary_hike',data=emp).fit()
model3e.summary()
#R-squared:0.874>0.8
#p value-7.38e-05<0.05
pred_el=model3e.predict(pd.DataFrame(emp['Salary_hike']))
pred_el
pred3e=np.exp(pred_el)
print(model3l.conf_int(0.01))

res3e=emp.Churn_out_rate-pred3e
sqres3e=res3e*res3e
mse3e=np.mean(sqres3e)
rmse3e=np.sqrt(mse3e)
rmse3e
#3.5415493188215756

##############Question 4################

salhk=pd.read_csv('D:\\360digiTMG\module 6\DataSets (2)\Salary_Data.csv')
salhk
plt.scatter(x=salhk['YearsExperience'],y=salhk['Salary'],color='black')
#strong positive corelation
np.corrcoef(salhk.YearsExperience,salhk.Salary)
#0.97824162=>strong correlation
model4=smf.ols('Salary~YearsExperience',data=salhk).fit()
model4.summary()
#R-squared: 0.957=>strong correlation
#Prob (F-statistic): 1.14e-20=> overall model is good
pred4=model4.predict(pd.DataFrame(salhk['YearsExperience']))
pred4
print(model4.conf_int(0.01))

res4=salhk.Salary-pred4
sqres4=res4*res4
mse4=np.mean(sqres4)
rmse4=np.sqrt(mse4)
rmse4
#rmse=5592.043608760661

############log transformation############

plt.scatter(x=np.log(salhk['YearsExperience']),y=salhk['Salary'],color='brown')
np.corrcoef(salhk.YearsExperience,salhk.Salary)
#0.97824162=>strong correlation
model4l=smf.ols('Salary~np.log(YearsExperience)',data=salhk).fit()
model4l.summary()
#R-squared: 0.854=>strong correlation
#Prob (F-statistic):3.25e-13=>overall model is good

pred4l=model4l.predict(pd.DataFrame(salhk['YearsExperience']))
pred4l
print(model4l.conf_int(0.01))

res4l=salhk.Salary-pred4l
sqres4l=res4l*res4l
mse4l=np.mean(sqres4l)
rmse4l=np.sqrt(mse4l)
rmse4l
#rmse=10302.893706228308

##############exp transformation##################

plt.scatter(x=salhk['YearsExperience'],y=salhk['Salary'],color='blue')
#strong correlation
np.corrcoef(salhk.YearsExperience,salhk.Salary)
#0.97824162

model4e=smf.ols('np.log(Salary)~YearsExperience',data=salhk).fit()
model4e.summary()
#R-squared:0.932=>strong correlation
#Prob (F-statistic):7.03e-18=>overall model is good

pred4e_log=model4e.predict(pd.DataFrame(salhk['YearsExperience']))
pred4e_log
pred4e=np.exp(pred4e_log)
pred4e
print(model4e.conf_int(0.01))


res4e=salhk.Salary-pred4e
sqres4e=res4e*res4e
mse4e=np.mean(sqres4e)
rmse4e=np.sqrt(mse4e)
rmse4e
#7213.235076620129