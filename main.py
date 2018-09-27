import post_crawler as pc

feed_csv = "feed.csv"
out_dir = "output"

csv = open(feed_csv)
count = 1

crawler = pc.crawler()

for line in csv:
    querry = line.strip()
    if "-" in querry:
        splt = querry.split("-")
        querry = ""
        for el in splt:
            querry = querry + el
    if len(querry) != 13 or not querry.isdigit():
        continue
    crawler.save_screenshot(querry, out_dir)
    print("JOB Number " + str(count) + " Done.\n>>>>>" + querry)
    count += 1

crawler.kill()