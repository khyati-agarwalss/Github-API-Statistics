# To be run after running 'code_frequency.py'

library(ggplot2)
options(stringsAsFactors = FALSE)

code_frequency <- read.csv(file = "C:/Users/Khyati Agarwal/Desktop/code_frequency.csv")     # CSV File Location

lgd <- scale_color_manual("Legend", values = c(Addition = "green4", Deletion = "firebrick1"))

ggplot()+
  geom_line(data = code_frequency, aes(x = week, y = additions, color = "Addition", group = 1), size = 1.1) + 
  geom_line(data = code_frequency, aes(x = week, y = deletions, color = "Deletion", group = 1), size = 1.1) + 
  labs(x = "Week", y = "Additions / Deletions", title = "Code frequency")
