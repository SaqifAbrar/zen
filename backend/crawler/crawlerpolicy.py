import urllib.robotparser as robotparser

class CrawlerPolicy:
  def __init__(self, base_url):
    self.url = base_url

    self.parser = robotparser.RobotFileParser()
    self.parser.set_url(f"{self.url}/robots.txt")
    self.parser.read()
  
  def validate(self, url, agent = "*"):
    return self.parser.can_fetch(agent, url)


checker = CrawlerPolicy("https://en.wikipedia.org")

print(checker.validate("/api/"))
