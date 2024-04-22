library(tidyverse) #collection of packages we will use
library(lubridate) #date time manipulation
library(magrittr) #forward pipe operator


install.packages("magrittr")


big_mac_data <- read.csv("big-mac-historical-source-data.csv")
View(big_mac_data)

big_mac_data$date <- ymd_hms(big_mac_data$date)

countries_of_interest <- c("United States", "Canada", "Australia", "India", "Germany")
filtered_data <- big_mac_data %>% filter(name %in% countries_of_interest )

View(filtered_data)


ggplot(filtered_data, aes(x = date, y = local_price, color = name)) + 
  geom_line() + labs(title = "Time Series Analysis of Big Mac Prices", x = "Year", "Local Price", color = "Country") +
  theme_minimal()

big_mac_data <- big_mac_data %>% mutate(PPP = local_price / dollar_ex)

View(big_mac_data)

recent_date_data <- big_mac_data %>% filter(date == max(date))


ggplot(recent_date_data, aes(x = reorder(name, PPP), y = PPP, fill = name)) + 
  geom_bar(stat = "identity") + labs(title = "Purchasing Power Parity of Big Macs in 1999", x = "Country", y = "PPP (price in USD", 
                              fill = "Country") + theme_dark() + coord_flip()
