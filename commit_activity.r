# To be run after running 'commit_activity.py'

library(ggplot2)
options(stringsAsFactors = FALSE)

commit_activity <- read.csv(file = "C:/Users/Khyati Agarwal/Desktop/commit_activity.csv")     # CSV File location

lgd <- scale_color_manual("Legend", values = c(commits = "firebrick1"))

ggplot() + 
  geom_line(data = commit_activity, aes(x = week, y = total, color = "commits", group = 1), size = 1.1) + 
  labs(x = "Week", y = "Total Commits", title = "Commit Activity (for last year)")
