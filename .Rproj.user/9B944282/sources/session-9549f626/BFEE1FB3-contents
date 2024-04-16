# Welcome to R! 

# R is an open sourced, command based data manipulation tool. 
# There are some really powerful calculation and visual technologies 
# available just one google search away s
#
# This intro will take a look at 

# Data Modeling 
# Data Analysis and Regression 
# Data Visualization 

# *Data Modeling* 

# Import a data set! 

library(dplyr)
library(ggplot2)

books_daggplot2books_data <- read.csv("books_data.csv")

View(books_data)


#R automatically numebers our data set for us
#so lets remove that using that package dplyr

books_data <- select(books_data, -`X`)

# Im only interested in books that we're written in english 
# So I will create a subset
english_books <- books_data %>%
  filter(Language == "English")

#now we can regress sales in millions to date published
regression_model <- lm(Sales_in_millions ~ First_Published, data = english_books)

summary(regression_model)

#now lets plot this regression

p <- ggplot(english_books_data, aes(x = First_Published, y = Sales_in_millions)) +
  geom_point(alpha = 0.5) +  # Add data points
  geom_smooth(method = "lm", color = "red") +  # Add regression line
  labs(title = "Regression of Sales on Year of Publication for English Books",
       x = "Year of Publication", y = "Sales in Millions") +
  theme_minimal()



#This is to tidy up the x-axis, making it only show every 10 years and include
#ticks in between. 
p + scale_x_continuous(breaks = seq(floor(min(english_books_data$First_Published, na.rm = TRUE)/10)*10, 
ceiling(max(english_books_data$First_Published, na.rm = TRUE)/10)*10, by = 10),
minor_breaks = seq(min(english_books_data$First_Published, na.rm = TRUE), 
max(english_books_data$First_Published, na.rm = TRUE), by = 1))


