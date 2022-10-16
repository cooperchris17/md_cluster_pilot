# https://stackoverflow.com/questions/27485549/how-to-colour-the-labels-of-a-dendrogram-by-an-additional-factor-variable-in-r

library(dendextend)

yt <- read.csv('random_bnc200_dim.csv', row.names = 1)
head(yt)
tail(yt)

data <- yt[,1:6]
head(data)

# Agglomerative clustering, using the default method 'complete'
# 'The algorithm compares the farthest neighbours in all pairs 
# of clusters and merges those clusters whose farthest neighbours
# are the closest' (Levshina, 2015, p. 310). 
# Ward.D2 might also be usable
dend <- as.dendrogram(hclust(dist(data)))

# Change the colors: YouTube '2'(red), BNC '4'(blue)
labels_colors(dend) <- as.numeric(yt[,10][order.dendrogram(dend)])
# Change the labels to 'Y' and 'B' 
# still can't read, but it's a bit cleaner
labels(dend) <- paste(as.character(yt[,9])[order.dendrogram(dend)])

plot(dend)

library(cluster)

# use silhouette to test which number of clusters is optimal
# I am checking from 2 to 15 clusters
asw <- sapply(2:15, function(x) summary(silhouette(cutree(dend, 
              k = x), dist(data)))$avg.width)

# highest asw is actually 3 (0.2929944), but it is very similar to 2 (0.2924318)
# the 3rd cluster is very small and I'm only interested in the main BNC cluster
# 2 clusters would give me these texts
asw


# give each text a label in df with cluster number (class-1 or class-2)
# https://stackoverflow.com/questions/50856937/how-to-add-cluster-id-in-a-seperate-column-of-a-dataframe

solution <- cutree(dend, k = 2)
solution

res <- cbind(yt, Class = factor(unname(solution), labels = c("class-1", "class-2")))
head(res)

write.csv(res,'yt_bnc_clusters.csv')

# from counting with pandas, I could see that 'Class-2' is the 
# one I am looking for (with the most BNC texts)
# 666 YouTube texts belong to the same cluster as BNC (1936 in the other cluster)
