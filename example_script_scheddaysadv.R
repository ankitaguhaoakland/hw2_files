#-----------------------------------------------
# R script example - analysis of healthcare data

#-----------------------------------------------

library(plyr)      # A library for data summarization and transformation
library(dplyr)     # A newer library for data summarization and transformation
library(ggplot2)   # A library for plotting

# Read data from csv file
sched_df <- read.csv("data/SchedDaysAdv.csv")  

head(sched_df)  # See the start of the data frame
tail(sched_df)  # See the end of the data frame

## Use summary() to get the 6 number summary
summary(sched_df$ScheduledDaysInAdvance)

## How about some percentiles
p05_leadtime <- quantile(sched_df$ScheduledDaysInAdvance,0.05)
p05_leadtime
p95_leadtime <- quantile(sched_df$ScheduledDaysInAdvance,0.95)
p95_leadtime

# Basic histogram for ScheduledDaysInAdvance. Each bin is 4 wide.
# These both do the same thing:
qplot(sched_df$ScheduledDaysInAdvance, binwidth=4)

ggplot(sched_df, aes(x=ScheduledDaysInAdvance)) + geom_histogram(binwidth=4)

# Draw with black outline, white fill
ggplot(sched_df, aes(x=ScheduledDaysInAdvance)) + geom_histogram(binwidth=4, colour="black", fill="white")

# Density curve
ggplot(sched_df, aes(x=ScheduledDaysInAdvance)) + geom_density()

# Histogram overlaid with kernel density curve
ggplot(sched_df, aes(x=ScheduledDaysInAdvance)) +
  geom_histogram(aes(y=..density..),      # Histogram with density instead of count on y-axis
                 binwidth=4,
                 colour="black", fill="white") +
  geom_density(alpha=.2, fill="#FF6666")  # Overlay with transparent density plot

# A basic box plot by InsuranceStatus
ggplot(sched_df, aes(x=InsuranceStatus, y=ScheduledDaysInAdvance)) + geom_boxplot()

# A basic box with the InsuranceStatus using color
ggplot(sched_df, aes(x=InsuranceStatus, y=ScheduledDaysInAdvance, fill=InsuranceStatus)) + geom_boxplot()

# The above adds a redundant legend. With the legend removed:
ggplot(sched_df, aes(x=InsuranceStatus, y=ScheduledDaysInAdvance, fill=InsuranceStatus)) + geom_boxplot() +
  guides(fill=FALSE)

# With flipped axes and a different grouping field
ggplot(sched_df, aes(x=Urgency, y=ScheduledDaysInAdvance, fill=Urgency)) + geom_boxplot() +
  guides(fill=FALSE) + coord_flip()

## Count(ScheduledDaysInAdvance) by Urgency
tapply(sched_df$ScheduledDaysInAdvance,sched_df$Urgency,length)

## Mean(ScheduledDaysInAdvance) by Urgency
tapply(sched_df$ScheduledDaysInAdvance,sched_df$Urgency,mean)

## Mean(ScheduledDaysInAdvance) by Urgency and store result in an array
meansbyurg <- tapply(sched_df$ScheduledDaysInAdvance,sched_df$Urgency,mean)
meansbyurg

## Count(ScheduledDaysInAdvance) by Urgency using plyr
ddply(sched_df,"Urgency",summarise,numcases=length(ScheduledDaysInAdvance))

## Now let's do mean lead time by Urgency and InsuranceStatus
ddply(sched_df,.(Urgency,InsuranceStatus),summarise,
      mean_leadtime=mean(ScheduledDaysInAdvance),
      numcases=length(ScheduledDaysInAdvance))


## Repeat the above but use dplyr instead of plyr

sched_df %>% 
  group_by(Urgency,InsuranceStatus) %>%
  summarise(mean_leadtime=mean(ScheduledDaysInAdvance),
            numcases=length(ScheduledDaysInAdvance))

  
## Percentiles of lead time by Urgency and Insurance Status
ddply(sched_df,.(Urgency,InsuranceStatus),summarise,
      p95_leadtime=quantile(ScheduledDaysInAdvance,0.95),
      numcases=length(ScheduledDaysInAdvance))

# Faceded histograms with counts
qplot(ScheduledDaysInAdvance, data = sched_df, binwidth=4) + facet_wrap(~ Service)

# Faceded histograms with frequencies
ggplot(sched_df,aes(x=ScheduledDaysInAdvance)) + facet_wrap(~ Service) +
  geom_histogram(aes(y=..density..), binwidth=4)

