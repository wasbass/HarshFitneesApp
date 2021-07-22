{
library("jiebaR")
library(tm)
library(tmcn)
library(dplyr)
library(wordcloud2)
library(readxl)
}
getwd()
setwd("D:/python/appproject") #設在檔案在的位置
#L <- read.csv("chang.csv" , sep = "," ,fileEncoding = "UTF-8",header = 0)
L <- read_excel("chang.xlsx", col_names = T)[5]


autocc <- function(L){
  cc = worker()
  keep <- c("柯文哲","柯市長")
  new_user_word(cc, keep)#可放入要加入的特定詞語
  
  L.cc <- cc[as.character(L$content)]
  L.df <- data.frame(table(L.cc))
  
  L.df %>%
    filter(nchar(as.character(L.cc)) > 1) -> L.df
  
  #stopword <- c()
  
  #for ( j in stopword){
  #L.df <- L.df[L.df$L.cc != j,]
  #}可刪除特定詞語
  
  L.fn <- L.df[order(L.df$Freq,decreasing = TRUE),]
  return(L.fn)
}

hot <- function(H,count){wordcloud2(head(H,count),shape = "star" , size = 1)}

#colnames(L)[1] = "content"
L_data = autocc(L)
hot(L_data,100)

