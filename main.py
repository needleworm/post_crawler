import post_crawler as pc

feed_csv = "feed.csv"

open(feed_csv)
count = 1

for line in feed_csv:
    querry = line.strip()[:-1]
    if len(querry) != 13 or not querry.isdigit():
        continue

    pc.save_screenshot(querry)
    print("JOB Number " + str(count) + " Done.\n>>>>>" + querry)