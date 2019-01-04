question_list =["1.which country is delhi located in?","2.what is the capital of India?","3.where is qutub minar?","4.what is the capital of bihar?","5.who is the cricketer?", "6.The weight of diamonds is usually measured in what?", "7.who is the prime minister of pakistan?", "8.who is the bowler of cricket?", "9.what is the capital of bangladesh?", "10.where is new york?"]
first_option  = ["a.India","a.bihar","a.mumbai","a.madhubani","a.sania mirza","a.tola", "a.Imran khan", "a.murli vijay", "a.turkey", "a.UK"]
second_option =["b.america","b.punjab","b.delhi","b.noida","b.Ms dhoni", "b.carat", "b.banjir bhutto", "b.ishant sharma", "b.islamabad", "b.USA"]
third_option  = ["c.pakistan","c.delhi","c.himachal pradesh","c.patna","c.usain bolt", "c.Maund", "c.Nawaz sarif", "c.mickal clarke", "c.dhaka", "c.India"]
fourth_option =["d.Nepal","d.uttar pradesh","d.kanpur","d.MP","d.modi", "d.Troy", "d.modi", "d.virat kohli", "d.delhi", "d.pakistan"]
# all_option  = [first_option,second_option,third_option,fourth_option]
ans_key=["a","c","b","c","b", "b", "a", "b", "c", "b"]
ans_list=[]
correct_answers=0

price=[1000,2000,3000,5000,10000,200000,40000,80000,160000,320000]
#money of all answers.
a=0
padav=1
while a<len(question_list):

	print question_list[a]
	print first_option[a]
	print second_option[a]
	print third_option[a]
	print fourth_option[a]
	user=raw_input("enter your answer-")
	if user==ans_key[a]:
		print "Congrats! Aapka answer sahi hai",price[a]
		print ""
		correct_answers=1
	else:
		print "Sadly aapka javab galat hai."
		print""
		break
	a=a+1
	if a%5==0:
		print "Congrats! Aapka %spadaav pura ho gaya hai."%padav
		print ""
		padav=padav+1
	ans_list.append(user)
# print len(question_list[a])

