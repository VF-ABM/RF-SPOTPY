set.seed(1)
n=600 # number of trees
library(clusterGeneration)
library(mnormt)

X=Input # import input

library(corrplot)
corrplot(cor(X), order = "hclust")

Y=output[ ,25] # import output; choose location for particular cell type

df=data.frame(Y,X)
allX=paste("X",1:ncol(X),sep="")
names(df)=c("Y",allX)
require(randomForest)
fit=randomForest(factor(Y)~., data=df)
VI_F=importance(fit)
library(caret)
varImp(fit)
varImpPlot(fit,type=2)
