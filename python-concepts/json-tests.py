import json

test = '{"author":"YouthfulPhotographer","author_flair_css_class":null,"author_flair_text":null,"body":"Welcome to generation void ","can_gild":true,"controversiality":0,"created_utc":1517443200,"distinguished":null,"edited":false,"gilded":0}'

x = json.loads(test)
print(x['author'], ':', x['body'])

test = """{"author":"YouthfulPhotographer","author_flair_css_class":null,"author_flair_text":null,"body":"Welcome to generation void ","can_gild":true,"controversiality":0,"created_utc":1517443200,"distinguished":null,"edited":false,"gilded":0,"id":"dtjoj2e","is_submitter":false,"link_id":"t3_7uaobc","parent_id":"t1_dtj8323","permalink":"/r/tumblr/comments/7uaobc/nihilism_across_generations/dtjoj2e/","retrieved_on":1518478113,"score":7,"stickied":false,"subreddit":"tumblr","subreddit_id":"t5_2r7hk","subreddit_type":"public"}
{"author":"jasonklacour","author_flair_css_class":null,"author_flair_text":null,"body":"Welcome","can_gild":true,"controversiality":0,"created_utc":1517443200,"distinguished":null,"edited":false,"gilded":0,"id":"dtjoj2l","is_submitter":false,"link_id":"t3_7ude45","parent_id":"t3_7ude45","permalink":"/r/pics/comments/7ude45/7_years_later_im_officially_an_us_citizen_murica/dtjoj2l/","retrieved_on":1518478113,"score":1,"stickied":false,"subreddit":"pics","subreddit_id":"t5_2qh0u","subreddit_type":"public"}
{"author":"Assassin2000","author_flair_css_class":null,"author_flair_text":null,"body":"I'm 16 and the friend told me he was joking after I reported it ","can_gild":true,"controversiality":0,"created_utc":1517443200,"distinguished":null,"edited":false,"gilded":0,"id":"dtjoj2m","is_submitter":true,"link_id":"t3_7uegdc","parent_id":"t1_dtjo9qq","permalink":"/r/legaladvice/comments/7uegdc/took_a_awful_joke_seriously_and_now_im_in_trouble/dtjoj2m/","retrieved_on":1518478113,"score":1,"stickied":false,"subreddit":"legaladvice","subreddit_id":"t5_2rawz","subreddit_type":"public"}"""

for line in test.split('\n'):
    x = json.loads(line)
    print(x['author'], ':', x['body'])