#!/root/OF-Scraper/.venv/bin/python
import multiprocessing
import ofscraper.start as start
def main():
    start.startvalues()
    start.discord_warning()
    start.main()

if __name__ == '__main__': 
    multiprocessing.freeze_support()
    main()

    