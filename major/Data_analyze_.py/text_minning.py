# # R 텍스트 마이닝 기초

# install.packages('tidytext')
# library(tidytext)

# # 엑셀 파일 -> R 읽어오기
# # 

# raw_moon <- readLines("C:/R/speech_moon.txt", encoding = "UTF-8")
# str(raw_moon)
# head(raw_moon,10)

# # [^가-힣] : 한글이 아닌 모든 문자자
# # 가-힣 : "가" 부터 "힣"까지 모든 한글 문자
# # ^ : 반대(Not)

# library(stringr)
# library(dplyr)

# # 불필요한 문자 제거
# moon <- raw_moon %>% 
#   str_replace_all("[^가-힣]", " ")
# head(moon)

# # 연속된 공백 제거
# moon <- moon %>% 
#   str_squish()
# head(moon)

# # 데이터를 tibble 구조로 바꾸기
# library(dplyr)
# moon <- as_tibble(moon)
# moon

# # 전처리 작업 한번에 하기
# moon <- raw_moon %>% 
#   str_replace_all("[^가-힣]", " ") %>%  # 한글만 남기기기
#   str_squish() %>%                      # 연속된 공백 제거
#   as_tibble()                           # tibble로 변환

# # 연설문 토큰화
# word_space <- moon %>% 
#   unnest_tokens(input = value,   # 토큰화할 텍스트
#                 output = word,   # 토큰을 담을 변수명명
#                 token = "words") # 띄어쓰기 기준준
# word_space

# # 단어 빈도 구하기 → count()
# word_space <- word_space %>%
#     count(word, sort = TRUE)
# word_space
