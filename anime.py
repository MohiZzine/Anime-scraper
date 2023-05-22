import requests
from bs4 import BeautifulSoup

# Create URLs
BABY_STEPS_URL = "https://mangaclash.com/manga/baby-steps/"
CLASSROOM_OF_THE_ELITE_URL = "https://www.classroomofelite.com/"
GRAND_BLUE_URL = "https://www.grandbluedreaming.com/"
BLUE_LOCK_URL = "https://w17.readbluelock.com/"

# Create Dictionary of URLs
URLs = {"Baby Steps": BABY_STEPS_URL, "BLUE LOCK": BLUE_LOCK_URL, "Grand Blue": GRAND_BLUE_URL, "Classroom of The Elite": CLASSROOM_OF_THE_ELITE_URL}

def scrape_baby_steps(soup):
  chapters = [chapter.findNext("a") for chapter in soup.find_all("li", class_="wp-manga-chapter")]
  last_chapter_title = chapters[0].text.strip()
  last_chapter_url = chapters[0]["href"]
  # last_chapter_title, last_chapter_date = chapters[0][0].text.strip(), chapters[0][1].text.strip()
  return {'url': last_chapter_url, 'title': last_chapter_title}
  
def scrape_blue_lock(soup):
  chapters = [chapter for chapter in soup.find_all("a", string=lambda text: "Chapter" in text)]
  last_chapter_url = chapters[0]["href"]
  last_chapter_title = chapters[0].text.strip()
  return {'url': last_chapter_url, 'title': last_chapter_title}

def scrape_classroom_of_the_elite(soup):
  chapters = [chapter for chapter in soup.find_all("div", class_="main-chapter-1")]
  last_chapter_link = chapters[0].findNext("a")
  last_chapter_url = last_chapter_link["href"]
  last_chapter_title = last_chapter_link.text.strip()
  return {'url': last_chapter_url, 'title': last_chapter_title}

def scrape_grand_blue(soup):
  chapters = [chapter for chapter in soup.find_all("div", class_="main-chapter-1")]
  last_chapter_link = chapters[0].findNext("a")
  last_chapter_url = last_chapter_link["href"]
  last_chapter_title = last_chapter_link.text.strip()
  return {'url': last_chapter_url, 'title': last_chapter_title}

def scrape_soup(manga, soup):
  match manga:
    case "Baby Steps":
      return scrape_baby_steps(soup)
    case "Classroom of The Elite":
      return scrape_classroom_of_the_elite(soup)
    case "BLUE LOCK":
      return scrape_blue_lock(soup)
    case "Grand Blue":
      return scrape_grand_blue(soup)
      
    
def display_manga_chapters(URLs):
  for manga in URLs:
    page = requests.get(URLs[manga])
    soup = BeautifulSoup(page.content, "html.parser")
    last_chapter_url = scrape_soup(manga, soup)['url']
    last_chapter_title = scrape_soup(manga, soup)['title']
    print(f"{manga}: {last_chapter_title} | {last_chapter_url}")
    print("==============================")
    
    
if __name__ == '__main__':
  display_manga_chapters(URLs)

    
    
