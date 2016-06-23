#R howto
library(ggplot2)

#load data
beats<-read.table("beatsAll.dat",sep=",")

#sort data by column x
sortedbyYear <- beats[order(beats[1]),]

#rename columns
colnames(sortedbyYear) <- c("year","speech","tempo","key","live","dance","rank","loud","length")

#Get only the top rank
sortedByYearTopRank <- sortedbyYear[sortedbyYear$rank==2,]

#graphing
library(ggplot2)

#simple dot plot
#p<- qplot(data=sortedbyYear,year,length)
p<- qplot(data=sortedByYearTopRank ,year,key)

#ggplot(sortedbyYear,aes(factor(year), fill = factor(key)))+ geom_histogram(binwidth=10)

#Draw dots
#p + geom_abline()
p + geom_quantile()
#p + geom_line(size=2,log='y')
#p + geom_histogram(binwidth=1)
#p + geom_bar()
#p+ stat_smooth()
#p + scale_size(range = c(0,10))

#p + stat_summary(geom="ribbon", fun.data="median_hilow")