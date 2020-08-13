######################SIMPLE LINEAR REGRESSION##################
#######################QUESTION1################################
cc <- read.csv(file.choose())
View(cc)
attach(cc)
summary(cc)

plot(Weight.gained..grams.,Calories.Consumed)#scatter plot
# positive correlation

cor(Weight.gained..grams.,Calories.Consumed)#correlation 
#|r|=0.946991>0.85=>strong correlation

model <- lm(Weight.gained..grams.~Calories.Consumed)
model
summary(model)
predict(model)
model$residuals
confint(model,level = 0.95)
predict(model,interval = "confidence")
rmse <- sqrt(mean(model$residuals^2))
rmse


######################QUESTION 2#################################

dt <- read.csv(file.choose())
View(dt)
attach(dt)
summary(dt)
plot(Delivery.Time,Sorting.Time)
#moderate positive correlation
cor(Delivery.Time,Sorting.Time)
#0.8259973=>moderate correlation
model2 <- lm(Delivery.Time~Sorting.Time)
summary(model2)
#R-squared:  0.6823
# p-value: 3.983e-06
######log transformation###############
plot(log(Delivery.Time),Sorting.Time)
#moderate positive correlation
cor(log(Delivery.Time),Sorting.Time)
# 0.8431773=>|r|<0.85=>moderate correlation
model_dt <- lm(Sorting.Time~log(Delivery.Time))
summary(model_dt)
#R^2 bw 0.65 & 0.8 =>moderate correlation
#Multiple R-squared:  0.7109
#p-value: 1.593e-06<0.05=> overall model is good
rmse_dt <- sqrt(mean(model_dt$residuals^2))
rmse_dt
#rmse=1.333748(root mean square error)


###########################QUESTION 3################################


emp <- read.csv(file.choose())
View(emp)
attach(emp)
summary(emp)

plot(Salary_hike,Churn_out_rate)
#strong negative correlation

cor(Salary_hike,Churn_out_rate)
#-0.9117216=>strong negative correaltion
model_emp <- lm(Churn_out_rate~Salary_hike)
summary(model_emp)
#R-squared:  0.8312>0.8=>strong correlation
# p-value: 0.0002386<0.05=>overall the model is good
predict(model_emp)
model$residuals
confint(model_emp,level = 0.95)
predict(model_emp,interval = 'confidence')
rmse <- sqrt(mean(model_emp$residuals^2))
rmse
#3.997528

################log transformation################

plot(log(Salary_hike), Churn_out_rate)

cor(log(Salary_hike),Churn_out_rate)
#-0.9212077>0.85=>strong negative  correlation
#slightly increase in the correlaton value
modellog <- lm(log(Churn_out_rate)~Salary_hike)
summary(modellog)
#R-squared:  0.8735>0.8=>strong correlation
#f static p-value: 7.377e-05<0.05=>overall model is good
rmse_3l <- sqrt(mean(modellog$residuals^2))
rmse_3l
#rmse=0.04641748


###################exponential transformation############


plot(Salary_hike,log(Churn_out_rate))
cor(Salary_hike,log(Churn_out_rate))
#|r|=-0.9346361>0.85=>strong -ve correlation
#slighty increse in the value
model_ex <- lm(Churn_out_rate~log(Salary_hike))
summary(model_ex)
#R-squared:  0.8486>0.8=>strong correlation
#p-value: 0.0001532<0.05=>overall model is good
model_ex$residuals
log_churn <- predict(model_ex,interval = 'confidence')
log_churn
churn <- exp(log_churn)
churn
err <- Churn_out_rate-churn
err
rmse <- sqrt(mean(err^2))
rmse
#1.213897e+38
#smaller the rmse better the model is. 


#################polynomial transformation###############


model_emp1 <- lm(log(Churn_out_rate)~Salary_hike+I(Salary_hike*Salary_hike))
summary(model_emp1)
#R-squared:  0.9836>0.8=>STRONG CORRELATION
#p-value: 5.634e-07<0.05=>overall model is good

confint(model_emp1,level = 0.95)

log_res <- predict(model_emp1,level = 'confidence')
ch_ploy <- exp(log_res)
ch_ploy
err_poly <- Churn_out_rate - ch_ploy
rmse <- sqrt(mean(err_poly^2))
rmse
#1.32679


################QUESTION 4###############################

#prediction model for salary high

salhk <- read.csv(file.choose())
View(salhk)
attach(salhk)
summary(salhk)#exploratory data analysis
plot(YearsExperience,Salary)
#strong correlation & positive direction 
cor(YearsExperience,Salary)
#|r|=0.9782416>0.85=>good &strong correlation
model4 <- lm(Salary~YearsExperience)
summary(model4)
#R-squared:  0.957>0.8=>strong correlation
#p-value: < 2.2e-16<0.05=>overall the model is good

predict(model4)
model4$residuals

confint(model4,level = 0.95)
predict(model4,interval = 'confidence')

rmse4 <- sqrt(mean(model4$residuals^2))
rmse4
# 5592.044


###############log transformation###################

plot(log(YearsExperience),Salary)
#curvilinear correlation
cor(log(YearsExperience),Salary)
#0.9240611>0.85=>good correlation
#slighly decreace in the value |r|

model4l <- lm(log(Salary)~YearsExperience)
summary(model4l)
##################exp tranformation###############
plot(YearsExperience,log(Salary))
#positive correlation
cor(YearsExperience,log(Salary))
# 0.9653844>0.85=>good correltion
model4exp <- lm(log(Salary)~YearsExperience)
summary(model4exp)
#R-squared:  0.932>0.8=>strong correaltion
#p-value: < 2.2e-16<0.05=>overall model is good
model4exp$residuals

log_sal<- predict(model4exp,interval = 'confidence')
log_sal
sal <- exp(log_sal)
sal
err4 <- Salary-sal
err4
rmse4 <- sqrt(mean(err4^2))
rmse4
#8177.02

###################polynomial transformation##############

model4p <- lm(log(Salary)~YearsExperience+I(YearsExperience*YearsExperience))
summary(model4p)
# 0.9486>0.8=>good correlation
#p-value: < 2.2e-16<0.05=>overall the model is good 

log_res4 <- predict(model4p,interval = 'confidence')
log_res4
salpoly <- exp(log_res4)
salpoly
err4_poly <- Salary-salpoly
err4_poly
rmse4_poly <- sqrt(mean(err4_poly^2))
rmse4_poly
#6676.884