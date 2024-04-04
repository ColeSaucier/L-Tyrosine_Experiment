library(ggplot2)

# Data/Variable definitions
data <- data.frame(
  Search_Type = c("Feature", "Conjunction0", "Conjunction1"),
  Slope = c(1.5, 24, 18),
  Std_Dev = c(0.707106781, 9.899494937, 7.071067812)
)

# Plot the bar chart with error bars
p <- ggplot(data, aes(x = Search_Type, y = Slope)) +
  geom_bar(stat = "identity", fill = "maroon", width = 0.4) +
  geom_errorbar(aes(ymin = Slope - Std_Dev, ymax = Slope + Std_Dev), width = 0.2, color = "black", linewidth = 0.7) +
  labs(x = "Search Type", y = "Slope (speed per distractor)") +
  theme_minimal() +
  theme(axis.text.x = element_text(size = 14), axis.text.y = element_text(size = 14),
        axis.title.x = element_text(size = 18), axis.title.y = element_text(size = 18))

print(p)