library("jiebaR")
library(tm)
library(tmcn)
library(stringr)
library(dplyr)
library(xlsx)
library(readxl)
library(ggplot2)
library(wordcloud2)
library(devtools)

getwd()
setwd("D:/python/應用程式/appproject") #設在檔案在的位置
L <- read.csv( "chang.csv" ,encoding = "UTF-8", header = 0)

autocc <- function(L){
  cc = worker()
  keep <- c()
  #new_user_word(cc, keep)可放入要加入的特定詞語
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
hot50  <- function(H){wordcloud2(head(H,50))}

colnames(L)[4] = "content"
L.data = autocc(L)
hot50(L.data)
